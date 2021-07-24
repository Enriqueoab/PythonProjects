from django.urls import path
# . = in the current folder
from . import views 

# Array to set each 'URL' (/new,/sales,/other_view,..)
# to a function of our views file

urlpatterns = [
    path('', views.index),
    path('new', views.product_new),
    path('offer', views.product_offer)

]