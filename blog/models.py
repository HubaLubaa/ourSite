from django.conf import settings
from django.db import models
from django.utils import timezone
from django.core.validators import * 

telephone = RegexValidator(r'^\d+$', 'Only numeric characters are allowed.')

class Registration(models.Model):
      mobile_telephone = models.PositiveIntegerField(max_length=18, validators=[telephone, MaxLengthValidator])


class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
