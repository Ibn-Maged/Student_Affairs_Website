# Generated by Django 4.2.1 on 2023-05-19 21:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('StudentAffairs', '0013_alter_student_studentstatus'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('Id', models.IntegerField(primary_key=True, serialize=False)),
                ('userId', models.CharField(max_length=8)),
                ('userName', models.CharField(max_length=40)),
                ('userPassword', models.CharField(max_length=8)),
            ],
        ),
    ]