from django.db import models

# Create your models here.


class Zigbee(models.Model):
    name = models.CharField(max_length=50)
    english = models.CharField(max_length=50, null=True, blank=True)
    desc = models.TextField(blank=True, null=True)
    address = models.CharField(max_length=50, blank=True, null=True)
    ctime = models.DateTimeField(auto_now=True)
    mtime = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "%s %s" % (self.name, self.mtime)


class ZigbeeState(models.Model):
    zigbee = models.ForeignKey(Zigbee, on_delete=models.CASCADE, related_name='state')
    state = models.CharField(max_length=50, default="normal")
    utime = models.DateTimeField(auto_now=True, auto_created=True)

    def __str__(self):
        return "%s %s %s" % (self.zigbee.name, self.state, self.utime)
