from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings

def home(request):
	return render(request, 'home.html', {})

def contact(request):
	if request.method=="POST":
		name=request.POST['name']
		email=request.POST['email']
		subject=request.POST['subject']
		message=request.POST['message']
		recipient_list = ['davide.piu.94@gmail.com']

		# send an email
		send_mail(
			email,
			subject,
			message,
			recipient_list)

		return render(request,'contact.html', {'name':name})
	else:
		return render(request, 'contact.html', {})



def about(request):
	return render(request, 'about.html', {})


def blog(request):
	return render(request, 'blog.html', {})


def blog_single(request):
	return render(request, 'blog-single.html', {})


def project(request):
	return render(request, 'project.html', {})

def services(request):
	return render(request, 'services.html', {})

def team(request):
	return render(request, 'team.html', {})

def team(request):
	return render(request, 'team.html', {})


def appointment(request):
	if request.method=="POST":
		your_name=request.POST['your-name']
		vehicle_number=request.POST['vehicle-number']
		date=request.POST['date']
		time=request.POST['time']
		message=request.POST['message']
		recipient_list = ['davide.piu.94@gmail.com']
		# send an email
		appointment= "name: " + your_name + "targa: "+ vehicle_number +"date "+ date +"time: "+time+"message: " +message

		send_mail(
			'Appointment request',
			appointment,
			'davide.piu.94@gmail.com',
			recipient_list
		)

		return render(request,'appointment.html', {
			'your_name':your_name,
			'vehicle_number':vehicle_number,
			'date':date,
			'time':time,
			'message':message})
	else:
		return render(request, 'home.html', {})