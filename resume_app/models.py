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
