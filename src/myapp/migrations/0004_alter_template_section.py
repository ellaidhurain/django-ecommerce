# Generated by Django 4.1.4 on 2023-02-07 15:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_alter_template_admission_no_alter_template_section_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='template',
            name='section',
            field=models.TextField(null=True),
        ),
    ]
