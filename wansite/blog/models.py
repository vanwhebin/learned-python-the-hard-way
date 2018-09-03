# -*- coding=utf-8 -*-
from django.db import models

# Create your models here.
from django.utils import timezone

class Post(models.Model):
    # redirect to an other model
    author = models.ForeignKey("auth.User", on_delete=models.CASCADE) 
    # define text with limited characters
    title= models.CharField(max_length=200)
    # define text with no limited characters
    text = models.TextField()
    # define date time 
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)


    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

