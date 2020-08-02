from django.db import models
from django.contrib.auth.models import User
from django.db.models import Count
from datetime import datetime

from django.urls import reverse
from django.utils.safestring import mark_safe

status_option = (('R', 'Requested'), ('E', 'Enrolled'), ('D', 'Denied'))


class Domain(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

    @property
    def sorted_course_set(self):
        return self.course_set.annotate(num_enrollment=Count('courseenroll')).filter(is_active=True).order_by(
            '-num_enrollment')


# course related models
class Course(models.Model):
    title = models.CharField(max_length=100)
    domain = models.ForeignKey(Domain, on_delete=models.CASCADE, null=True)
    description = models.TextField()
    image = models.ImageField(upload_to='course/')
    start_from = models.DateField()
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    created_on = models.DateField(auto_now_add=True)
    is_active = models.BooleanField(default=False)

    def __str__(self):
        return self.title

    def lesson_count(self):
        data = Course.objects.filter(id=self.id).aggregate(lesson_count=Count('lesson'))
        return data['lesson_count']

    def video_count(self):
        data = Course.objects.filter(id=self.id).aggregate(video_count=Count('lesson__video'))
        return data['video_count']

    def material_count(self):
        data = Course.objects.filter(id=self.id).aggregate(material_count=Count('lesson__material'))
        return data['material_count']


class Lesson(models.Model):
    name = models.CharField(max_length=200)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    def changeformlink(self):
        if self.id:
            changeformurl = reverse(
                'admin:course_lesson_change', args=(self.id,)
            )
            return mark_safe(u'<a href="%s" target="_blank">Details</a>' % changeformurl)
        return u''

    changeformlink.allow_tags = True
    changeformlink.short_description = ''


class CourseEnroll(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    enrolled_on = models.DateField(auto_now_add=True)
    status = models.CharField(max_length=1, choices=status_option, default='R')

    def __str__(self):
        return self.course.title


# material and video for the couse
class Material(models.Model):
    # topic = models.ForeignKey(Topic, on_delete=models.CASCADE, null=True, blank=True)
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=50)
    description = models.TextField()
    material = models.FileField(upload_to='material/')
    added_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    @property
    def material_url(self):
        if self.material:
            return self.material.url


class Video(models.Model):
    # topic = models.ForeignKey(Topic, on_delete=models.CASCADE, null=True, blank=True)
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=50)
    link = models.CharField(max_length=255)
    added_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
