from django.db import models
from ckeditor.fields import RichTextField


class AboutMe(models.Model):
    about_me = RichTextField(blank=True, null=True)
    full_name = models.CharField(max_length=100)
    profile_title = models.CharField(max_length=100)
    profile_image = models.ImageField(upload_to='img/')
    email = models.EmailField()
    linkedin = models.URLField()
    github = models.URLField()
    youtube = models.URLField()

    def __str__(self):
        return self.full_name


class ExperienceModel(models.Model):
    job_title = models.CharField(max_length=100)
    company_name = models.CharField(max_length=100)
    place = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField()
    description = RichTextField(blank=True, null=True)

    def __str__(self):
        return str(self.company_name) + ' __ ' + str(self.start_date)


class EducationModel(models.Model):
    degree = models.CharField(max_length=100)
    university = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField()
    description = RichTextField(blank=True, null=True)

    def __str__(self):
        return self.university
