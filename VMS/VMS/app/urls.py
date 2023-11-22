from django.urls import path,include
from .views import *
urlpatterns = [
     path('All_VendorApiView/',All_VendorApiView.as_view(),name="All_VendorApiView"),
    path('VendorApiView/',VendorApiView.as_view(),name="VendorApiView"),
    path('Performance_metricsApiView/',Performance_metricsApiView.as_view(),name="Performance_metricsApiView"),
    path('Specific_Purchase_orderApiView/',Specific_Purchase_orderApiView.as_view(),name="PurchaseApiView"),
    path('All_Purchase_orderApiView/',All_Purchase_orderApiView.as_view(),name="All_Purchase_orderApiView")
    
]
