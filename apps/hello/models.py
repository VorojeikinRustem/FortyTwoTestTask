
from django.db import models


class MyProfile(models.Model):
    
    name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    date_of_birth = models.DateField()
    email = models.EmailField()
    skype = models.CharField(max_length=50)
    bio = models.TextField()
    other_contacts = models.TextField()

    def full_name(self):
        return self.name + ' ' + self.last_name

    def __unicode__(self):
        return self.name + ' ' + self.last_name

        
class HttpRequests(models.Model):
    http_request = models.CharField(max_length=50)

    def __unicode__(self):
        return self.http_request