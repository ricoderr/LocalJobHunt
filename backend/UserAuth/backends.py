from django.contrib.auth.backends import ModelBackend
from django.contrib.auth import get_user_model

''' 
django by default users 'usename' and 'password' to authenticate, 
    # So, It is overwritten below in a way that authenticate() method will use email
    # But, we need to pass username as email while using 
    # example : authenticate(username=rijang@gmail.com, password=******)
                                                  -Rijan
'''
class PhoneBackend(ModelBackend): 
    def authenticate(self, request, username = None, password = None, **kwargs):
        User = get_user_model()
        try: 
            if User.check_password(password): 
                user = User.objects.get(phone_number=username)
                return user 
            return None
        except User.DoesNotExist: 
            return None