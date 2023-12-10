from django.db import models


# Create your models here.
class Menu(models.Model):
    name = models.CharField(max_length=255)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='child')
    url = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.name
