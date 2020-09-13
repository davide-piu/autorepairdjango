from django.urls import path
from . import views

urlpatterns = [
	path('', views.home, name="home"),
	path('contact.html', views.contact, name="contact"),
	path('about.html', views.about, name="about"),
	path('blog.html', views.blog, name="blog"),
	path('blog-single.html', views.blog_single, name="blog-single"),
	path('project.html', views.project, name="project"),
	path('services.html', views.services, name="services"),
	path('teams.html', views.team, name="team"),
	path('appointment.html', views.appointment, name="appointment"),

]