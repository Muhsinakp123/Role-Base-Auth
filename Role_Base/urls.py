from django.urls import  path

from Role_Base import views

urlpatterns = [
    path('',views.login_View, name='login'),
    path('signup/',views.signup, name='signup'),
    path('logout/', views.logout_view, name='logout'),

    path('dashboard/student/', views.student_dashboard, name='student_dashboard'),
    path('dashboard/teacher/', views.teacher_dashboard, name='teacher_dashboard'),
    path('dashboard/admin/', views.admin_dashboard, name='admin_dashboard'),
]