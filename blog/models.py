from django.db import models

# Create your models here.
class Blog_Project(models.Model):
    title = models.CharField(max_length = 200)
    description = models.TextField()
    image = models.ImageField(upload_to = 'blog/images/')
    date = models.DateField()

    def __str__(self):
        return self.title
