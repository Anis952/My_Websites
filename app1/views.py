from django.shortcuts import render
from django.http import HttpResponse
from .models import Contact



# Create your views here.
def home(request):
   return render (request, 'app1/index.html')


def contact(request):
	if request.method=="POST":
		#contact.contact()
		 name=request.POST.get('name')
		 email=request.POST.get('email')
		 subject=request.POST.get('message')
		 #contact.name=name
		 #contact.email=email
		 #contact.subject=subject
		 #Contact.save()
		 print(name, email, subject)
		 #contact = contact(name=name, email=email, subject=subject)
		 contact = Contact(name=name, email=email, message=message)
		 contact.SendNow()

		 return HttpResponse("Thank you for your response, our team will catch you soon")
	return render(request, 'app/index.html')   