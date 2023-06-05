from rest_framework import serializers
from .models import *

class TemplateSerializers(serializers.ModelSerializer):
    class meta:
        model = Template
        fields = '__all__'
        