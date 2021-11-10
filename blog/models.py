from typing import AsyncGenerator
from django.db import models
from django.utils import timezone
from datetime import datetime
from phone_field import PhoneField
from datetime import date
from django.urls import reverse
from django.contrib.auth.models import User

# Create your models here.
# friends
# company
# hobby
# blood group
# Address

class Friend(models.Model):
    name = models.CharField(max_length=100)
    gender = models.CharField(max_length=20)
    occupation = models.CharField(max_length=100)
    town = models.CharField(max_length=100)
    bio = models.TextField()
    dob = models.DateTimeField(default=timezone.now)
    # phone = models.PhoneNumberField(_(""))
    email = models.EmailField()    

    def __str__(self):
        return self.name

gender = (
    ("Male", "Male"),
    ("Female", "Female"),
)

grade = (
    (-3, "Playgroup",),
    (-2, 'PP1'),
    (-1, 'PP2'),
    (1, 'G1'),
    (2, 'G2'),
    (3, 'G3'),
    (4, 'G4'),
    (5, 'G5'),
    (6, 'G6'),
    (7, "General Teacher"),
    (8, "Support Staff"),
    (9, "Administrative Staff"),
        
)

class School(models.Model):
    school_name = models.CharField(max_length=100)
    post_box = models.IntegerField()
    town = models.CharField(max_length=100)

    def __str__(self):
        return str(self.school_name)


class Student(models.Model):
    student_name = models.CharField(max_length=100, null=True)
    extra_role = models.CharField(max_length=100, default='None', null=True)
    gender = models.CharField(max_length=20, choices = gender, default = "female")
    dob = models.DateField(null=True, blank=True)
    grade = models.IntegerField(choices=grade)
    parent_phone = PhoneField(blank=True, help_text='Contact phone number')
    # admission_date = models.DateField(null=True, blank=True)
    # admNo = models.AutoField() 
    transfered = models.BooleanField(default=False, verbose_name='Transfered?')

    @property
    def age(self):
        if(self.dob != None):
            age = date.today().year - self.dob.year
            return age

    # @property    
    # def sgrade(self):
    #     if datetime.today().day == 25:
    #         grade = self.grade +1
    #         return grade

    
    def sgrade(self):
        if datetime.now().day == 26:
            grade = self.grade +1
            return grade
    
    def __str__(self):
        return self.student_name
    
class Staff(models.Model):
    name = models.OneToOneField(User, on_delete=models.CASCADE)
    # username = User.username
    id_number = models.IntegerField(blank=False, null=False)
    Occupation = models.CharField(max_length=100)
    extra_role = models.CharField(max_length=100, default='None', null=True)
    gender = models.CharField(max_length=20, choices=gender)
    grade = models.IntegerField(choices=grade)
    salary = models.IntegerField(blank=False, null=False)
    phone = PhoneField(blank=True, help_text='Contact phone number')
    certified = models.BooleanField(default='No')
    dob = models.DateField(null=True, blank=True)
    day_recruited = models.DateField(null=True, blank=True)
    day_retirement = models.DateField(null=True, blank=True)
    next_of_kin = models.CharField(max_length=100)
    kin_contact = PhoneField(blank=True, help_text='Contact phone number')
    photo = models.ImageField(default='john.png', upload_to='profile_photos')
    transfered = models.BooleanField(default=False, verbose_name='Transfered?')

    # age = models.PositiveIntegerField(default=0)
    # subject / specialty = 

    def __str__(self):
        return str(self.name)

    @property
    def age(self):
        if(self.dob != None):
            age = date.today().year - self.dob.year
            return age
        
    def get_absolute_url(self):
        return reverse("staff", kwargs={"pk": self.pk})
    
    
    # @property
    # def grade(self):
    #     if datetime.today().month == 1:
    #         grade = self.grade +1
    #         return grade


class Attendance(models.Model):
    name = models.ForeignKey(Student, on_delete=models.CASCADE)
    day = models.DateTimeField(auto_now=True)
    morning = models.BooleanField(default=False)
    afternoon = models.BooleanField(default=False)

    def __str__(self):
        return str(self.day)


class Announcement(models.Model):
    poster = models.ForeignKey(Staff, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now=True)
    title = models.CharField(max_length=100)
    post = models.TextField()

    def __str__(self):
        return str(self.poster)

class Feedback(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    date = models.DateTimeField(auto_now=True)
    title = models.CharField(max_length=100)
    details = models.TextField()

    def __str__(self):
        return str(self.title)