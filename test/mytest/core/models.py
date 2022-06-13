from tabnanny import verbose
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager

# Create your models here.


class CustomUserManager(BaseUserManager):
    def _create_user(self, email, password, first_name, last_name, number, date_naissance, nature, **extra_fields):
        if not email:
            raise ValueError('email needed')
        if not password:
            raise ValueError('password needed')

        user = self.model(
            email = self.normalize_email(email),
            first_name = first_name,
            last_name = last_name,
            number = number,
            date_naissance = date_naissance,
            nature = nature,
            **extra_fields 
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, password, first_name, last_name, date_naissance, email, nature, number, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_active', True)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, first_name, last_name, number, date_naissance, nature, **extra_fields)
    
    def create_superuser(self, password, first_name, last_name, date_naissance, email, nature, number, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_active', True)
        extra_fields.setdefault('is_superuser', True)
        return self._create_user(email, password, first_name, last_name, number, date_naissance, nature, **extra_fields)
    

class User(AbstractBaseUser, PermissionsMixin):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100, unique=True)
    number = models.CharField(max_length=100)
    date_naissance = models.DateField()
    nature_choices = [('c','conducteur'), ('p', 'passager')]
    nature = models.CharField(max_length=1, choices=nature_choices, default='passager')
    rating = models.DecimalField(max_digits=2, decimal_places=1)
    raters = models.IntegerField(default=0)
    profile_pic = models.ImageField(null=True, blank=True)
    description = models.CharField(max_length=500, null=True, blank=True)

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)

    objects = CustomUserManager()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name','number', 'date_naissance', 'nature']


    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'




class MyUser(models.Model):

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100, unique=True)
    number = models.CharField(max_length=100)
    date_naissance = models.DateField()
    nature_choices = [('c','conducteur'), ('p', 'passager')]
    nature = models.CharField(max_length=1, choices=nature_choices, default='passager')
    password = models.CharField(max_length=100)
    # 4.9
    rating = models.DecimalField(max_digits=2, decimal_places=1, default=0.0)
    # 14 ratings
    raters = models.IntegerField(default=0)
    profile_pic = models.ImageField(null=True, blank=True, default="https://pngset.com/images/default-profile-picture-circle-symbol-logo-trademark-number-transparent-png-890174.png", upload_to='images/')
    description = models.CharField(max_length=500, null=True, blank=True)
    is_logged = models.BooleanField(default=False)













