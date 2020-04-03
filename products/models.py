from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Products(models.Model):
    title = models.CharField(max_length=256)
    url = models.URLField()
    published_date = models.DateTimeField()
    total_votes = models.IntegerField(default=1)
    image = models.ImageField(upload_to='images/')
    icon = models.ImageField(upload_to='images/')
    body = models.TextField()
    hunter = models.ForeignKey(User, on_delete=models.CASCADE)


    def pub_date_pretty(self):
        return self.published_date.strftime("%b %e, %Y")

    def __str__(self):
        return self.title
    
    def summary(self):
        return self.body[:350]

   