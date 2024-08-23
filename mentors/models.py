from django.db import models

from users.models import UserModel


class Mentor(models.Model):
    user = models.OneToOneField(UserModel, on_delete=models.CASCADE, related_name='mentor_profile')
    bio = models.TextField(null=True)
    speciality = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.user.first_name} {self.user.last_name} - {self.speciality}'
