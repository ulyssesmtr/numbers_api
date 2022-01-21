from django.db import models

class Number(models.Model):
    number = models.JSONField()
