# Generated by Django 3.0.6 on 2020-05-23 16:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lab', '0002_auto_20200523_1604'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dept',
            name='deptno',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='emp',
            name='empno',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
