from django.db import models

# Create your models here.

class Events(models.Model):
    imageTop=models.ImageField(upload_to='images/events/imageTop',blank=True, null=True)
    title=models.CharField(primary_key=True,max_length=255)
    description=models.TextField()
    date=models.DateField(help_text = "Please use the following format: <em>YYYY-MM-DD</em>.")
    details=models.TextField()


class EventImages(models.Model):
    title=models.ForeignKey(Events,on_delete=models.CASCADE,related_name="moreImages")
    moreImages = models.ImageField(upload_to='images/events/moreImages',blank=True, null=True)


