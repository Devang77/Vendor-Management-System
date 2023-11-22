# Vendor-Management-System
**Use the Postman to Test the Api Endpoint**

In this project i have created a vendor management system, in this project there a user can create a vendor using the api,and can also view a specific vendor by using the vendor id that yo
you get after creating the vendor to create a vendor through api one can send a Post request to the api and note that Vendor_name,vendor-address,vendor_code,contact_details are the necessary fields.We can also retrive all the vendor information by sending a get request to the api, if you waant to retrive a specific vendor's information that can also be done by using the vendor_id make sure you give the vendor_id in the body of the get request,one can also update the information of the vendor by giving the name of the vendor and the changes you want to make like contact_detail etc in the body of the put request, and also delete a vendor from the system but make sure to give the name of the vendor you want to delete in the body of the request.
we can also create a purchase order and to do that you can use the purchase order api and make sure to include the vendor_id,items and quantity im using vendor_id to associate the purchase order to a specific vendor.we can also view all the purchase orders by using the api, and also retrive a purchase order of a specific vendor through the api, if you want to update an order you can do it by making a put request to the api but make sure to give the purchase order number in the body of the request to update a specific order, to delete an order mention the specific purchase order number in the body of the delete request to delete the order.
the last feature of this project is the performance evaluation like avgerage response time,average quality rating and many more as mentioned in the assignment to create a specific vendor's 
performance metrics just give the vendor's id(i.e vendor_id) and you can calculate the performance metrics of the purchase order whoes status is completed,one can also retrive the performance metrics of a specific vendor's by giving the vendor_id 
The Following are the api Endpoints 

***Note:- Ihave cerated two api endpoints for vendor as i was not able to make two get request from the same api endpoint**
**Vendor Api endpoint**

1)http://127.0.0.1:8000/All_VendorApiView/:-this endpoint gives the information of all the vendors in the system
2)http://127.0.0.1:8000/VendorApiView/:- this endpoint gives the information of a specific vendor in the system and this the and it is also used to perform the update delete functionality

**Performance metrics Api Endpoint**

3)http://127.0.0.1:8000/Performance_metricsApiView/:- This is the endpoint which is used for performance metrics

***Note:- Ihave cerated two api endpoints for purchase order as i was not able to make two get request from the same api endpoint**
**Purchase Order Api Endpoint**

4)http://127.0.0.1:8000/All_Purchase_orderApiView/:-this endpoint gives the information of all the purchase order in the system
5)http://127.0.0.1:8000/Specific_Purchase_orderApiView/:- this endpoint gives the information of a specific purchase_order in the system and it is also used to perform the update delete functionality.
