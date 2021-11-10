from .models import Announcement, Friend, Student, Staff, Feedback
from django.shortcuts import get_object_or_404, render, redirect
from .forms import FeedbackForm, NewsUpdateForm, AnnouncementForm, TakeAttendanceForm, StudentAddForm, SchoolAddForm, StaffAddForm, StudentUpdateForm, StaffUpdateForm
from django.contrib import messages

def news(request):
    context = {
        'news': Announcement.objects.all()
    }
    return render(request, 'blog/news.html', context)

def students(request):
    context = {
        'students': Student.objects.all(),
        'nostudents': len(Student.objects.all()),
        'boys': len(Student.objects.filter(gender='Male')),
        'girls': len(Student.objects.filter(gender='Female')),
    }
    return render(request, 'blog/grade.html', context)

def staffs(request):
    context = {
        'staffs': Staff.objects.all()
    }
    return render(request, 'blog/staff.html', context)

def staff_details(request, id):
    context = {
        'staffs': Staff.objects.get(id=id)
    }
    return render(request, 'blog/staff_details.html', context)


def staff_delete(request, id):
    context = {
        'staffdelete': Staff.objects.get(id=id).delete()
    }
    return redirect('staff')


def student_details(request, id):
    context = {
        'studentdetails': Student.objects.get(id=id)
    }
    return render(request, 'blog/studentdetails.html', context)


def student_delete(request, id):
    context = {
        'studentdelete': Student.objects.get(id=id).delete()
    }
    return redirect('classlist')


def add_student(request):
    if request.method=='POST':
        form = StudentAddForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, f'Student Added')
            return redirect('classlist')
    else:
        form = StudentAddForm()
    return render(request, 'blog/add_student.html', {'form':form})

def student_update(request, id):
    context = {}
    student = get_object_or_404(Student, id=id)
    form = StudentUpdateForm(request.POST or None, instance=student)
    if form.is_valid():
        form.save()
        messages.success(request, f'Student Information Updated')
        return redirect('classlist')
    context['form'] = form
    return render(request, 'blog/update_student.html', context)


def staff_update(request, id):
    context = {}
    staff = get_object_or_404(Staff, id=id)
    form = StaffUpdateForm(request.POST or None, instance=staff)
    if form.is_valid():
        form.save()
        messages.success(request, f'Staff Information Updated')
        return redirect('staff')
    context['form'] = form
    return render(request, 'blog/update_staff.html', context)


def news_update(request, id):
    context = {}
    news = get_object_or_404(Announcement, id=id)
    form = NewsUpdateForm(request.POST or None, instance=news)
    if form.is_valid():
        form.save()
        messages.success(request, f'Announcement Updated')
        return redirect('news')
    context['form'] = form
    return render(request, 'blog/updatenews.html', context)

def add_school(request):
    if request.method=='POST':
        form = SchoolAddForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, f'School Added')
            return redirect('classlist')
    else:
        form = SchoolAddForm()
    return render(request, 'blog/add_sch.html', {'form':form})


def add_staff(request):
    if request.method=='POST':
        form = StaffAddForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, f'Member of Staff Added')
            return redirect('staff')
    else:
        form = StaffAddForm()
    return render(request, 'blog/add_staff.html', {'form':form})


def take_attendance(request):
    if request.method=='POST':
        form = TakeAttendanceForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, f'Class Attendance Taken')
            return redirect('classlist')
    else:
        form = TakeAttendanceForm()
    return render(request, 'blog/take_attendance.html', {'form':form})


def make_announcement(request):
    if request.method=='POST':
        form = AnnouncementForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, f'Class Attendance Taken')
            return redirect('news')
    else:
        form = AnnouncementForm()
    return render(request, 'blog/make_announcement.html', {'form':form})


def news_details(request, id):
    context = {
        'news': Announcement.objects.get(id=id)
    }
    return render(request, 'blog/newsdetails.html', context)

def news_delete(request, id):
    context = {
        'newsdelete': Announcement.objects.get(id=id).delete()
    }
    return redirect('news')

def list_feedback(request):
    context = {
        'feedbacks': Feedback.objects.all()
    }
    return render(request, 'blog/feedback_list.html', context)

def send_feedback(request):
    if request.method=='POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, f'Feedback Sent')
            return redirect('feedbacklist')
    else:
        form = FeedbackForm()
    return render(request, 'blog/feedback.html', {'form':form})

def feedback_details(request, id):
    context = {
        'news': Feedback.objects.get(id=id)
    }
    return render(request, 'blog/feedbackdetails_.html', context)

def feedback_delete(request, id):
    context = {
        'feedbackdelete': Feedback.objects.get(id=id).delete()
    }
    return redirect('feedbacklist')

def navbar(request):
    return render(request, 'blog/navbar.html')

def nav(request):
    return render(request, 'blog/nav.html')