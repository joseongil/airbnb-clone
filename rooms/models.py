from django.db import models
from django_countries.fields import CountryField
from core import models as core_models

# Create your models here.
class AbstractItem(core_models.TimeStampedModel):

    """ Abstract Item """

    name = models.CharField(max_length=80)

    class Meta:
        abstract = True

    def __str__(self):
        return self.name


class RoomType(AbstractItem):

    """ RoomType Model Definition """

    pass

    class Meta:
        verbose_name = "Room Type"
        ordering = ["-created"]


class Amenity(AbstractItem):
    """ Amenity Model Definition """

    pass

    class Meta:
        verbose_name_plural = "Amenities"


class Facility(AbstractItem):
    """ Facility Model Definition """

    pass

    class Meta:
        verbose_name_plural = "Facilities"


class HouseRule(AbstractItem):
    """ HouseRule ModelDefinition """

    pass

    class Meta:
        verbose_name = "House Rule"


class Photo(core_models.TimeStampedModel):
    """ Photo Model Definition """

    caption = models.CharField(max_length=80)
    file = models.ImageField()

    # Room class 를 Foreign Key 로서 여기에서 등록하면, 실제 Room class는 더 아래에있고,
    # Python 은 수직으로 code를 interpret 하기 때문에 Room 은 없다고 에러가난다. (Room이 위에있으면 에러안나고 잘됨)
    # 근데 여기서 그냥 String으로 명시해주면 Django가 알아서 Room 모델을 말하는거구나 하고 이후에 찾아서 처리해준다.
    # room = models.ForeignKey(Room, on_delete=models.CASCADE)
    room = models.ForeignKey("Room", on_delete=models.CASCADE)

    def __str__(self):
        return self.caption


class Room(core_models.TimeStampedModel):
    """ Room Model Definition """

    name = models.CharField(max_length=140)
    description = models.TextField()
    country = CountryField()
    city = models.CharField(max_length=80)
    price = models.IntegerField()
    address = models.CharField(max_length=140)
    guests = models.IntegerField()
    beds = models.IntegerField()
    bedrooms = models.IntegerField()
    baths = models.IntegerField()
    check_in = models.TimeField()
    check_out = models.TimeField()
    instant_book = models.BooleanField(default=False)
    # ForeignKey 등록 시 import 후 실제 Class를 지정할 수 도있지만, 아래와 같이 String으로 위치.Class명으로해도 처리됨
    # host = models.ForeignKey(user_models.User, on_delete=models.CASCADE)
    host = models.ForeignKey("users.User", on_delete=models.CASCADE)
    room_type = models.ForeignKey(RoomType, on_delete=models.SET_NULL, null=True)
    amenities = models.ManyToManyField("Amenity", blank=True)
    facilities = models.ManyToManyField(Facility, blank=True)
    house_rules = models.ManyToManyField(HouseRule, blank=True)

    def __str__(self):
        return self.name