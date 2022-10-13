from django.db import models

# Create your models here.

class Collection(models.Model):
    form_title = models.TextField(null=True)
    form_body = models.TextField(null=True)
