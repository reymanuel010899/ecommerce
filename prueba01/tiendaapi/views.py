from django.shortcuts import render
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView, UpdateAPIView
from inicio.models import electronicomodel,categoria
from .serializers import serialisarmodelo, categoriaserial, paginacion, crearserializar, actualizar
from rest_framework.viewsets import ViewSet
from rest_framework.authtoken.models import Token
from rest_framework.views import APIView
# Create your views here.


class listarapiview(ListAPIView):
    serializer_class = serialisarmodelo
    pagination_class = paginacion

    def get_queryset(self):
        return electronicomodel.objects.all()
    

class listarcategoriaapiview(ListAPIView):
    serializer_class =    categoriaserial

    def get_queryset(self):
        return categoria.objects.all()
    
class crearapiview(CreateAPIView):
    serializer_class = crearserializar

class detalleapis(RetrieveAPIView):
    serializer_class = actualizar
    queryset = electronicomodel

class  updateapis(UpdateAPIView):
    serializer_class = actualizar
    queryset = electronicomodel


class grudview(ViewSet):
    serializer_class = crearserializar
    queryset = electronicomodel.objects.all()



from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework import status
from rest_framework.response import Response
#para que un usuario solo pueda estar activo en una sola secion
from django.contrib.sessions.models import Session
import datetime
class login(ObtainAuthToken):

    
    def post(self, request, *args, **kwargs):
         
        login_serializer = self.serializer_class(data=request.data, context={'request':request})
        if login_serializer.is_valid():
            user = login_serializer.validated_data['user']
            if user.is_activo:
                user_serializado = self.serialazer_class(user)
                obt , creado = Token.objects.get_or_create(user=user)
                if creado:
                    return Response({'token':obt.key,
                                     'user':user_serializado.data}, status=status.HTTP_200_OK)
                else:
                    #aqui me esta validando si hay mas seciines abiertas , si hay seciones me la cierra
                    all_secion = Session.objects.filter(expire_date__gte=datetime.now())
                    if all_secion.exists():
                        for secion in all_secion:
                            secion_data = secion.decoded()
                            if user.id == int(secion_data.get('_auth_user_id')):
                                secion.delete()

                    obt.delete()
                    token=Token.objects.create(user=user)
                    return Response({'token':token.key,
                                     'user':user_serializado.data}, status=status.HTTP_200_OK)

class logaut(APIView):
    
    def get(self, request, *arg, **kwargs):
        try:
            token = self.request.get('token')
            token = Token.object.filter(user=user).first()
            if token:
                user = token.user
                all_secion = Session.objects.filter(expire_date__gte=datetime.now())
                if all_secion.exists():
                    for secion in all_secion:
                        data = secion.get_decoded()
                        if user.id == int(data.get('_auth_id_user')):
                            secion.delete()
                secion_message = 'seciones eliminadas'
                token.delete()
                token_message = 'token eliminado'
                return Response({'secion_message':secion_message, 'token_message':token_message}, status=status.HTTP_200_OK)
        except:
            return Response({'error':'no existe un usuario con estas credenciales'}, status=status.HTTP_400_BAD_REQUEST)




                

class login(ObtainAuthToken):
    def get(self, request, *args, **kwargs):
        login_serializer = self.serializer_class(data=request.data, context={'request':request})
        if login_serializer.is_valid():
            user = login_serializer.validated_data['user']
            if user.is_active():
                user_serializado = self.serialisando_usuario(user)
                obj, created=Token.objects.get_or_create(user=user)
                if created:
                    return Response({'token':obj.key, 'user':user_serializado, 'mensaje':'usuario creado sastifactoriamente'}, status=status.HTTP_200_OK)
                else:
                    all_secion = Session.objects.filter(expire_date__gte=datetime.now())
                    if all_secion.exists():
                        for secion in all_secion:
                            data = secion.get_decoded()
                            if user.id == int(data.get('_auth_id_user')):
                                secion.delete()

                    obj.delete()
                    token = Token.objects.create(user=user)
                    return Response({'token':token.key, 'user':user_serializado, 'message':'usuario aunteticado correctamente'}, status=status.HTTP_200_OK)








'''rest framework'''
from .serializers import categoriarserializar, actualizar, user_sserialiser,  caroo_serializer
from rest_framework.views import APIView
from inicio.models import categoria
from .funciones import venta_funcion
from inicio.models import electronicomodel
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from carro_compra.models import carro_compras

class listar_view(APIView):
    serializer_class = categoriarserializar

    def get(self, request):
        lista = categoria.objects.all()
        serialiser = self.serializer_class(lista, many=True)        
        return Response(serialiser.data)
    


    def post(self, request):

        serialiser = self.serializer_class(data=request.data)
        if serialiser.is_valid():
            senta = venta_funcion(self, serialiser)
            venta =  user_sserialiser(senta)
            serialiser.save()
            return Response(venta)
    

class creat_producto_carro(ListAPIView):
    # authentication_classes = (TokenAuthentication,)
    # permission_classes = [IsAuthenticated]
    serializer_class = caroo_serializer

    def get_queryset(self):
        return carro_compras.objects.all()