# Generated by Django 4.0.1 on 2022-02-06 13:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0005_alter_students_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='students',
            options={'ordering': ['-id']},
        ),
        migrations.AlterField(
            model_name='students',
            name='created_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]