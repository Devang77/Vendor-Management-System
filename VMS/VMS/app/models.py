from django.db import models
import jsonfield
import uuid
class Vendor(models.Model):
    Vendor_name = models.CharField(max_length=50,null=False)
    contact_details = models.TextField(max_length=50,null=False)
    vendor_address = models.TextField(max_length=50,null=False)
    vendor_code = models.CharField(max_length=50,unique=True,null=False)
    on_time_delivery_rate = models.FloatField(max_length=50,null=True)
    quality_rating_avg = models.FloatField(max_length=50,null=True)
    average_response_time = models.FloatField(max_length=50,null=True)
    fulfillment_rate = models.FloatField(max_length=50,null=True)
    def __str__(self):
        return self.Vendor_name

class Purchase_Order(models.Model):
    po_number = models.CharField(max_length=50,unique=True,default=uuid.uuid4)
    vendor = models.ForeignKey(Vendor,on_delete=models.CASCADE)
    order_date = models.DateTimeField()
    delivery_date = models.DateTimeField()
    items = jsonfield.JSONField()
    quantity = models.IntegerField(null=False)
    status = models.CharField(max_length=50,null=True)
    quality_rating = models.FloatField(max_length=50,null=True)
    issue_date = models.DateTimeField()
    acknowledgment_date = models.DateTimeField(null=True,blank=True)
    def __str__(self):
        return self.po_number

class Performance(models.Model):
    vendor = models.ForeignKey(Vendor,on_delete=models.CASCADE)
    date = models.DateTimeField()
    on_time_delivery_rate = models.FloatField(max_length=50,null=True)
    quality_rating_avg = models.FloatField(max_length=50,null=True)
    average_response_time = models.FloatField(max_length=50,null=True)
    fulfillment_rate = models.FloatField(max_length=50,null=True)

