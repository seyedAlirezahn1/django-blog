from django.db import models

# Create your models here.

class Products(models.Model):
    title = models.CharField(max_length=150)
    image = models.FileField(upload_to="products/", null=True, blank=True)
    file = models.FileField(upload_to="products/", null=True, blank=True)
    text_blog = models.TextField()

    def __str__(self):
        return self.title
