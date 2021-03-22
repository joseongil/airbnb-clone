from django.db import models
from core import models as core_models

# Create your models here.

# List는 내가 좋아요 누른 방들을 모아놓은 것들이다.  간단하게 list명, 사용자, 방 만으로 구성하자
# 이 때 여러개의 list가 특정 방과의 relation을 가질 수 있고 이 list가 여러개의 방과도 relation을 가질 수 있어서 방은 m2m 임
class List(core_models.TimeStampedModel):

    """ List Model Definition """

    name = models.CharField(max_length=80)
    user = models.ForeignKey("users.User", on_delete=models.CASCADE)
    rooms = models.ManyToManyField("rooms.Room", blank=True)

    def __str__(self):
        return self.name