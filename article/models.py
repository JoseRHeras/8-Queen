from django.db import models
from blog.models import article
from PIL import Image

class FullArticle(models.Model):
    article_brief = models.ForeignKey(article, on_delete=models.CASCADE)
    article_title = models.CharField(max_length=70)
    lead_paragraph = models.TextField()
    ending_paragraph = models.TextField()
    
    def __str__(self):
        return f"{self.article_brief.title} Full Article"

    @property
    def paragraph_sorted_by_position(self):
        return self.articleparagraph_set.order_by('position_in_article')


class ArticleParagraph(models.Model):
    parent_article = models.ForeignKey(FullArticle, on_delete=models.CASCADE)
    position_in_article = models.IntegerField()
    paragraph_content = models.TextField()

    def __str__(self):
        return f"{self.parent_article.article_title} paragraph {self.position_in_article}"

    @property
    def number_of_images(self):
        return len(self.paragraphimage_set.all())

   

class ParagraphImage(models.Model):
    paragraph = models.ForeignKey(ArticleParagraph, on_delete=models.CASCADE)
    image = models.ImageField(default="paragraph_default.jpg",upload_to="paragraph_pic")
    alt_description = models.CharField(max_length=50, default='image')
    leading = models.BooleanField(default=False)

    def __str__(self):
        return f"Paragraph {self.paragraph.position_in_article} in article {self.paragraph.parent_article.article_title}"

    def save(self):
        super().save()
        
        img = Image.open(self.image.path)
        if img.height > 300 or img.width > 300:
            profile_size = (200, 200)
            img.thumbnail(profile_size)
            img.save(self.image.path)
    