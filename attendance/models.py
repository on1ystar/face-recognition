from django.conf import settings
from django.core.validators import MinLengthValidator
from django.db import models
from django.urls import reverse
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager,PermissionsMixin
import uuid
from django.contrib.auth.models import User


# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, primary_key=True, on_delete=models.CASCADE)
    school = models.CharField(max_length=20)
    student_id = models.CharField(max_length=20, blank=True)
    classroom_set = models.ManyToManyField('Classroom', blank=True, through='Role')

    def __str__(self):
        return f'{self.user}'

class UserPhoto(models.Model):
    user = models.ForeignKey(Profile, on_delete=models.CASCADE)
    photo = models.ImageField(upload_to='checkmate/user', blank=True)  # photo.url 로 접근해야 이미지 보임


class Classroom(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=30)
    desc = models.TextField(blank=True)
    timer = models.DurationField(blank=True)
    personnel = models.PositiveIntegerField(default=10)
    created_at = models.DateTimeField(auto_now_add=True)
    # profile_set -> related name
    # add, remove 함수로 유저 추가, 삭제

    def __str__(self):
        return f'{self.name}'
    
class Role(models.Model):
    user = models.ForeignKey(Profile, on_delete=models.CASCADE)
    classroom = models.ForeignKey(Classroom, on_delete=models.CASCADE)
    is_checker = models.BooleanField(default=False, verbose_name='체커')

    def __str__(self):
        return f'{self.is_checker}' 

class Attendance(models.Model):
    user = models.ForeignKey(Profile, on_delete=models.CASCADE)
    classroom = models.ForeignKey(Classroom, on_delete=models.CASCADE)
    is_attendance = models.BooleanField(default=False)
    time_out = models.DurationField(default=0, blank=True)
    checked_at = models.DateTimeField(auto_now_add=True)
