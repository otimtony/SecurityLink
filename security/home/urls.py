from django.urls import path,re_path
from django.conf.urls import url
from . import views
from .views import JobListView, JobDetailView, JobUpdateView, JobDeleteView, JobCreateView, clientListView, clientDetailView, clientDeleteView
from django.contrib.auth.views import LoginView, LogoutView, PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required

app_name='home'

urlpatterns = [

    path('', views.profile, name='home'),
    path('register/', views.client, name='register'),
    path('job/', views.jobMart, name='jobmart'),
    path('gallery/', views.gallery, name='gallery'),
    re_path(r'^job_detail/(?P<id>[0-9]+)/$', views.jdetail, name='detail'),
    path('dashboard/', views.dash, name='dash'),
    path('dashboard/jobs/', views.JobListView, name='jobs'),
    path('dashboard/<int:pk>/detail', views.JobDetailView.as_view(), name='job_detail'),
    path('dashboard/Add_job/', views.JobCreateView, name='add_job'),
    path('dashboard/<int:pk>/edit', views.JobUpdateView.as_view(), name='job_update'),
    path('dashboard/<int:pk>/del', views.JobDeleteView.as_view(), name='job_delete'),
    path('dashboard/clientelle/', views.clientListView, name='clientelle'),
    path('dashboard/<int:pk>/clientDetail/', views.clientDetailView.as_view(), name='clientDetail'),
    path('dashboard/<int:pk>/del/', views.clientDeleteView.as_view(), name='clientDel'),
    path('dashboard/testimonials/', views.testimonial, name='testimonial'),
    path('dashboard/testimonials/add_testimonials/', views.add_testimonial, name='add_test'),
    path('dashboard/<int:pk>/del testimonial/', views.testDeleteView.as_view(), name='del_test'),
    path('dashboard/gallery/', views.dash_gallery, name='dash_gallery'),
    path('dashboard/<int:pk>/photo edit/', views.PhotoUpdateView.as_view(), name='dash_gallery_edit'),
    path('dashboard/<int:pk>/del edit/', views.PhotoDeleteView.as_view(), name='dash_gallery_del'),
    path('dashboard/gallery/add_photo/', views.add_photo, name='add_photo'),
    path('videos/', views.yutbe, name='vid_gallery'),
    path('dashboard/videos', views.VidListView, name='vids'),
    path('dasshboard/add video', views.add_video, name='add_video'),
    path('dasshboard/<int:pk>/delete video', views.add_video, name='del_video'),
    path('dashboard/employers/', views.employer, name='employers'),
    path('dashboard/add employer/', views.add_employer, name='add_employer'),
    path('dashboard/<int:pk>/del employer/', views.employerDeleteView.as_view(), name='del_employer'),
    path('dashboard/services/', views.services, name='services'),
    path('dashboard/add service/', views.add_service, name='add_service'),
    path('dashboard/<int:pk>/edit service/', views.serviceUpdateView.as_view(), name='edit_service'),
    path('dashboard/<int:pk>/del service/', views.serviceDeleteView.as_view(), name='del_service'),
    path('dashboard/branch/', views.branches, name='branches'),
    path('dashboard/add branch/', views.add_branch, name='add_branch'),
    path('dashboard/<int:pk>/edit_branch/', views.branchUpdateView.as_view(), name='edit_branch'),
    path('dashboard/<int:pk>/del branch/', views.branchDeleteView.as_view(), name='del_branch'),
    path('login/',LoginView.as_view(template_name='hm/login.html'), name='login'),
    path('logout/',LogoutView.as_view(), name='logout'),
    path('password-reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('password-reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),

]