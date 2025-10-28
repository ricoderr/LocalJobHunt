from django.contrib.auth.backends import ModelBackend
from django.contrib.auth import get_user_model

''' 
django by default users 'usename' and 'password' to authenticate, 
    # So, It is overwritten below in a way that authenticate() method will use email
    # But, we need to pass username as email while using 
    # example : authenticate(username=rijang@gmail.com, password=******)
                                                  -Rijan
'''
class EmailBackend(ModelBackend): 
    def authenticate(self, request, username = None, password = None, **kwargs):
        User = get_user_model()
        try: 
            user = User.objects.get(email=username)
            return user 
        except User.DoesNotExist: 
            return None