from django.shortcuts import render
from django.http import HttpResponse
from .models import Contact
from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.core.mail import BadHeaderError, EmailMessage



# Create your views here.
def home(request):
	
	if request.method=="POST":
		#contact.contact()
		 name=request.POST.get('name')
		 email=request.POST.get('email')
		 subject=request.POST.get('subject')
		 #contact.name=name
		 #contact.email=email
		 #contact.subject=subject
		 #Contact.save()
		 print(name, email, subject)
		 #contact = contact(name=name, email=email, subject=subject)
		 contact = Contact(name=name, email=email, subject=subject)
		 contact.save()

		 return HttpResponse("Thank you for your response, our team will catch you soon")
	return render(request, 'app1/index.html')
 



# def contact(request):
#     #check for POST requests on load.
#     request.method == 'POST'
#     name = request.POST.get('name')
#     message = request.POST.get('message')
#     email = request.POST.get('email')

#     if name and message and email:
#         try:
#             send_mail(name, message, email, ['adam1edinburgh@gmail.com'])
#         except BadHeaderError:
#             return HttpResponse('Invalid header found.') 
#         return HttpResponse('Thanks for your email')

#     else:
#         #loading contacts.html if no requests
#         return render(request, 'app1/index.html')

