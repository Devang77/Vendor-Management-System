from django.shortcuts import render
from .models import *
from django.db.models import Avg
from django.http import HttpResponse
from datetime import datetime,timedelta
from .serializers import *
from rest_framework.views import APIView
from rest_framework import permissions
from rest_framework.decorators import action
from rest_framework.response import Response
class VendorApiView(APIView): 
    def post(self,request):
        new_vendor = Vendor(Vendor_name=request.data.get("Vendor_name"),contact_details=request.data.get("contact_details"),vendor_address=request.data.get("vendor_address"),vendor_code=request.data.get("vendor_code"))
        new_vendor.save()
        return Response({'message':'vendor created'})
    def get(self,request):
        vendor = Vendor.objects.filter(Vendor_name=request.data.get("Vendor_name"))
        serializer = VendorSerializer(vendor,many=True) 
        return Response(serializer.data)
    def put(self,request):
        vendor = Vendor.objects.filter(Vendor_name=request.data.get("Vendor_name")).update(contact_details=request.data.get("contact_details"))
        return Response({'message':'Vendor Details Updated'})
    def delete(self,request):
        vendor = Vendor.objects.filter(Vendor_name=request.data.get("Vendor_name")).delete()
        return Response({'message':'Vendor Deleted'})

class All_VendorApiView(APIView):
    def get(self,request):
        vendor = Vendor.objects.all()
        serializer = VendorSerializer(vendor,many=True) 
        return Response(serializer.data)


class Performance_metricsApiView(APIView):
    def post(self,request):
        # vendor_performance = Vendor.objects.filter(Vendor_name="demo").values()
        
        Total_po = Purchase_Order.objects.filter(vendor_id=request.data.get("vendor_id")).count()
        status = Purchase_Order.objects.filter(status="completed",vendor_id=request.data.get("vendor_id")).values()
        po_status = Purchase_Order.objects.filter(status="completed",vendor_id=request.data.get("vendor_id"),delivery_date="2023-11-2 17:57:07").count()
        On_Time_Delivery_Rate = po_status/Total_po
        
        rating = Purchase_Order.objects.filter(status="completed").aggregate(Avg('quality_rating')).values()
        Quality_rating = float([x for x in rating][0])
        fullfiled_po = Purchase_Order.objects.filter(status="completed",vendor_id=request.data.get("vendor_id")).count()
        Fullfilment_Rate= fullfiled_po / Total_po
        
        
        

        responseTime = Purchase_Order.objects.filter(vendor_id=request.data.get("vendor_id"),status="completed").values()
        # print(responseTime)
        for time in responseTime:
            # print(time)
            issue_Date = time.get("issue_date")
            ack_date =  time.get("acknowledgment_date")
            acknowledgmentDate = ack_date.strftime("%d")
            
            issueDate = issue_Date.strftime("%d")
            
            issue_day = float(issueDate)
            avg_issue_day = Avg(issue_day)
            # print(avg_issue_day)
            # print(issueDate)
            # print(issue_day)
            ack_day = float(acknowledgmentDate)
            avg_ack_day = Avg(ack_day)
            # print(acknowledgmentDate)
            # print(ack_day)
            avg_res_time = ack_day - issue_day
        # Vendor_update = Vendor.objects.filter(Vendor_name="xyz").update(on_time_delivery_rate=On_Time_Delivery_Rate,quality_rating_avg=Quality_rating,fulfillment_rate=Fullfilment_Rate,average_response_time=avg_res_time)
        performance = Performance.objects.create(vendor_id=request.data.get("vendor_id"),date="2023-11-27 17:57:07" ,on_time_delivery_rate=On_Time_Delivery_Rate,quality_rating_avg=Quality_rating,fulfillment_rate=Fullfilment_Rate,average_response_time=avg_res_time)
        return Response({'message':'Performance metrics created'})
        # issueDate = ([time for time in responseTime][0].get("issue_date"))
    # date = issueDate.strftime("%d")
    # acknowledgmentDate = ([time for time in responseTime][0].get("acknowledgment_date"))
    # ack_date = acknowledgmentDate.strftime("%d")
    # ack_day = float(ack_date)
    # issue_day = float(date)
    # avg_res_time = ack_day - issue_day
    # final_date = avg_res_time.timestamp()
    # print(type(avg_res_time))
    
    def get(self,request):
        performance = Performance.objects.filter(vendor_id=request.data.get("vendor_id"))
        serializer = PerformanceSerializer(performance,many=True) 
        return Response(serializer.data)

class Specific_Purchase_orderApiView(APIView):
    def post(self,request):    
        dt = datetime.now()
        td = timedelta(days=5)
        deliveryDate = dt + td
        ack_date = timedelta(days=1)
        ack_day = deliveryDate + ack_date
        # po = Purchase_Order.objects.create()
        po = Purchase_Order.objects.create(vendor_id=request.data.get("vendor_id"),order_date=dt,delivery_date=deliveryDate,items=request.data.get("items"),quantity=request.data.get("quantity"),status="shipping",quality_rating=3.3,issue_date=dt,acknowledgment_date=ack_day)
        return Response({'message':'ordercreated'})
    def get(self,request):   
        purchase = Purchase_Order.objects.filter(po_number=request.data.get("po_number"))
        serializer = PurchaseOrderSerializer(purchase,many=True)
        return Response(serializer.data)
    def put(self,request):
        purchase = Purchase_Order.objects.filter(po_number=request.data.get("po_number")).update(status="completed")
        return Response({'message':'Order Updated'})
    def delete(self,request):
        purchase = Purchase_Order.objects.filter(po_number=request.data.get("po_number")).delete()
        return Response({'message':'Order Deleted'})
class All_Purchase_orderApiView(APIView):        
    def get(self,request):   
        order = Purchase_Order.objects.all()
        purchase = PurchaseOrderSerializer(order,many=True)
        return Response(purchase.data)

