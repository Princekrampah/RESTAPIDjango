from django.urls import path, include
from . import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('createlistemployee/', views.EmployeeListCreatView.as_view(),
         name='list-employees'),
        path('updatedetaildelete/<int:pk>/',
             views.EmployeeRetrieveUpdateDeleteView.as_view(), name='detail-employees'),

]

urlpatterns = format_suffix_patterns(urlpatterns)
