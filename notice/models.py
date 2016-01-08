from django.db import models
from django.utils import timezone


class Post(models.Model):
    author_notice = models.CharField(max_length=200, blank = True, null = True)
    title_notice = models.CharField(max_length=200, blank = True, null = True)
    text_notice = models.TextField(blank = True, null = True)
    created_date_notice = models.DateTimeField(
            blank = True, null = True)
    

    author_highlights = models.CharField(max_length=200 , blank = True, null = True)
    title_highlights = models.CharField(max_length=200, blank = True, null = True)
    text_highlights = models.TextField(blank = True, null = True)
   
            

    author_announcement = models.CharField(max_length=200, blank = True, null = True)
    title_announcement = models.CharField(max_length=200, blank = True, null = True)
    text_announcement = models.TextField(blank = True, null = True)
    created_date_announcement = models.DateTimeField(
            blank = True, null = True)

    author_events = models.CharField(max_length=200, blank = True, null = True)
    title_events = models.CharField(max_length=200, blank = True, null = True)
    text_events = models.TextField(blank = True, null = True)
    created_date_events = models.DateTimeField(
            blank = True)

    slide_image1 = models.ImageField(upload_to='images', blank=True, null = True)
    slide_image2 = models.ImageField(upload_to='images', blank=True, null = True)
    slide_image3 = models.ImageField(upload_to='images', blank=True, null = True)

    event_title = models.CharField(max_length=200, blank = True, null = True)
    event_text = models.CharField(max_length=200, blank = True, null = True)
    event_image = models.ImageField(upload_to='images', blank=True, null = True)

    vision_text = models.CharField(max_length=200, blank = True, null = True)
    vision_author = models.CharField(max_length=200, blank = True, null = True)

    gallery_image =  models.ImageField(upload_to='images', blank=True , null = True)


    


