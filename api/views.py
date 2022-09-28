
from .models import TranSum
from .serializers import TranSumSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics
from django_filters.rest_framework import DjangoFilterBackend
from datetime import datetime
from django.db.models import Q


class MosCreateList(generics.ListCreateAPIView):
    queryset=TranSum.objects.all()
    serializer_class=TranSumSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['customerId','memberId','type','script']
   
    def get_queryset(self):
        if 'option'=='O':
            return self.queryset.filter(purchaseDate__lt ='date_obj1')

        elif 'option'=='A':
            return self.queryset.filter(Q(purchaseDate__gt ='date_obj1')&Q(purchaseDate__lt ='date_obj2'))
    
    
   
    def list(self, request, *args, **kwargs):
        response = super().list(request, *args, **kwargs)
        response.data = {'status': 'True','message': 'done', 'data': response.data}
        # print("Data------>",response.data['fy'])
        return response

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        # print("Data--->",serializer.data)
        serializer.is_valid(raise_exception=True)
       
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        print("FY-->",serializer.data['fy'])
        print("splited-->",serializer.data['fy'].split("-"))
        print("Split-->start_Year-->",serializer.data['fy'].split("-")[0])
        print("Split-->end_Year-->",serializer.data['fy'].split("-")[1])
        print("O-->",serializer.data['option'])
        print("Purchase date -->",serializer.data['purchaseDate'])
        date_str1 = serializer.data['fy'].split("-")[0]+"-04-01"
        date_str2 = serializer.data['fy'].split("-")[1]+"-03-31"
        date_obj1 = datetime.strptime(date_str1, "%Y-%m-%d")
        date_obj2 = datetime.strptime(date_str2, "%Y-%m-%d")
        print("Date object1 >>>",date_obj1)
        print("Date object2 >>>",date_obj2)

        purchasedate=serializer.data['purchaseDate']
        PurchDate = datetime.strptime(purchasedate, '%Y-%m-%d')
        print("Purchase Date - Date Format -->",PurchDate)
        return Response({'status':True,'Message': 'You have successfully Created','data':serializer.data}, status=status.HTTP_201_CREATED,headers=headers)

    # def get_queryset(self):
    #     stu=TranSum.objects.filter(PurchDate__lt=self.date_obj)
    #     print("All Data ....>",stu)
    #     return stu


class MosRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset=TranSum.objects.all()
    serializer_class=TranSumSerializer
   
    def update(self, request, *args, **kwargs):
       partial = kwargs.pop('partial', False)
       instance = self.get_object()
       serializer = self.get_serializer(instance, data=request.data, partial=partial)
       serializer.is_valid(raise_exception=True)
       self.perform_update(serializer)
       result = {
        "status": True,
        "message": "Data successfully updated",
        "data": serializer.data,
       }
       return Response(result)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.delete()
        return Response({'status':True,'Message': 'You have successfully Deleted'})