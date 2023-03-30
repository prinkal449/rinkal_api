from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import *
from .serializers import *

# Create your views here.

class GetUserData(APIView):

    def get(self, request):
        all_python_data = Buyer.objects.all()
        d1 = DataConverter(all_python_data, many=True)
        return Response(d1.data)


class CreateUserData(APIView):

    def post(self, request):
        d1 = DataConverter(data= request.data)
        if d1.is_valid():
            d1.save() # aa method call karvathi J db ma row create thase
            all_python_data = Buyer.objects.all()
            d1 = DataConverter(all_python_data, many=True)
            return Response(d1.data)
        else:
            return Response(d1.errors)

        
class EditUserData(APIView):
    
    def put(self, request, pk):
        python_row = Buyer.objects.get(id=pk)
        d1 = DataConverter(python_row, data=request.data)
        if d1.is_valid():
            d1.save()
            all_python_data = Buyer.objects.all()
            d1 = DataConverter(all_python_data, many=True)
            return Response(d1.data)
        else:
            return Response(d1.errors)


class DeleteUserData(APIView):
    
    def delete(self, request, pk):
        d_row = Buyer.objects.get(id=pk)
        d_row.delete()
        all_python_data = Buyer.objects.all()
        d1 = DataConverter(all_python_data, many=True)
        return Response(d1.data)