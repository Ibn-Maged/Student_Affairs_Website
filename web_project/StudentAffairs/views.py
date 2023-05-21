from django.shortcuts import render, redirect
from django.template import loader
from django.http import HttpResponse

from .forms import StudentForm, UserForm
from .models import Student, User


def index(request):
    return render(request, "app/index.html")


def add_profile(request):
    stud_form = StudentForm()

    last_id = 0

    if Student.objects.count() > 0:
        last_id = Student.objects.order_by('-pk')[0]

    # print(last_id)
    ctx = {"lastID": last_id} 


    if request.method == "POST":
        student = Student()
        
        # if stud_form.is_valid():
        #     stud_form.save()

        student.sid = request.POST['studentID']
        student.name = request.POST['studentName']
        student.dateOfBirth = request.POST['studentBirthDate']
        student.gpa = request.POST['studentGPA']
        student.level = request.POST['studentLevel']
        student.department = request.POST.get('studentDepartment', "")
        student.email = request.POST['studentEmail']
        student.phone = request.POST['studentPhone']
        student.gender = request.POST['studentGender']
        student.status = request.POST.get('studentStatus', "0")

        # print(student.id)
        # print(student.name)
        # print(student.dateOfBirth)
        # print(student.gpa)
        # print(student.level)
        # print(student.department)
        # print(student.email)
        # print(student.phone)
        # print(student.gender)
        # print(student.status)

        # stud_form = StudentForm(request.POST)
        # print(stud_form)

        # stud_form = StudentForm(request.POST, instance=student)

        stud_form = StudentForm(request.POST)
        # print(stud_form)
        if stud_form.is_valid():
            # print("done")
            stud_form.save()
            return redirect(all_students)
        ctx["submittedForm"] = stud_form
        return render(request,'app/show_profile.html', context=ctx)
    
    
    return render(request,'app/show_profile.html', context=ctx)


def show_profile(request, st_id):
    
    student = Student.objects.get(studentID=st_id)
    
    ctx = {"stud" : student}

    return render(request,'app/show_profile.html', context=ctx)


def update_profile(request, st_id):
    
    student = Student.objects.filter(studentID=st_id)

    if request.method == "POST":

        if StudentForm(request.POST).is_valid():

            student.update(studentName=request.POST['studentName'])
            student.update(studentBirthDate=request.POST['studentBirthDate'])
            student.update(studentGPA=request.POST['studentGPA'])
            student.update(studentLevel=request.POST['studentLevel'])
            student.update(studentDepartment=request.POST.get('studentDepartment', ""))
            student.update(studentEmail=request.POST['studentEmail'])
            student.update(studentPhone=request.POST['studentPhone'])
            student.update(studentGender=request.POST['studentGender'])
            student.update(studentStatus=request.POST.get('studentStatus', "0"))


            # student.save()

            # print(student.name, student.email)
            # print(request.POST)

            return redirect(all_students)
        ctx = {"submittedForm" : StudentForm(request.POST)}
        return render(request,'app/show_profile.html', context=ctx)
    return render(request,'app/show_profile.html')


def delete_profile(request, st_id):
    
    Student.objects.get(studentID=st_id).delete()

    # student.save()

    # print(student.name, student.email)
    # print(request.POST)

    return redirect(all_students)


def department_assign(request, st_id):
    
    student = Student.objects.filter(studentID=st_id)

    if request.method == "POST":

        if StudentForm(request.POST).is_valid():

            student.update(studentName=request.POST['studentName'])
            student.update(studentBirthDate=request.POST['studentBirthDate'])
            student.update(studentGPA=request.POST['studentGPA'])
            student.update(studentLevel=request.POST['studentLevel'])
            student.update(studentDepartment=request.POST.get('studentDepartment', ""))
            student.update(studentEmail=request.POST['studentEmail'])
            student.update(studentPhone=request.POST['studentPhone'])
            student.update(studentGender=request.POST['studentGender'])
            student.update(studentStatus=request.POST.get('studentStatus', "0"))


            return render(request,'app/department_assignment.html')
        
        ctx = {"submittedForm" : StudentForm(request.POST)}
        return render(request,'app/show_profile.html', context=ctx)
    
    return render(request,'app/show_profile.html')


def all_students(request):
    students = Student.objects.all()
    
    return render(request,'app/all_students.html',{"students":students})



def add_user(request):
    form = UserForm()
    last_id = 0

    if User.objects.count() > 0:
        last_id = User.objects.order_by('-pk')[0]

    ctx = {"lastID": last_id} 

    if request.method == 'POST':

        form = UserForm(request.POST)
        user = User()
        
        user.userId = request.POST.get('userId','')
        user.userName = request.POST.get('userName','')
        user.userPassword = request.POST.get('userPassword','')
        
        if form.is_valid():
            form.save()
            return render(request, 'home.html', {'message': 'User added successfully'})
        ctx["addUserForm"] = form
        return render(request, 'app/add_user.html', context=ctx)
    
    return render(request,'app/add_user.html', context=ctx)



def view_user(request):
    if request.method == 'POST':
        user_id = request.POST['userId']
        user = User.objects.get(pk=user_id)
        form = UserForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return render(request, 'home.html', {'message': 'User updated successfully'})
    else:
        form = UserForm()

    return render(request, 'view_user.html', {'form': form})


def edit_user(request, selectedId):
    user = User.objects.filter(userId = selectedId)

    if request.method == "POST":

        if UserForm(request.POST).is_valid():

            user.update(userName = request.POST['userName'])
            user.update(userId = request.POST['userId'])
            user.update(password = request.POST['userPassword'])
            
            return redirect(all_students)
        ctx = {"editUserForm" : UserForm(request.POST)}
        return render(request,'app/show_profile.html', context=ctx)
    return render(request,'app/show_profile.html')


def delete_user(request, deletedId):
    
    Student.objects.get( userId = deletedId).delete()
    return render(request, 'home.html', {'message': 'User deleted successfully'})
