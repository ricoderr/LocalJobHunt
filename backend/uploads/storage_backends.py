from django.core.files.storage import Storage 
from webdav3.client import Client
from django.conf import settings 
import os 

class KoofrStorage(Storage): 
    def __init__(self): 
        options = {
             'webdav_hostname': settings.KOFR_HOST,
            'webdav_login': settings.KOFR_USER,
            'webdav_password': settings.KOFR_PASSWORD,
        }
        self.client = Client(options)
    
    def _save(self, name, content): 
        folder = '/resumes'
        
        if folder != '' and not self.client.check(folder): 
            self.client.mkdir(folder)
            
        self.client.upload_sync(remote_path=f'{folder}/{name}', local_path_or_file=content.file)
        return name

    def exists(self, name):
        return self.client.check(f'/{name}')

    def url(self, name):
        # Koofr files are private by default
        return f"{settings.KOFR_HOST}/{name}"

    def delete(self, name):
        if self.client.check(f'/{name}'):
            self.client.clean(f'/{name}')
