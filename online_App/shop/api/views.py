
from pickle import TRUE
from urllib import response
from django.http.response import JsonResponse
from shop.models import Category,Product,Customer,Order
from .serializers import CategorySerializers, CustomerSerializers, ProductSerializers,OrderSerializers

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.generics import ListCreateAPIView


def apiOverview(request):
    return JsonResponse('Api Base view', safe=False)

@api_view (['GET'])
def categorylistapi(request):
    categories = Category.objects.all()
    serializer = CategorySerializers(categories,many=True)
    return Response(serializer.data)

@api_view(["GET"])
def customerlistapi(request):
    customers = Customer.objects.all()
    serializer = CustomerSerializers(customers,many=True)
    return Response(serializer.data)


@api_view(['GET'])
def productlistapi(request):
    products = Product.objects.all()
    serializer = ProductSerializers(products,many=True)
    return Response(serializer.data)


class catList(ListCreateAPIView):
    queryset= Category.objects.all()
    serializer_class = CategorySerializers

    def list(self,request):
        queryset=self.get_queryset()
        serializer=CategorySerializers(queryset,many=True)

        return Response(serializer.data)

class cus_List(ListCreateAPIView):
    queryset = Customer.objects.all()
    serializer_class= CustomerSerializers
    def list(self,request):
        queryset=self.get_queryset()
        serializer=CustomerSerializers(queryset,many=True)
        return Response(serializer.data)

class OrderList(ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class= OrderSerializers
    def list(self,request):
        queryset=self.get_queryset()
        serializer=OrderSerializers(queryset,many=True)
        return Response(serializer.data)