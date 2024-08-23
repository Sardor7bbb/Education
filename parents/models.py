from django.db import models

from users.models import UserModel


class Parent(models.Model):
    user = models.OneToOneField(UserModel, on_delete=models.CASCADE, limit_choices_to={'role': 'Parent'}, related_name='parent')
    children = models.ManyToManyField(UserModel, limit_choices_to={'role': 'User'}, related_name='children')

    def __str__(self):
        return f'{self.user.first_name} {self.user.last_name}'

