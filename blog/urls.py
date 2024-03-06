from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('class/', views.students, name='classlist'),
    path('staff/', views.staffs, name='staff'),
    path('staff/<int:id>/', views.staff_details, name='staffdetails'),
    path('staffdelete/<int:id>/', views.staff_delete, name='staffdelete'),
    path('staff/<int:id>/update/', views.staff_update, name='staffupdate'),
    path('student/<int:id>/', views.student_details, name='studentdetails'),
    path('student/<int:id>/update/', views.student_update, name='studentupdate'),
    path('studentdelete/<int:id>/', views.student_delete, name='studentdelete'),
    path('addstudent/', views.add_student, name='addstudent'),
    path('addschool/', views.add_school, name='add_school'),
    path('addstaff/', views.add_staff, name='add_staff'),
    path('takeattendance/', views.take_attendance, name='takeattendance'),
    path('makeannouncement/', views.make_announcement, name='makeannouncement'),
    path('news/', views.news, name='news'),
    path('news/<int:id>/', views.news_details, name='newsdetails'),
    path('news/<int:id>/delete/', views.news_delete, name='newsdelete'),
    path('news/<int:id>/update/', views.news_update, name='newsupdate'),
    path('feedback/', views.send_feedback, name='feedback'),
    path('feedbacklist/', views.list_feedback, name='feedbacklist'),
    path('feedback/<int:id>/', views.feedback_details, name='feedbackdetails'),
    path('feedback/<int:id>/delete/', views.feedback_delete, name='feedbackdelete'),



    path('navbar/', views.navbar, name='navbar'),
    path('nav/', views.nav, name='nav'),

   
]

#if settings.DEBUG:
 #       urlpatterns += static(settings.MEDIA_URL,
  #                            document_root=settings.MEDIA_ROOT)
