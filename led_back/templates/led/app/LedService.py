#-*-coding:utf-8-*-
#author: liuce

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import exceptions
from rest_framework import status
from led.util.LedUtil import ledOff,ledOn

class LedService(APIView):

    def get(self,request, *args, **params):
        status = params['status']
        try:
            if status == 'on':
                ledOn()
            if status == 'off':
                ledOff()
            return Response(status)
        except Exception as e:
            print(e)
            return Response(status.HTTP_501_NOT_IMPLEMENTED)

    def post(self,request,*args, **params):
        pass