from django.shortcuts import render


def home(request):
    return render(request, 'resume_app/home.html', {})
