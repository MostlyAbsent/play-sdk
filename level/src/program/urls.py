from django.urls import path
from .views import main
from .views.employee import EmployeeView

urlpatterns = [
    path('', EmployeeView.as_view(), name='employee')
]
