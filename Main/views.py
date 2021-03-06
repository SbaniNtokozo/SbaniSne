from django.shortcuts import render


# Create your views here.

def homepage(request):
    return render(request, template_name='Main/home.html')


def dashboard(request):
    return render(request, template_name='Main/dashboard.html')


def about(request):
    return render(request, template_name='Main/about.html')



def contact(request):
    return render(request, template_name='Main/contact.html')


def faq(request):
    return render(request, template_name='Main/faq.html')


