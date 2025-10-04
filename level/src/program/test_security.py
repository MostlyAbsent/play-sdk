from django.test import TestCase, Client
from django.test.utils import setup_test_environment
from django.urls import reverse
from .utils import is_optimal
import json

class ProgramSecurityTestCase(TestCase):
    fixtures = ['data.json']

    def test_api_reject_secure_property_query_manager(self):
        """
        The Employee.manager property should be protected, any query
        containing manager references should be rejected
        """
        payload = json.dumps({"manager__firstName__startswith": "A"})
        res = self.client.post("/employee/",
                               data=payload,
                               content_type="application/json")
        self.assertEqual(res.status_code, 400)
        self.assertEqual(res.content, [])

    def test_api_reject_secure_property_query_user(self):
        """
        The Employee.user property should be protected, any query
        containing user references should be rejected
        """
        payload = json.dumps({"user__username__startswith": "A"})
        res = self.client.post("/employee/",
                               data=payload,
                               content_type="application/json")
        self.assertEqual(res.status_code, 400)
        self.assertEqual(res.content, [])

    def test_api_reject_traversal_query_user(self):
        """
        The Employee.user property should be protected, any query
        containing user references should be rejected, including those
        that traverse a database relationship.
        """
        payload = json.dumps({"manager__user__username__startswith": "A"})
        res = self.client.post("/employee/",
                               data=payload,
                               content_type="application/json")
        self.assertEqual(res.status_code, 400)
        self.assertEqual(res.content, [])
