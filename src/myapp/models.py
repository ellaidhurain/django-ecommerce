from django.db import models # django model for storing data
from ckeditor.fields import RichTextField

class Editor(models.Model):
    body=RichTextField(blank=True,null=True)


class Template(models.Model):
    GENDER =(
        ('MALE','male'),
        ('FEMALE', 'female'),
        ('OTHERS', 'others')
    )
    student_id  = models.AutoField(primary_key=True,unique=True) 
    student_name = models.TextField(max_length=200, null=True, blank=False,)  
    father_name = models.TextField(max_length=200, null=True, blank=False)
    mother_name = models.TextField(max_length=200, null=True, blank=False)
    gender = models.CharField( max_length=50, blank=False, null=True, choices=GENDER)
    standard = models.TextField(max_length=200, null=True, blank=False)
    section = models.TextField(null=True, blank=False)
    school_name = models.TextField(max_length=200, null=True, blank=False)
    date_of_birth =  models.DateField( auto_now=False, auto_now_add=False)
    admission_no = models.PositiveIntegerField(blank=False,unique=True)
    tc_no = models.PositiveIntegerField(blank=False,unique=True)
    
    
    
    def __str__(self):
        return self.student_name