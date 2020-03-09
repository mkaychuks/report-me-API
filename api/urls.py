from django.urls import path

from rest_framework.routers import SimpleRouter

from .views import (
    ReportView, ReportCreateView,
    CategoryView, UserProfile, UserList
)

router = SimpleRouter()
router.register('add-reports', ReportCreateView, basename='add-reports')

urlpatterns = [
    path('reports/', ReportView.as_view(), name='reports'),
    path('reports/category/', CategoryView.as_view(), name='categories'),
    path('user/profile/', UserProfile.as_view(), name='user-profile'),
    path('users/', UserList.as_view(), name='user-lists'),
]

urlpatterns1 = router.urls

urlpatterns += urlpatterns1