from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
# from .managers import CustomUserManager
from django.conf import settings

from django.contrib.auth.base_user import BaseUserManager
from django.utils.translation import gettext_lazy as _
from django.utils import timezone


class CustomUserManager(BaseUserManager):
    """
    Custom user model manager where email is the unique identifiers
    for authentication instead of usernames.
    """
    def create_user(self, email, password=None, **extra_fields):
        """
        Create and save a user with the given email and password.
        """
        if not email:
            raise ValueError("Users must have an Email address")
        # if not username :
        #     raise ValueError("Users must have an Username")
        user = self.model(
            email=self.normalize_email(email),
        )

        if extra_fields.get('name'):
            user.name = extra_fields.get('name')

        if extra_fields.get('mobile_number'):
            user.mobile_number = extra_fields.get('mobile_number')

        if extra_fields.get('image'):
            user.image = extra_fields.get('image')

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        user = self.create_user(
            email=self.normalize_email(email),
            password=password,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser, PermissionsMixin):
    name = models.CharField(max_length=100, null=True)
    email = models.EmailField(max_length=100, null=False, unique=True)
    password = models.CharField(max_length=100, null=False)
    mobile_number = models.CharField(max_length=15, null=True)
    image = models.ImageField(upload_to='profile', null=True)

    is_staff = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    date_joined = models.DateTimeField(default=timezone.now)

    objects = CustomUserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ['name']

    def __str__(self):
        return self.email

    def get_full_name(self):
        return f'{self.name}'

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin

