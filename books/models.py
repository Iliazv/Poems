import datetime
from django.db import models
from django.utils import timezone

class Poet(models.Model):
    name = models.CharField(max_length = 30)
    lastname = models.CharField(max_length = 30)
    url = models.CharField(max_length = 250, default = '')
    century = models.CharField(max_length=100, default = '')
    photo = models.ImageField(upload_to = 'authors_images/', blank = True)

    def __str__(self):
        return self.name + ' ' + self.lastname
    
class Poem(models.Model):
    connect_question = models.ForeignKey(Poet, on_delete=models.CASCADE)   
    poem_name = models.CharField(max_length = 50, default = '')
    poem_text = models.TextField(max_length = 2000, default = '')
    rating = models.IntegerField(default = 0)
    votes = models.IntegerField(default = 0)
    rank = models.FloatField(default = 0)
    old = models.BooleanField(default = True)
    
    def __str__(self):
        return self.poem_name
    
class Comment(models.Model):
    connect_question = models.ForeignKey(Poem, on_delete=models.CASCADE)
    name_author = models.CharField(max_length = 50)
    comment = models.TextField(max_length = 600)
    date = models.DateTimeField('Date published')
    
    def __str__(self):
        return self.name_author
    
    def new_comment(self):
        return self.date + datetime.timedelta(days = 7) > timezone.now() and self.date < timezone.now()