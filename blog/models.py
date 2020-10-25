from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class article(models.Model):
    title = models.CharField( max_length=50)
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