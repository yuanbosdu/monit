from django.db import models
from django.contrib.auth.models import User

# Create your models here.


# model company
class Company(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    phone = models.CharField(max_length=50)
    email = models.CharField(max_length=50, blank=True, null=True)
    admin = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    extra = models.TextField(null=True, blank=True)
    ctime = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "%s" % self.name


# model device
class Device(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    address = models.CharField(max_length=50)
    longitude = models.CharField(max_length=10, blank=True, null=True)
    latitude = models.CharField(max_length=10, blank=True, null=True)
    dtype = models.CharField(max_length=50)
    dprotocol = models.CharField(max_length=50)
    dtype_uuid = models.CharField(max_length=50)  # this is uuid of dtype
    ctime = models.DateTimeField(models.DateTimeField, auto_now=True)

    company = models.ForeignKey(Company, on_delete=models.SET_NULL, default=None, null=True)

    def __str__(self):
        return "%s" % self.name


# model user property
class UserInfo(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    company = models.ForeignKey(Company, on_delete=models.CASCADE, null=True, blank=True)
    phone = models.CharField(max_length=50)
    permission = models.CharField(max_length=200)   # simple permission management

    def __str__(self):
        return "%s" % self.permission


# secret key management
class SecretKey(models.Model):
    AES = models.CharField(max_length=16, blank=True, null=True)
    RSA_Public = models.CharField(max_length=128, blank=True, null=True)
    RSA_Private = models.CharField(max_length=128, blank=True, null=True)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    mtime = models.DateTimeField(auto_now=True)  # modify time

    def __str__(self):
        return "%s" % self.AES
