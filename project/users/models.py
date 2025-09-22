
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.utils import timezone
from serviceCategory.models import ServiceCategory


class UserManager(BaseUserManager):
    def create_user(self, email, phone, password=None, **extra_fields):
        if not email:
            raise ValueError("Email is required")
        if not phone:
            raise ValueError("Phone is required")

        email = self.normalize_email(email)
        user = self.model(email=email, phone=phone, **extra_fields)
        user.set_password(password)   # Hash password
        user.save(using=self._db)
        return user

    def create_superuser(self, email, phone, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        return self.create_user(email, phone, password, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    class Role(models.TextChoices):
        CUSTOMER = 'customer', 'Customer'
        WORKER = 'worker', 'Worker'

    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15, unique=True)
    
    role = models.CharField(max_length=20, choices=Role.choices, default=Role.CUSTOMER)
    # worker filed 
    skills = models.TextField(blank=True, null=True)
    serviceCategory = models.ForeignKey(
        ServiceCategory,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )
    rate = models.DecimalField(max_digits=10,
        decimal_places=2,
        default=0.00 )
    experience = models.PositiveIntegerField(null=True, blank=True)   
    availability = models.BooleanField(default=True)
    
    created_at = models.DateTimeField(default=timezone.now)
    update_at = models.DateTimeField(auto_now=True)

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    city = models.CharField(max_length=100 , default="unknow")

    objects = UserManager()

    USERNAME_FIELD = "email"  
    REQUIRED_FIELDS = ["phone", "name"]

    def __str__(self):
        return self.email 