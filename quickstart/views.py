from django.contrib.auth.models import User, Group
from rest_framework import viewsets, generics
from quickstart.serializers import UserSerializer, GroupSerializer, ProductSerializer
from quickstart.models import Product 
from rest_framework.decorators import api_view  
from rest_framework.response import Response
from django.db.models import Q
import quickstart.bl.pandas_example


class UserViewSet(viewsets.ModelViewSet):
    """
        API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined');    
    serializer_class = UserSerializer

class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

class ProductList(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ProductRudView(generics.RetrieveUpdateDestroyAPIView):
    lookup_field = 'pk'    
    serializer_class = ProductSerializer    

    def get_queryset(self):
        return Product.objects.all()

@api_view(['GET'])
def product_up(request):
    query = request.GET.get("q")
    qs = Product.objects.all()
    if query is not None:
        qs = qs.filter(Q(name__icontains=query))
    serializer = ProductSerializer(qs, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def data_test(request):
    val = quickstart.bl.pandas_example.get_data()
    res = val.to_dict('dict')
    return Response(res)