from django.db import models
from django.contrib.auth.models import User
# Create your models here.


# blog model
class Blog(models.Model):

    title = models.CharField(max_length=200)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    content = models.TextField()
    see = models.IntegerField(default=0)

    def __str__(self):
        return "%s" % self.title
