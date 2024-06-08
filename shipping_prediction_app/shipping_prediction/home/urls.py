from django.urls import path
from shipping_prediction.home.views import predict_shipping_days, home

urlpatterns = [
    path('predict/', predict_shipping_days, name='predict_shipping_days'),
    path('', home, name='home'),

]