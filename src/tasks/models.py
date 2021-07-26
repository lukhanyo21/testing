from django.db import models
from libs.models import BaseModel
from django.contrib.auth.models import User
# from django.contrib.postgres.fields import ArrayField


# Create your models here.
class Task(BaseModel):

    availability = models.DateTimeField(max_length=255, blank=False, null=False)
    name = models.ForeignKey(User, on_delete=models.CASCADE, blank=False, null=False)

    # def __str__(self):
    #     return self.name

    def get_full_name(self):
        return self.User.get_full_name()
