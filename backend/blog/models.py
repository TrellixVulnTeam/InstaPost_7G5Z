from django.db import models
from datetime import datetime
from django.template.defaultfilters import slugify

# Create your models here.
class Categories(models.TextChoices):
  HOME = 'home'
  ABOUT = 'about'
  NEWS = 'news'
  SPORT = 'sport'
  TRAVEL = 'travel'
  CULTURE = 'culture'
  POLITICS = 'politics'
  LIFESTYLE ='lifestyle'
  HEALTH  = 'health'
  ENTERTAINMENT ='entertainment'
  FASHION = 'fashion'
  BOOKS = 'books'
  REVIEWS = 'reviews'
  CONTACTUS ='contactus'

class BlogPost(models.Model):
  title= models.CharField(max_length=50, default="New Post")
  slug = models.SlugField()
  category = models.CharField(max_length=50, choices=Categories.choices, default = Categories.HOME)
  thumbnail = models.ImageField(upload_to='photos/%Y/%m/%d/')
  excerpt = models.CharField(max_length=150)
  month = models.CharField(max_length = 3)
  day = models.CharField(max_length=2)
  content = models.TextField()
  featured = models.BooleanField(default=False)
  date_created = models.DateTimeField(default=datetime.now, blank=True)

  def __str__(self):
    return self.title
