from django.db import models

class Project(models.Model):
    name = models.CharField(max_length=50)
    icon = models.CharField(max_length=50)
    description = models.TextField()
    project_link = models.URLField()

    def __str__(self):
        return f"{self.name} project"

