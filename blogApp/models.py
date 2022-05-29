from django.db import models

# Create your models here.
class BlogPost(models.Model):
    title = models.CharField(max_length=150)
    slug = models.CharField(max_length=150,primary_key=True)
    content = models.TextField()
    publishAt = models.DateTimeField()
    updatedAt = models.DateTimeField(auto_now=True)
    createdAt = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title + self.slug
