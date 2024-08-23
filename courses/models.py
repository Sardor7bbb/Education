from django.db import models

# from mentors.models import Mentor
from users.models import UserModel


class CourseModel(models.Model):
    group = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    subject = models.CharField(max_length=100)
    student = models.ForeignKey(UserModel, on_delete=models.SET_NULL, null=True,  limit_choices_to={'role': 'User'}, related_name='student_course')
    mentor = models.ForeignKey(UserModel, on_delete=models.SET_NULL, null=True, limit_choices_to={'role': 'Mentor'},related_name='mentor_course')

    def __str__(self):
        return f'{self.group} - {self.name}'

