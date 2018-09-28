from django.conf.urls import url
from quickstart.views import ProductList, ProductRudView, product_up, data_test


urlpatterns = [
    url(r'^$', ProductList.as_view(), name='product'),
    url(r'all', product_up, name='product11'),
    url(r'data', data_test, name='data'),
    url(r'(?P<pk>\d+)/', ProductRudView.as_view(), name='product22'),
    
    
]