from django.test import TestCase, Client
from django.test.utils import setup_test_environment
from django.urls import reverse
import json
from .models.employee import Employee

class ProgramTestCase(TestCase):
    fixtures = ['data.json']

    def test_find_robert(self):
        payload = json.dumps({"firstName": "Robert"})
        res = self.client.post("/employee/",
                               data=payload,
                               content_type="application/json")
        self.assertEqual(res.status_code, 200)
        expected = """[{"firstName": "Robert", "lastName": "Smith"}]"""
        self.assertJSONEqual(res.content, expected)

    def test_employee_endpoint_get_forbidden(self):
        res = self.client.get("/employee")
        self.assertEqual(res.status_code, 301)
