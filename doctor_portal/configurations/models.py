from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models
import uuid

class CustomUserManager(BaseUserManager):
    def create_user(self, name, mobile, usertype, password=None):
        if not name:
            raise ValueError('Users must have a name')
        if not mobile:
            raise ValueError('Users must have a mobile number')
        
        user = self.model(name=name, mobile=mobile, usertype=usertype)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, name, mobile, password=None):
        user = self.create_user(name, mobile, 'superadmin', password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user

class CustomUser(AbstractBaseUser, PermissionsMixin):
    USER_TYPE_CHOICES = [
        ('doctor', 'Doctor'),
        ('patient', 'Patient'),
        ('hospital', 'Hospital'),
        ('clinic', 'Clinic'),
        ('front_desk', 'Front Desk'),
        ('back_desk', 'Back Desk'),
        ('admin', 'Admin'),
        ('superadmin', 'Super Admin'),
    ]

    name = models.CharField(max_length=255)
    mobile = models.CharField(max_length=15, unique=True)
    usertype = models.CharField(max_length=20, choices=USER_TYPE_CHOICES)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    slug = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)  # UUID slug field
    is_verified = models.BooleanField(default=False)  # Verification status
    objects = CustomUserManager()

    USERNAME_FIELD = 'mobile'
    REQUIRED_FIELDS = ['name', 'usertype']

    def __str__(self):
        return self.name

class State(models.Model):
    name = models.CharField(max_length=255)
    status = models.CharField(max_length=5)

    def __str__(self):
        return self.name

class City(models.Model):
    name = models.CharField(max_length=255)
    states = models.ManyToManyField(State, related_name='cities')

    def __str__(self):
        return self.name

class Location(models.Model):
    name = models.CharField(max_length=255)
    cities = models.ManyToManyField(City, related_name='locations')

    def __str__(self):
        return self.name
    

class Services(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.name

class Specialization(models.Model):
    name = models.CharField(max_length=255)
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.name
    
class University(models.Model):
    name = models.CharField(max_length=255)
    state = models.ForeignKey(State, on_delete=models.DO_NOTHING, related_name='universities')
    city = models.ForeignKey(City, on_delete=models.DO_NOTHING, related_name='universities')
    pincode = models.CharField(max_length=6)
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.name

class college(models.Model):
    name = models.CharField(max_length=255)
    state = models.ForeignKey(State, on_delete=models.DO_NOTHING, related_name='colleges')
    city = models.ForeignKey(City, on_delete=models.DO_NOTHING, related_name='colleges')
    pincode = models.CharField(max_length=6)
    affiliation_type = models.CharField(max_length=255, choices=[('govt', 'Government'), ('private', 'Private'),('deemed', 'Deemed')])
    affliated_to = models.ForeignKey(University, on_delete=models.DO_NOTHING, related_name='colleges')
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.name
    
class degree(models.Model):
    name = models.CharField(max_length=255)
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.name

class Memberships(models.Model):
    name = models.CharField(max_length=255)
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.name
    
class Registration(models.Model):
    name = models.CharField(max_length=255)
    status = models.BooleanField(default=True)