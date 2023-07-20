from django.db import models
import uuid
from ckeditor_uploader.fields import RichTextUploadingField

# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=200)
    thumbnail = models.ImageField(null=True)
    body = RichTextUploadingField()
    slug = models.SlugField(null=True,blank=True)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4,unique=True,primary_key=True,editable=False)

    def __str__(self):
        return self.title
    
class Skill(models.Model):
    title = models.CharField(max_length=200,null=True)
    body = models.TextField(null=True,blank=True)
    logo = models.ImageField(null=True)
    created = models.DateTimeField(auto_now_add=True)
    

    def __str__(self):
        return self.title
    
class Tag(models.Model):
    name = models.CharField(max_length=200,null=True)
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name  
    
class Message(models.Model):
    name = models.CharField(max_length=250,null=True)
    email = models.EmailField(max_length=254,null=True)
    subject = models.CharField(max_length=250,null=True)
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)
    id = models.UUIDField(default=uuid.uuid4,unique=True,primary_key=True,editable=False)

    def __str__(self):
        return self.name
    
class Endorsement(models.Model):
    name = models.CharField(max_length=200,null=True,blank=True)
    body = models.TextField()
    approved = models.BooleanField(default=False,null=True)
    featured = models.BooleanField(default=False)

    def __str__(self):
        return self.body[0:50]
    
class Comment(models.Model):
    project = models.ForeignKey(Project,on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    body = models.TextField(null=True,blank=True)
    created = models.DateTimeField(auto_now_add=True,null=True)

    def __str__(self):
        return self.body[0:60]
    
class Coffee(models.Model):
    name = models.CharField(max_length=100)
    amount = models.CharField(max_length=50)
    order_id = models.CharField(max_length=100,blank=True)
    razorpay_payment_id = models.CharField(max_length=100,blank=True)
    paid = models.BooleanField(default=False)

class Question(models.Model):
    TYPES = (
        ('backend','backend'),
        ('frontend','frontend'),
        ('fullstack','fullstack')
    )

    answer = models.CharField(max_length=100,choices=TYPES)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4,unique=True,primary_key=True,editable=False)

    def __str__(self):
        return self.answer