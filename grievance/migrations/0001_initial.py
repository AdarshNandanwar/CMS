# Generated by Django 2.1.7 on 2019-08-24 18:50

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ApplicationStatus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('attempt', models.IntegerField()),
                ('level', models.IntegerField()),
                ('status', models.IntegerField()),
                ('lastChangedDate', models.DateTimeField()),
                ('discription', models.CharField(max_length=500)),
                ('level1Comment', models.CharField(max_length=500)),
                ('level2Comment', models.CharField(max_length=500)),
                ('newStation', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('student_id', models.CharField(max_length=25, primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(max_length=50)),
                ('contact', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=254)),
                ('champus', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='UserType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('token', models.IntegerField(default=0)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='GrievanceForm',
            fields=[
                ('student_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='grievance.Student')),
                ('cg', models.CharField(max_length=10)),
                ('offShoot', models.CharField(max_length=10)),
                ('allocatedStation', models.CharField(max_length=500)),
                ('preferenceNumberOfAllocatedStation', models.IntegerField()),
                ('natureOfQuery', models.IntegerField()),
                ('applicationDate', models.DateTimeField()),
                ('preferedStation1', models.CharField(max_length=500)),
                ('preferedStation2', models.CharField(max_length=500)),
                ('preferedStation3', models.CharField(max_length=500)),
                ('preferedStation4', models.CharField(max_length=500)),
                ('preferedStation5', models.CharField(max_length=500)),
                ('priority', models.IntegerField()),
            ],
        ),
        migrations.AddField(
            model_name='applicationstatus',
            name='student_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='grievance.Student'),
        ),
        migrations.AlterUniqueTogether(
            name='applicationstatus',
            unique_together={('student_id', 'attempt')},
        ),
    ]
