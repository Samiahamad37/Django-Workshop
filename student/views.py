from django.shortcuts import render

# drf views 
# 1. FUNCTIONAL BASED -> @api_view

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Student
from .serializer import StudentSerializer
from rest_framework.views import APIView
from rest_framework.generics import ListCreateAPIView
from rest_framework import mixins, generics
from rest_framework.viewsets import ModelViewSet


@api_view(['GET', 'POST'])
def student_ListCreate(request):
    if request.method == 'POST':
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    if request.method == 'GET':
        Students =Student.objects.all()
        serializer= StudentSerializer(Student, many=True)
        return Response(serializer.data)



# 2. CLASS BASED
#    i. APIVIEW

class StudentView(APIView):
    def post(self,request):
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    

    def get(self, request):
        student= Student.object.all()
        serializer = StudentSerializer(student, many=True)
        return Response
    

# ii. Generic view
class StudentListCreate(ListCreateAPIView):
    queryset = Student.object.all()
    serializer_class=StudentSerializer



# iii. mixin view
class StudenMixinView(mixins.ListModelMixin,
                     mixins.CreateModelMixin,
                     generics.GenericAPIView):
    queryset = Student.object.all()
    serializer_class=StudentSerializer

    def get(self, request):
        return self.list(request)
    
    def post(self, request):
        return self.create(request) 
    


# iv. Viewset
class StudentViewSet(ModelViewSet):
    queryset = Student.object.all()
    serializer_class=StudentSerializer
