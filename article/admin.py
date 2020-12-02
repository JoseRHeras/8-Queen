from django.contrib import admin
from .models import FullArticle
from .models import ParagraphImage
from .models import ArticleParagraph
from .models import Article

admin.site.register(FullArticle)
admin.site.register(ArticleParagraph)
admin.site.register(ParagraphImage)
admin.site.register(Article)