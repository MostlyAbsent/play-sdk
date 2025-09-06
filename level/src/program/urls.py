from django.urls import path
from .views import main
from .views.employee import EmployeeView

urlpatterns = [
    path('', main.index, name='index'),
    path('employee/', EmployeeView.as_view(), name='employee')
]
