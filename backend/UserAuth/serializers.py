from rest_framework import serializers
from django.contrib.auth import get_user_model


User = get_user_model()

class SignupSerializer(serializers.ModelSerializer): 
    
    class Meta: 
        model = User
        fields = ["Fname", "Lname", "email", "phone_number", "password"]
        extra_kwargs = {"password": {"write_only": True}}
    
    def create(self, validated_data): 
        
        user = User.objects.create_user(
            Fname = validated_data['Fname'],
            Lname = validated_data['Lname'],
            email = validated_data.get('email'),  # .get() returns None if no value is there!
            password = validated_data['password'],
            password = validated_data['password'],
        )
        
        return user
    

class LoginSerializer(serializers.Serializer): 
    
    identifier = serializers.CharField()
    password = serializers.CharField(write_only=True)
    
    def validate(self, attrs):
        identifier = attrs.get("identifier")
        password = attrs.get("password")
        
        if not identifier or not password: 
            raise ValueError("Identifier and password both are required!")
        
        if '@' in identifier:                                         # checks whether the identifier is email or ph_number
            user = User.objects.filter(email=identifier).first()
        else: 
            user = User.objects.filter(phone_number = identifier).first()
        
        if not user:                                                  # checks if the user with these cred.. exists or not.
            raise serializers.ValidationError("User doesn't exists with these credentials!")

        if not user.check_password(password):                         # checks the password
            raise serializers.ValidationError("Incorrect password.")
        
        attrs['user'] = user        # includes user key in attrs if the user is validated
        return attrs                # returns the attrs to send back to the client. 