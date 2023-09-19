from django.db import models

# Create your models here.

class Dest(models.Model):
    iframe = models.CharField(max_length=600)
    dest_name = models.CharField(max_length=256)
    # created_at = models.DateTimeField(auto_now_add=True)


# class Dest(models.Model):
    # iframe = models.CharField(max_length=600)
    # facility_name = models.CharField(max_length=256)
    # open_hour = models.DateTimeField()
    # close_hour = models.DateTimeField()
    # created_at = models.DateTimeField(auto_now_add=True)
    # last_entry_time = models.DateTimeField(null=True, blank=True)