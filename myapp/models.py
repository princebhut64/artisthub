from django.db import models

# Create your models here.
class User(models.Model):
    fname =models.CharField(max_length = 20)
    lname = models.CharField(max_length = 20)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length = 20)
    contactno = models.CharField(max_length = 20)
    status = models.CharField(max_length = 20, default="inactive")
    role = models.CharField(max_length = 30, default="user")

    def __str__(self):
        return self.email+" - "+self.role

class Artist(models.Model):
    user_id = models.ForeignKey(User,on_delete=models.CASCADE)
    address = models.CharField(max_length = 50)
    city = models.CharField(max_length = 20)
    postcode = models.IntegerField(default = 00000)
    State = models.CharField(max_length = 20)
    country = models.CharField(max_length = 20,blank=True)
    fax = models.CharField(max_length = 30)
    description = models.TextField(max_length = 700)
    profile_pic=models.FileField(upload_to="images/",blank=True,default="avtar.png",null=True)   

    def __str__(self):
        return self.city+"-"+self.country

class Events(models.Model):
    title = models.CharField(max_length = 20)
    description = models.TextField(max_length = 700)
    event_pic=models.FileField(upload_to="images/",blank=True,null=True)   
    address = models.CharField(max_length = 50)
    created_at = models.CharField(max_length = 20)

    def __str__(self):
        return self.title

class Contact(models.Model):
    fullname =  models.CharField(max_length = 30)
    contactno =  models.CharField(max_length = 15)
    email =  models.EmailField(unique=True)
    message = models.TextField(max_length=600, blank=True)
    subject =  models.CharField(max_length = 50)
    
    def __str__(self):
        return self.fullname+"-"+self.subject

class Team(models.Model):
    name = models.CharField(max_length = 30)
    category = models.CharField(max_length = 20)
    description = models.TextField(max_length = 700)
    photos=models.FileField(upload_to="images/",blank=True,null=True)   

    def __str__(self):
        return self.name

class BookArtist(models.Model):
    
    user_id = models.ForeignKey(User,on_delete=models.CASCADE)
    artist_id = models.ForeignKey(Artist,on_delete=models.CASCADE,null=True)
    is_verified = models.BooleanField(default = False,null=True)
    event_name =  models.CharField(max_length = 50)
    budget =  models.IntegerField(max_length = 15)
    address = models.CharField(max_length = 50)
    city = models.CharField(max_length = 25)
    event_date = models.DateTimeField(blank = False)
    description = models.TextField(max_length = 700)
    def __str__(self):
        return self.event_name


class Newsletter(models.Model):
    email = models.EmailField(unique=True)