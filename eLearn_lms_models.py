from django.db import models
from django.contrib.auth.models import User
from django.db.models import Count
from datetime import datetime

edu_options = (('S', 'School'), ('C', 'College'))
board_options = (('S', 'State Board'), ('C', 'CBSE'), ('I', 'ICSE'))
grade_options = (('I', 'I'), ('II', 'II'), ('III', 'III'), ('IV', 'IV'), ('V', 'V'),
                 ('VI', 'VI'), ('VII', 'VII'), ('VIII', 'VIII'), ('IX', 'IX'), ('X', 'X'), ('XI', 'XI'),
                 ('XII', 'XII'),)
year_options = (('I', 'I'), ('II', 'II'), ('III', 'III'), ('IV', 'IV'), ('V', 'V'))


# User and Related Models
class District(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    mobile_no = models.CharField(max_length=10, null=True)
    address = models.TextField(null=True, blank=True)
    district = models.ForeignKey(District, on_delete=models.CASCADE, null=True)
    education = models.CharField(max_length=1, choices=edu_options, null=True)
    institution = models.CharField(max_length=200, null=True, blank=True)
    board = models.CharField(max_length=1, choices=board_options, null=True, blank=True)
    grade = models.CharField(max_length=4, choices=grade_options, null=True, blank=True)
    year = models.CharField(max_length=3, choices=year_options, null=True, blank=True)

    def __str__(self):
        return self.user.username

    def firstname(self):
        return self.user.first_name

    def lastname(self):
        return self.user.last_name

    def email(self):
        return self.user.email


class Teacher(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    full_name = models.CharField(max_length=30, null=True)
    education = models.CharField(max_length=255)
    experience = models.IntegerField()
    specialization = models.CharField(max_length=255)
    teaching_method = models.TextField()
    video_link = models.CharField(max_length=255, null=True, blank=True)
    email_id = models.EmailField(max_length=50, null=True)
    mobile_no = models.CharField(max_length=10)
    address = models.TextField(null=True)
    district = models.ForeignKey(District, on_delete=models.CASCADE, null=True)
    resume = models.FileField(upload_to='documents/')
    applied_on = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.full_name

    def email(self):
        return self.user.email
