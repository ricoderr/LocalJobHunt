from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin, Group, Permission


'''CustomUserManager for the custom user we are creating below'''
class CustomUserManager(BaseUserManager): 
    
    def create_user(self, username: str, email: str, password: str, **extra_fields):
        if not email: 
            raise ValueError("Email required to login")
        
        email = self.normalize_email()
        user = self.model(username=username, email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self, username: str, email:str, password: str, **extra_fields): 
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        self.create_user(username=username, email=email, password=password, **extra_fields)
        
        
        
'''CustomUser Model'''
        
class CustomeUser(AbstractBaseUser, PermissionsMixin): 
    
    email = models.CharField(max_length=225, unique=True)
    username = models.CharField(max_length=225)
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
    REQUIRED_FIELDS = ['username']
    
    def __str__(self): 
        return self.username