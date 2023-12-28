from django.db import models


class MyFile(models.Model):
    image_name = models.CharField(max_length=100, default="image")
    image_url = models.ImageField(blank=True, null=True, upload_to="img/")

    def __str__(self):
        return self.image_name
