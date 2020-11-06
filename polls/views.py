
from django.views.decorators.csrf import csrf_exempt
from django.db import models
from polls.models import Users
from http import HTTPStatus
from django.http import HttpResponse
from rest_framework.response import Response
import rest_framework
from django.core.exceptions import ObjectDoesNotExist
from rest_framework.decorators import api_view
from django.views.decorators.csrf import csrf_exempt


@api_view(['GET', 'PUT', 'DELETE','POST'])
@csrf_exempt
def user(request,pk): # creating
        if request.method == 'POST' :
            try:
                user = Users.objects.get(user_id=pk)
                return Response({"message": "User exist,enter new user_id"})
            except ObjectDoesNotExist:

                data = request.data
                user = Users(user_id = pk,full_name=data["full_name"])
                user.save()
                return Response({"message":"user created","full_name":user.full_name})

        if request.method == 'DELETE':
            user = Users.objects.get(user_id=pk)
            full_name = user.full_name
            user.delete()
            return Response({"message":"user deleted","full_name":full_name})

        if request.method == 'GET':
            user = Users.objects.get(user_id=pk)
            full_name = user.full_name
            user_id = user.user_id
            return Response({"user_id":user_id,"full_name":full_name})

        if request.method == 'GET':
            user = Users.objects.get(user_id=pk)
            data = request.data
            user.full_name=data["full_name"]
            user.user_id = pk
            user.save()
            return Response({"message":"user edited","full_name":user.full_name})