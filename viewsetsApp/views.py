from rest_framework.viewsets import ModelViewSet
from .models import Course
from .serializer import CourseSerializer

'''
One viewset is capable enough to handle 
non primary key based operations
and primary key based operations.
'''

class CourseViewSet(ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer