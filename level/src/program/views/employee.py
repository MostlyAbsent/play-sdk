import json
from django.views import View
from django.shortcuts import render
from django.http import JsonResponse, HttpRequest
from ..models.employee import Employee

class EmployeeView(View):
    """
    A vulnerable endpoint that responds to JSON formatted queries for
    users of the system.
    """
    def post(self, request: HttpRequest, *args, **kwargs):
        print(f"--- EmployeeView POST received ---")

        try:
            request_data = json.loads(request.body)
        except json.JSONDecodeError:
            return JsonResponse(
                {"error": "Invalid JSON in request body"}, status = 400
            )
        except Exception as e:
            print(f"Error parsing request body: {e}")
            return JsonResponse(
                {"error": "Bad Request"}, status = 400
            )

        FORBIDDEN_KEYS = {
            'manager',
            'user'
        }

        def filter_fun(key: str) -> bool:
            for k in FORBIDDEN_KEYS:
                if k in key:
                    return False
            return True

        filtered_req = {}
        for key, value in request_data.items():
            if filter_fun(key):
                filtered_req[key] = value
            else:
                return JsonResponse([], status=400, safe=False)

        try:
            employees = Employee.objects.filter(**request_data)
            print(f"Queryset count: {employees.count()}")
            serialized_data =[employee.to_dict() for employee in employees]
        except Exception as e:
            print(e)
            return JsonResponse([], status=500, safe=False)
        return JsonResponse(serialized_data, safe=False)

    def get(self, request: HttpRequest, *args, **kwargs):
        return render(request, "employee_form.html")
