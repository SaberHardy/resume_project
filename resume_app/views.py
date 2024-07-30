from django.shortcuts import render

from .models import AboutMe, ExperienceModel, EducationModel, CertificationModel


def home(request):
    all_properties = AboutMe.objects.all()
    context = {'all_properties': all_properties}
    return render(request, 'resume_app/index.html', context)


def get_experience(request):
    # order_by('-start_date')
    all_experiences = ExperienceModel.objects.all().order_by('-start_date')

    context = {'all_experiences': all_experiences}
    return context


def get_educations(request):
    # order_by('-start_date')
    all_educations = EducationModel.objects.all().order_by('-start_date')

    context = {'all_educations': all_educations}
    return context


def get_certifications(request):
    # order_by('-start_date')
    all_certifications = CertificationModel.objects.all()

    context = {'all_certifications': all_certifications}
    return context
