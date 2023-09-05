from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, UserManager


class CustomUserManager(UserManager):

    def create_user(self, email, password, **extra_fields):
    
        if not email:
            raise ValueError("You must set the email")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, **extra_fields):
     
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_active", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True")
        return self.create_user(email, password, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):

  username = models.CharField("Username", max_length=50, unique=True)
  first_name = models.CharField("First name", max_length=50)
  last_name = models.CharField("Last name", max_length=50)
  email = models.EmailField("Email", unique=True)
  update_time = models.DateTimeField("Update time", auto_now=True)

  is_active = models.BooleanField("Active", default=True)
  is_superuser = models.BooleanField("Superuser", default=False)
  is_staff = models.BooleanField(default=False)

  USERNAME_FIELD = "email"

  objects = CustomUserManager()

  
  class Meta:
    verbose_name = "User"
    verbose_name_plural = "Users"
