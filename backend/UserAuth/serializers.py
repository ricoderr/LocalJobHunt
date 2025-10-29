from rest_framework import serializers

class SignupSerializer(serializers.Serializer): 
    
    class Meta: 
        model = U