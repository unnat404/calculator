from django.shortcuts import render
from django.http import HttpResponse
import re
# Create your views here.

# added Unnat
from rest_framework import generics, permissions,status, viewsets
from rest_framework.response import Response
from knox.models import AuthToken
from .serializers import ClientSerializer, RegisterSerializer

from .models import Client
# Register API
class RegisterAPI(generics.GenericAPIView):
    serializer_class = RegisterSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({
        "user": ClientSerializer(user, context=self.get_serializer_context()).data,
        "token": AuthToken.objects.create(user)[1]
        })

# for :: model viewset :: automatic basic CRUD functionalities
class ClientViewSet(viewsets.ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer    

# for :: model viewset

# from rest_framework import status
# from rest_framework import viewsets
# from rest_framework.response import Response

# from student import serializers
# from student import models


# class StudentViewSet(viewsets.ModelViewSet):
#     queryset = models.Student.objects.all()
#     serializer_class = serializers.StudentSerializer

def greetings(request):
    # var=request.GET['var']
    res=render(request,'calc.html')
    return res
    
#  instead of eval() use this calculation function - modify it to better handle the error messages
def calculation(request):
    global final_result , result, values
    final_result = float(0)
    result = float(0)
    values = ""
    if request.method=="POST":
        values=request.POST['values'] #string having whole ques
        print(values)
        vals=re.findall(r"(\d+)",values) #extrect values
        operators=['+','x','÷','-','.','%']
        opr=[]
        for v in values:
            for o in operators:
                if v==o:
                    opr.append(o)
        print(opr)                      #extrect operators
        print(re.findall(r"(\d+)",values))

        for o in opr:
            if o=='.':
                i=opr.index(o)
                res=vals[i]+"."+vals[i+1]
                vals.remove(vals[i+1])
                opr.remove(opr[i])
                vals[i]=res
                print(vals)
                print(opr)
        for o in opr:
            if o=='%':
                i=opr.index(o)
                res=(float(vals[i])/100)*float(vals[i+1])
                vals.remove(vals[i+1])
                opr.remove(opr[i])
                vals[i]=res
                print(vals)
                print(opr)
        for o in opr:
            if o=='÷':
                i=opr.index(o)
                res=float(vals[i])/float(vals[i+1])
                vals.remove(vals[i+1])
                opr.remove(opr[i])
                vals[i]=str(res)
                print(vals)
                print(opr)
        for o in opr:
            if o=='x':
                i=opr.index(o)
                res=float(vals[i])*float(vals[i+1])
                vals.remove(vals[i+1])
                opr.remove(opr[i])
                vals[i]=str(res)
                print(vals)
                print(opr)
        for o in opr:
            if o=='+':
                i=opr.index(o)
                res=float(vals[i])+float(vals[i+1])
                vals.remove(vals[i+1])
                opr.remove(opr[i])
                vals[i]=str(res)
                print(vals)
                print(opr)
            if o=='-':
                i=opr.index(o)
                res=float(vals[i])-float(vals[i+1])
                vals.remove(vals[i+1])
                opr.remove(opr[i])
                vals[i]=str(res)
                print(vals)
                print(opr)

        # for o in opr:
        #     if o=='-':
        #         i=opr.index(o)
        #         res=int(vals[i])-int(vals[i+1])
        #         vals.remove(vals[i+1])
        #         opr.remove(opr[i])
        #         vals[i]=str(res)
        #         print(vals)
        #         print(opr)

        # print(opr)
        if len(opr)!=0:
            if opr[0]=='÷':
                result = float(vals[0])/float(vals[1])
            elif opr[0]=='x':
                result = float(vals[0])*float(vals[1])
            elif opr[0]=='+':
                result = float(vals[0])+float(vals[1])
            else :
                result = float(vals[0])-float(vals[1])
        else:
            result = float(vals[0])

        final_result=round(result,2)
        # print(final_result)

        # result = int(vals[0])+int(vals[1])

        # i=0
        # res=int(vals[i])
        # for operator in values:
        #     if not operator.isdigit():
        #         # print(type(int(vals[1])))
        #         # print(value)
        #         if operator=='+':
        #             res=res+int(vals[i+1])
        #         i=i+1
    # context = {'result':final_result,'values':values}
    # res=render(request,'calc.html',context)

    context = {'result':float(0),'values':values}
    res=render(request,'calc.html')
    return res
