# Generated by Django 2.2.3 on 2021-04-05 08:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('studentid', models.CharField(max_length=20, unique=True)),
                ('student_password', models.CharField(max_length=20)),
                ('student_email', models.CharField(max_length=40)),
                ('student_mobile', models.CharField(max_length=10)),
            ],
            options={
                'db_table': 'student',
            },
        ),
    ]