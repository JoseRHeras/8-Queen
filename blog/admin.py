from django.contrib import admin
from .models import article
from .models import article_image

admin.site.register(article)
admin.site.register(article_image)