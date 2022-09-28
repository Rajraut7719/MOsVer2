from dataclasses import fields
from pyexpat import model
from rest_framework import serializers
from .models import TranSum



class TranSumSerializer(serializers.ModelSerializer):
    class Meta:
        model=TranSum
        fields='__all__'

    # def validate(self, attrs):
    #     purch=attrs.get('purchaseDate')
    #     print(purch)
    #     option=attrs.get('option')
    #     print(option)
    #     fy=attrs.get('fy')
    #     print(fy)
    #     if option=='O':
    #         if purch <'2022-04-01':
    #             raise serializers.ValidationErr("Show Opening")
            
    #     if option=='A':
    #         if purch >'2023-03-31':
    #             raise serializers.ValidationError("Show Addtion")
    #     print(attrs)
    #     return attrs





