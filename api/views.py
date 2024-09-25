from django.shortcuts import render

# Create your views here.

from rest_framework.views import APIView
from rest_framework.response import Response
from api.models import Cosmetics
from api.serializers import ProductSerializer,ProductModelSerializer,UserSerializer

from rest_framework.viewsets import ViewSet,ModelViewSet
from rest_framework.decorators import action
from django.contrib.auth.models import User
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated


class ProductView(APIView):
    def get(self,request,*args,**kw):
        qs=Cosmetics.objects.all()
        serializer=ProductSerializer(qs,many=True)
        return Response(data=serializer.data)
    
    def post(self,request,*args,**kw):
        serializer=ProductSerializer(data=request.data)
        if serializer.is_valid():
            print(serializer.validated_data)
            Cosmetics.objects.create(**serializer.validated_data)
            return Response(data=serializer.data)
        else:
            return Response(data=serializer.errors)
    
        

class ProductDetailView(APIView):
    def get(self,request,*args,**kw):

        print(kw)
        id=kw.get('id')
        qs=Cosmetics.objects.get(id=id)
        serializer=ProductSerializer(qs)
        return Response(data=serializer.data)
    

    def put(self,request,*args,**kw):
        
        serializer=ProductSerializer(data=request.data)

        if serializer.is_valid():
            id=kw.get('id')
            qs=Cosmetics.objects.filter(id=id).update(**request.data)
            return Response(data=serializer.data)
        else:
            return Response(data=serializer.errors)

        
    
    def delete(self,request,*args,**kw):
        id=kw.get('id')
        qs=Cosmetics.objects.filter(id=id).delete()
        # serializer=ProductSerializer
        return Response(data='item deleted')





# class CartView(APIView):
#     def create(self,request,*args,**kw):
#         serializer=ProductModelSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(data=serializer.data)
#         else:
#             return Response(data=serializer.errors)
        
#     @action(methods=["POST"],detail=True)
#     def add_cart(self,request,*args,**kw):
#         id=kw.get('pk')
#         user=request.user
#         item=Products.objects.get(id=id)
#         user.carts_set.create(product=item)

#         return Response(data='Item Successfully added to cart')



class PrductViewsetview(ModelViewSet):
    serializer_class=ProductModelSerializer
    queryset=Cosmetics.objects.all()

    authentication_classes=[BasicAuthentication]
    permission_classes=[IsAuthenticated]

    @action(methods=["GET"],detail=False)
    def categories(self,request,*args,**kw):
        qs=Cosmetics.objects.values_list('category',flat=True).distinct()
        return Response(data=qs)
    
    @action(methods=["POST"],detail=True)
    def add_cart(self,request,*args,**kw):
        id=kw.get('pk')
        user=request.user
        item=Cosmetics.objects.get(id=id)
        user.carts_set.create(product=item)

        return Response(data='Item Successfully added to cart')


class UserViewSet(ModelViewSet):
    serializer_class=UserSerializer
    queryset=User.objects.all()




