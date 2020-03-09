from django.shortcuts import render
from django.contrib.auth.models import User


from rest_framework.generics import (
    ListAPIView, RetrieveAPIView,
)
from rest_framework import permissions, viewsets


from .models import Report, Category
from .serializers import (
    ReportListSerializer, UserSerializer, CategorySerializer, ReportCreateSerializer
)
from .permissions import IsAuthor

# The following views are grouped under the same function
# Its separated now because I have not learnt how to make a SerializerMethodField() writable
# thus the dupication of codes.. 
class ReportView(ListAPIView):
    """Lists the total number of reports"""
    serializer_class = ReportListSerializer

    def get_queryset(self):
        queryset = Report.objects.order_by('-reported_time')
        return queryset


class ReportCreateView(viewsets.ModelViewSet):
    """Allows for the creation of new reports"""
    queryset = Report.objects.all()
    serializer_class = ReportCreateSerializer
    permission_classes = (IsAuthor, permissions.IsAuthenticated,)




# Lists the various categories
class CategoryView(RetrieveAPIView):
    serializer_class = CategorySerializer
    
    def get_queryset(self):
        try:
            queryset = Category.objects.all()
            return queryset
        except:
            pass



# returns the UserProfile of the logged in User
class UserProfile(ListAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = (permissions.IsAuthenticated,)

    def get(self, request):
        serializer = UserSerializer(request.user)
        return Response(serializer.data)

class UserList(ListAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = (permissions.IsAuthenticated,)