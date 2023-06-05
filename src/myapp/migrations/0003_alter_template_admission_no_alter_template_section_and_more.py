# Generated by Django 4.1.4 on 2023-02-07 15:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_template'),
    ]

    operations = [
        migrations.AlterField(
            model_name='template',
            name='admission_no',
            field=models.PositiveIntegerField(unique=True),
        ),
        migrations.AlterField(
            model_name='template',
            name='section',
            field=models.TimeField(null=True),
        ),
        migrations.AlterField(
            model_name='template',
            name='student_id',
            field=models.AutoField(primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='template',
            name='tc_no',
            field=models.PositiveIntegerField(unique=True),
        ),
    ]
