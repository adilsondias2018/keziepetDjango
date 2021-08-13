from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Animal, Characteristic, Group
from .serializers import (AnimalSerializer, CharacteristicSerializer,
                          GroupSerializer)

# Create your views here.

class AnimalView(APIView):

    def post(self, request):

        serializer = AnimalSerializer(data=request.data)
        
        if not serializer.is_valid():

            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        group = serializer.validated_data.pop('group') 
        characteristics = serializer.validated_data.pop('characteristics')



        group1 = Group.objects.get_or_create(**group)[0]


        animal = Animal.objects.create(**serializer.validated_data, group=group1)
        
        

        for ch in characteristics:

            characteristic = Characteristic.objects.get_or_create(**ch)[0]
            animal.characteristics.add(characteristic)
        
        serializer = AnimalSerializer(animal)

        return Response(serializer.data, status=status.HTTP_201_CREATED)


    def get(self, request, animal_id):

        if animal_id:
            try:
                animal = Animal.objects.get(id=animal_id)
            except ObjectDoesNotExist:
                
                return Response(status=status.HTTP_404_NOT_FOUND)
            
            serializer = AnimalSerializer(animal)

            return Response(serializer.data)    
            

        queryset = Animal.objects.all()

        serializer = AnimalSerializer(queryset, many=True)

        # print(serializer)

        return Response(serializer.data)    
        
    def delete(self, request, animal_id):

        try:
            animal = Animal.objects.get(id=animal_id)
        except ObjectDoesNotExist:
            return Response({"message": "Animal doesn't exist"},status=status.HTTP_404_NOT_FOUND)

        animal.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)







