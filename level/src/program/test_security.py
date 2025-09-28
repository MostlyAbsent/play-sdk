from django.test import TestCase, Client
from django.test.utils import setup_test_environment
from django.urls import reverse
from .utils import is_optimal
import json

class ProgramSecurityTestCase(TestCase):
    fixtures = ['data.json']

    def test_alice_password_ittr_w_firstName(self):
        payload = json.dumps({"manager__user__password__startswith": "p",
                              "firstName": "Robert"})
        res = self.client.post("/employee/",
                               data=payload,
                               content_type="application/json")
        self.assertEqual(res.status_code, 200)
        expected = """[{"firstName":"Robert","lastName":"Smith"}]"""
        self.assertEqual(res.content.decode('utf-8'), expected)

    def test_alice_password_itterable(self):
        payload = json.dumps({"manager__user__password__startswith": "p"})
        res = self.client.post("/employee/",
                               data=payload,
                               content_type="application/json")
        self.assertEqual(res.status_code, 200)
        self.assertEqual(json.loads(res.content), [])
