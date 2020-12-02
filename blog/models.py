from django.db import models
from PIL import Image


class HomePageProfile(models.Model):
    first_name = models.CharField(max_length=30)
    middle_name_initial = models.CharField(max_length=1, default=None)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(max_length=150)
    github_link = models.URLField(max_length=200)
    linkedin_link = models.URLField(max_length=200)
    profile_image = models.ImageField(default='default_user_pic.jpg', upload_to="home_page_pic")
    about_me = models.TextField()
    location = models.CharField(max_length=50)


    def __str__(self):
        return f"{self.first_name} {self.last_name} profile"

    def save(self):
        super().save()

        img = Image.open(self.profile_image.path)

        if(img.height > 300 or img.width > 300):
            new_size = (300, 300)
            img.thumbnail(new_size)
            img.save(self.profile_image.path)

class SectionHeader(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    logo = models.CharField(max_length=80)


    def __str__(self):
        return f"{self.name} header data"