from django.db import models
import uuid
# Create your models here.


class Zigbee(models.Model):
    uuid = models.UUIDField(default=uuid.uuid1(), blank=True, null=True)
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


class ZigbeeAction(models.Model):
    zigbee = models.ForeignKey(Zigbee, on_delete=models.CASCADE)
    zigbee_state = models.ForeignKey(ZigbeeState, on_delete=models.CASCADE)
    action = models.CharField(max_length=50)
    newstate = models.CharField(max_length=50)
    ctime = models.DateTimeField(auto_now=True, auto_created=True)
    mtime = models.DateTimeField(auto_now=True, auto_created=True)
    done = models.BooleanField(default=False)

    def __str__(self):
        return "%s: %s %s" % (self.action,
                              self.newstate,
                              self.done)


