from django.contrib import admin
from .models import article
from .models import article_image
from .models import user_introduction_data
from .models import HomePageProfile
from .models import SectionHeader

admin.site.register(article)
admin.site.register(article_image)
admin.site.register(user_introduction_data)
admin.site.register(HomePageProfile)
admin.site.register(SectionHeader)