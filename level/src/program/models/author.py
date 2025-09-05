from django.db import models
from django.contrib.auth.models import User
from .department import Department

class Author(models.Model):
    # An one-to-one mapping to the user that is associated to this author
    # Reason why this is done is because for Django it is not recommended to modify the User model
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    # An example how users could be organised into different groups
    # In this example users are organised into Departments they work for
    departments = models.ManyToManyField(Department, related_name='employees')

    def __str__(self) -> str:
        return f"{self.user.username}"
