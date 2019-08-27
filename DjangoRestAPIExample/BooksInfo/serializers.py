from rest_framework import serializers
from .models import books   #import model
 
# Create a class
class booksSerializer(serializers.ModelSerializer):
 
    class Meta:
        model = books
        fields = '__all__'