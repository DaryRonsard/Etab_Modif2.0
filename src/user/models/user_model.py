from django.db import models
from base.models.helpers.date_time_model import DateTimeModel
from django.contrib.auth.models import AbstractUser


class UserModel(DateTimeModel, AbstractUser):
    school = models.ForeignKey('school.SchoolModel', on_delete=models.CASCADE, null=True)
    role = models.ManyToManyField('user.RoleUserModel')
    #pseudo = models.CharField(max_length=255)
    #password = models.CharField(max_length=255)

    def __str__(self):
        return f'{self.school} - {self.role}'
