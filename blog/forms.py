from django.forms import widgets
from .models import Feedback, Student, School, Staff, Attendance, Announcement
from django import forms

class StudentAddForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ('__all__') 
        # ("payment_date", "student_name", "payable_towards", "amount_paid", "account_name", "receipt_number", "paid_by", "name")

class SchoolAddForm(forms.ModelForm):
    class Meta:
        model = School
        fields = ('__all__')

class StaffAddForm(forms.ModelForm):
    class Meta:
        model = Staff
        fields = ('name', 'id_number', 'Occupation', 'extra_role', 'gender', 
        'grade', 'salary', 'phone', 'certified', 'dob', 'day_recruited', 
        'day_retirement', 'next_of_kin', 'kin_contact', 'photo', 'transfered')
        
        # widgets = {
        #     'name': forms.TextInput(attrs={'class': 'form-control'}),
        #     'id_number': forms.TextInput(attrs={'class': 'form-control'}),
        #     'Occupation': forms.TextInput(attrs={'class': 'form-control'}),
        #     'extra_role': forms.TextInput(attrs={'class': 'form-control'}),
        #     'gender': forms.Select(attrs={'class': 'form-control'}),
        #     'grade': forms.Select(attrs={'class': 'form-control'}),
        #     'salary': forms.TextInput(attrs={'class': 'form-control'}),
        #     'phone': forms.TextInput(attrs={'class': 'form-control'}),
        #     'certified': forms.CheckboxInput(attrs={'class': 'form-control'}),
        #     'dob': forms.TextInput(attrs={'class': 'form-control'}),
        #     # 'day_recruited': forms.DateInput(attrs={'class': 'form-control', 'placeholder': 'Select Date', 'type': 'date'}),
        #     # 'day_retirement': forms.DateInput(attrs={'class': 'form-control', 'placeholder': 'Select Date', 'type': 'date'}),
        #     'day_recruited': forms.TextInput(attrs={'class': 'form-control'}),
        #     'day_retirement': forms.TextInput(attrs={'class': 'form-control'}),
        #     'next_of_kin': forms.TextInput(attrs={'class': 'form-control'}),
        #     'kin_contact': forms.NumberInput(attrs={'class': 'form-control'}),
        #     'photo': forms.FileInput(),
        #     'transfered': forms.CheckboxInput(attrs={'class': 'form-control'}),
        # }



class TakeAttendanceForm(forms.ModelForm):
    class Meta:
        model = Attendance
        fields = ('name', 'morning', 'afternoon')

        widgets = {
            'name': forms.Select(attrs={'class': 'form-control'}),
            # 'day': forms.TextInput(attrs={'class': 'form-control'}),
            'morning': forms.TextInput(attrs={'class': 'form-control'}),
            'afternoon': forms.TextInput(attrs={'class': 'form-control'}),

        }


class AnnouncementForm(forms.ModelForm):
    class Meta:
        model = Announcement
        fields = ('poster', 'title', 'post')

        widgets = {
            'poster': forms.Select(attrs={'class': 'form-control'}),
            # 'date': forms.TextInput(attrs={'class': 'form-control'}),
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'post': forms.TextInput(attrs={'class': 'form-control'}),

        }

class StaffUpdateForm(forms.ModelForm):
    class Meta:
        model = Staff
        fields = ('__all__')

class StudentUpdateForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ('__all__')

class NewsUpdateForm(forms.ModelForm):
    class Meta:
        model = Announcement
        fields = ('__all__')

class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = ('name', 'email', 'title', 'details')
    
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.TextInput(attrs={'class': 'form-control'}),
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'details': forms.Textarea(attrs={'class': 'form-control'})
        }
