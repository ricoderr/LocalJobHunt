from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin, Group, Permission
from django.core.validators import RegexValidator


'''CustomUserManager for the custom user we are creating below'''

class CustomUserManager(BaseUserManager): 
    
    def create_user(self, Fname:str, Lname:str, phone_number:str,  email: str = None, password: str = None, **extra_fields):
        if email:
            email = self.normalize_email(email)
        user = self.model(Fname=Fname, Lname= Lname, phone_number=phone_number, email=email, **extra_fields)
        if password:
            user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, Fname:str, Lname:str, phone_number:str,  email: str = None, password: str = None, **extra_fields): 
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user( Fname=Fname, Lname=Lname, phone_number=phone_number, email=email, password=password, **extra_fields)
        
        
'''CustomUser Model'''
        
PHONE_VALIDATOR = RegexValidator(regex=r"^\+?\d{10-15}$", message="The number must be of 10-15 digits, with optional + at start!")
class CustomUser(AbstractBaseUser, PermissionsMixin): 
    
    Fname = models.CharField(max_length=225)
    Lname = models.CharField(max_length=225)
    username = models.CharField(max_length=225, null=True)
    email = models.EmailField(max_length=225, blank=True, null=True, unique=True)
    phone_number = models.CharField( max_length=15,unique=True, validators=[PHONE_VALIDATOR])
    profile_picture = models.ImageField(upload_to='profiles/', blank=True, null=True)
    resume = models.FileField(upload_to='resumes/', blank=True, null=True)
    
    
    skills = models.TextField(blank=True, null=True)
    
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    date_joined = models.DateTimeField(auto_now_add=True)
    
    groups = models.ManyToManyField(
        Group, 
        related_name="customuser_set", 
        blank=True
    )
    
    user_permissions = models.ManyToManyField(
        Permission, 
        related_name="customuser_permissions_set", 
        blank=True, 
    )
    
    objects = CustomUserManager()
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['phone_number', 'Fname', "Lname"]
    
    def __str__(self): 
        return f"{self.Fname} {self.Lname}"
