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
