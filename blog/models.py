from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
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

class article(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.title} Article"

class article_image(models.Model):
    article = models.OneToOneField(article, on_delete=models.CASCADE)
    image = models.ImageField(default="default.jpg", upload_to="article_pics")


    def __str__(self):
        return f"{self.article.title} Image"

class user_introduction_data(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    contact_email = models.EmailField(max_length=254)
    github = models.URLField(max_length=200)
    linkedin = models.URLField(max_length=200)
    image = models.ImageField(default='default_user_pic.jpg', upload_to="user_pics")
    slogan = models.TextField()
    location = models.CharField(max_length=50)


    def __str__(self):
        return f"{self.user.first_name} Intro Card"

    def save(self):
        super().save()
        
        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            profile_size = (300, 300)
            img.thumbnail(profile_size)
            img.save(self.image.path)


class SectionHeader(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    logo = models.CharField(max_length=80)


    def __str__(self):
        return f"{self.name} header data"