
# ViewSet
------
Viewset are different and apiview methods are different
Viewset is alternative to APIView


APIView => get(),put(),patch(),post(),delete()
ViewSet => 
- list() => To get all resources/records
- retrieve() => To get a specific resource
- create() => To create a new resource
- update() => To perform full updation
- partial_update() => To perform partial update
- destroy() => To delete a resource

Only method names are different, but the remaining functionality is the same
- get() = list(),retrieve()
- post() => create()
- put() => update()
- patch() => partial_update()
- delete() => destroy()

if we want to create a fast api, go for viewset-recommended 
apiview everything we have to write 

## Q1 When ViewSet is a Best Choice:
1. If we want to develop a simple CRUD interface for our database
2. If we want to develop API very quickly
3. If we are performing standard operation
4. If we are not performing any complex operation

APIView we are response to define URL patteren(URL match)

In viewset:
Routers will map views to urls automatically

### Q How to define a router?
DFR provides a special class => DefaultRouter: automatically define router

### Q How to create Default router
base_name => basename they change the variable name

usage of multiple view is not required one viewset is enough
they need primary key: retrieve(), update(),partial_update(),destroy()

viewset always talk about database CRUD operation only
for normal view method better to go apiview

views.py => Business logic

## Demo application for APIView with models:
-----------------------------------------



## How to use APIViews to perform CRUD Operations:
----------------------------------------------

APIView
ListAPIView =>List out all records
CreateAPIView => Create a new record



### Retrieve Operation:
--------------------
To get a particular record(detail operation)


RetrieveAPIView


## APIView:
-------
1. ListAPIView
2. CreateAPIView
3. RetrieveAPIView
4. UpdateAPIView
5. DestroyAPIView
6. ListCreateAPIView
7. RetrieveUpdateAPIView
8. RetrieveDestroyAPIView
9. RetrieveUpdateDestroyAPIView



Implement both list and Create simultaneously:
----------------------------------------------
ListCreateAPIView

ImplementBoth Retrieve and Update Operation:
--------------------------------------------
RetrieveUpdateApiView

Implement Both Retrieve and Delete Operation:
---------------------------------------------
RetrieveDestroyAPIView

Dont go for apiView go for viewset


