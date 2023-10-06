from rest_framework import generics
from django.contrib.auth.models import User
from .serializers import UserSerializer
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework import response
  


@api_view(['POST'])
def post(req):
    api_urls = {
        'Singup':'/api/v1/singup'
    }
    
    return response(api_urls)
    # try:
    #     data = json.loads(req.body)
    # except json.JSONDecodeError:
    #     res_data = {"status": False,
    #                 "message": "invalid data",
    #                 "data":[]
    #                 }
    # serializer = UserSerializer(data=data)
    # if serializer.is_valid():
    #     serializer.save()
    #     res_data = {
    #         "status": True,
    #         "message": "user added",
    #         "data": serializer.data
    #     }
    #     return JsonResponse(res_data, status=200)
    # else:
    #     res_data = {
    #         "status": False,
    #         "message": "Some thing went wrong",
    #         "data":[]
    #     }
    #     return JsonResponse(res_data, status= 404)