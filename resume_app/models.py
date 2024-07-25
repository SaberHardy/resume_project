from django.db import models


class AboutMe(models.Model):
    about_me = models.TextField()
    full_name = models.CharField(max_length=100)
    profile_title = models.CharField(max_length=100)
    profile_image = models.ImageField(upload_to='img/')
    email = models.EmailField()
    linkedin = models.URLField()
    github = models.URLField()
    youtube = models.URLField()

    def __str__(self):
        return self.full_name
