from django.db import models
from django.contrib.auth.models import User

class Employee(models.Model):
    firstName = models.CharField(max_length=255)
    lastName = models.CharField(max_length=255)
    manager = models.ForeignKey('self', on_delete=models.SET_NULL, null=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.firstName} {self.lastName}"

    def to_dict(self):
        """
        Convert to dict to assist JSON serialising.
        """

        return {
            "firstName" : self.firstName,
            "lastName" : self.lastName,
        }
