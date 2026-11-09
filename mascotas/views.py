from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from mascotas.models import Responsable, Mascota
from mascotas.serializers import ResponsableSerializer, MascotaSerializer

# CRUD RESPONSABLE

@api_view(['POST', 'PUT'])
def crear_responsable(request):
    serializado = ResponsableSerializer(data=request.data)
    if serializado.is_valid():
        serializado.save()
        return Response(serializado.data, status=status.HTTP_201_CREATED)
    else:
        return Response(serializado.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def listar_responsable(request):
    responsables = Responsable.objects.all()
    serializado = ResponsableSerializer(responsables, many=True)
    return Response(serializado.data, status=status.HTTP_200_OK)

@api_view(['PATCH'])
def modificar_responsable(request, id):
    try:
        responsable = Responsable.objects.get(id=id)
    except Responsable.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
        
    serializado = ResponsableSerializer(responsable, data=request.data, partial=True)
    if serializado.is_valid():
        serializado.save()
        return Response(serializado.data, status=status.HTTP_200_OK)
    else:
        return Response(serializado.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def eliminar_responsable(request, id):
    try:
        responsable = Responsable.objects.get(id=id)
        responsable.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    except Responsable.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

# CRUD MASCOTA

@api_view(['POST', 'PUT'])
def crear_mascota(request):
    serializado = MascotaSerializer(data=request.data)
    if serializado.is_valid():
        serializado.save()
        return Response(serializado.data, status=status.HTTP_201_CREATED)
    else:
        return Response(serializado.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def listar_mascotas(request):
    mascotas = Mascota.objects.all()
    serializado = MascotaSerializer(mascotas, many=True)
    return Response(serializado.data, status=status.HTTP_200_OK)

@api_view(['PATCH'])
def modificar_mascota(request, id):
    try:
        mascota = Mascota.objects.get(id=id)
    except Mascota.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
        
    serializado = MascotaSerializer(mascota, data=request.data, partial=True)
    if serializado.is_valid():
        serializado.save()
        return Response(serializado.data, status=status.HTTP_200_OK)
    else:
        return Response(serializado.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def eliminar_mascota(request, id):
    try:
        mascota = Mascota.objects.get(id=id)
        mascota.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    except Mascota.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)