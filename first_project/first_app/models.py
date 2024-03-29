from django.db import models
from django.contrib.auth.models import User
# SuperUserInformation
# User: Jose
# Email: training@pieriandata.com
# Password: testpassword

# CREATE SOME TEST DATA WITH SOME SHELL COMMANDS:

# python manage.py shell

# from first_app.models import Topic
# print(Topic.objects.all())
# t = Topic(top_name="Social Network")
# t.save()
# print(Topic.objects.all())
# quit()

# Create your models here.
# class Topic(models.Model):
#     top_name = models.CharField(max_length=264,unique=True)

#     def __str__(self):
#         return self.top_name

# class Webpage(models.Model):
#     topic = models.ForeignKey(Topic,on_delete=models.CASCADE)
#     name = models.CharField(max_length=264,unique=True)
#     url = models.URLField(unique=True)

#     def __str__(self):
#         return self.name

# class AccessRecord(models.Model):
#     name = models.ForeignKey(Webpage,on_delete=models.CASCADE)
#     date = models.DateField()

#     def __str__(self):
#         return str(self.date)

class UserProfileInfo(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    #class object attributes to be added

    portfolio = models.URLField(blank=True)
    profile_pic = models.ImageField(upload_to='profile_pics',blank=True)

    def __str__(self):
        return self.user.username
