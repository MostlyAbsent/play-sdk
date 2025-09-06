from rest_framework.views import APIView
from rest_framework.request import Request
from rest_framework.response import Response
from ..models.employee import Employee
from ..serializers.employee import EmployeeSerializer

class EmployeeView(APIView):
    """
        Some basic API view that users send requests to for
        searching for employees
    """
    def post(self, request: Request, format=None):
        print(f"--- EmployeeView POST received ---")
        try:
            employees = Employee.objects.filter(**request.data)
            print(f"Queryset count: {employees.count()}")
            serializer = EmployeeSerializer(employees, many=True)
        except Exception as e:
            print(e)
            return Response([])
        return Response(serializer.data)
