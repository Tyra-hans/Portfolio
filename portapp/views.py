from django.conf import settings
from django.core.mail import send_mail
from django.template.loader import get_template
from django.shortcuts import render
from django.http import HttpResponse


from .forms import ContactForm

def welcome(request):
    return render(request, 'home.html')

# def contact(request):

    # trial1
    # if request.method == 'POST':
    #     message= request.POST['message']
    #     send_mail('Contact Form',
    #     message,
    #     settings.EMAIL_HOST_USER, ['tyrahans17@gmail.com'])
        

  
    # return render(request,'contact.html')


# trial2
    # if request.method == 'POST':
        
    #     form = ContactForm(request.POST)
    #     if form.is_valid():
    #         # send email code goes here
    #         sender_name = form.cleaned_data['name']
    #         sender_email = form.cleaned_data['email']
    #         subject = 'Contact form received'
    #         from_email = settings.DEFAULT_FROM_EMAIL
    #         to_email = [settings.DEFAULT_FROM_EMAIL]

    #         message = "{0} has sent you a new message: \n\n{1}".format(sender_name,form.cleaned_data['message'])
    #         send_mail('New Enquiry',message,sender_email,['tyrahans17@gmail.com'], fail_silently=False)
    #         return HttpResponse('Thanks for contacting me !')

    # else:
    #     form = ContactForm()

    # return render(request,'contact.html', {'form':form})
    