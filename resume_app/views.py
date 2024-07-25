from django.shortcuts import render

from .models import AboutMe


def home(request):
    all_properties = AboutMe.objects.all()
    context = {'all_properties': all_properties}
    return render(request, 'resume_app/home.html', context)
