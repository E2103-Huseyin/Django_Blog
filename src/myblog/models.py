from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100)
    
    class Meta:
        verbose_name_plural = "Categories" #admin panelinde class ismininin doğru yazımı için kod yazdık
    def __str__(self): 
        return self.name  #admin panelinde objelerin isim listesi olarakgözükmesiiçin kod yazdık
    

class Post(models.Model):
    OPTIONS = (
        ('d', 'Draft'),
        ('p', 'Published')
    )
    title = models.CharField(max_length=100)
    content = models.TextField()
    image = models.ImageField()
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    publish_date = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.CharField(max_length=10, choices=OPTIONS, default='d')
    slug = models.SlugField(blank=True)
    def __str__(self): 
        return self.name  #admin panelinde objelerin isim listesi olarakgözükmesiiçin kod yazdık
    
    

    