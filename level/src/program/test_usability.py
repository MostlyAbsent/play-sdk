from django.test import TestCase, Client
from django.test.utils import setup_test_environment
from django.urls import reverse
import json
from .models.employee import Employee

class ProgramTestCase(TestCase):
    fixtures = ['data.json']

    def test_query_by_firstName(self):
        payload = json.dumps({"firstName": "Robert"})
        res = self.client.post("",
                               data=payload,
                               content_type="application/json")
        self.assertEqual(res.status_code, 200)
        expected = [{"firstName": "Robert", "lastName": "Smith"}]
        self.assertJSONEqual(res.content, expected)

    def test_query_by_lastName(self):
        payload = json.dumps({"lastName": "Smith"})
        res = self.client.post("",
                               data=payload,
                               content_type="application/json")
        self.assertEqual(res.status_code, 200)
        expected = [{"firstName": "Robert", "lastName": "Smith"},
                    {"firstName": "Alice", "lastName": "Smith"}]
        self.assertJSONEqual(res.content, expected)

    def test_query_by_lastName_contains(self):
        payload = json.dumps({"lastName__contains": "mi"})
        res = self.client.post("",
                               data=payload,
                               content_type="application/json")
        self.assertEqual(res.status_code, 200)
        expected = [{"firstName": "Robert", "lastName": "Smith"},
                    {"firstName": "Alice", "lastName": "Smith"}]
        self.assertJSONEqual(res.content, expected)

    def test_query_by_firstName_and_lastName(self):
        payload = json.dumps({"firstName": "Robert", "lastName": "Smith"})
        res = self.client.post("",
                               data=payload,
                               content_type="application/json")
        self.assertEqual(res.status_code, 200)
        expected = [{"firstName": "Robert", "lastName": "Smith"}]
        self.assertJSONEqual(res.content, expected)
