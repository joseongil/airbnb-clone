from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

# test on models.py in users app
class User(AbstractUser):
    # Docstring 이란 기능으로 class가 어떤 class 인지 알려주는기능이고 따옴표 세개로 감싸서 적는다.
    # 요 User class 를 import 한 다른 파일에서 User 위에 마우스 올려보면 저 DOcstring 내용이 보인다. (난 안되네..)
    """ Custom User Model """

    GENDER_MALE = "male"
    GENDER_FEMALE = "female"
    GENDER_OTHER = "other"

    GENDER_CHOICES = (
        (GENDER_MALE, "Male"),
        (GENDER_FEMALE, "Female"),
        (GENDER_OTHER, "Other"),
    )

    LANGUAGE_ENGLISH = "en"
    LANGUAGE_KOREAN = "kr"

    CURRENCY_USD = "usd"
    CURRENCY_KRW = "krw"

    CURRENCY_CHOICES = ((CURRENCY_USD, "USD"), (CURRENCY_USD, "KRW"))

    # Tuple 의 앞의것이 DB에 기록될 값이고, 뒤에것이 Form에 표시될 값이다.
    LANGUAGE_CHOICES = (
        (LANGUAGE_ENGLISH, "English"),
        (LANGUAGE_KOREAN, "Korean"),
    )

    # Default 값은 무조건 지정해줘야하는데 그러기 싫으면 null True 라도 해줘야된다. 그럼 null 이들어간다.
    avatar = models.ImageField(blank=True)
    # 한줄짜리 text 를 쓸수있는 필드인데 TextField보단 이걸 더 많이 쓰게 된다.
    # 난 Male, Female, Other 만 두고 싶어 choice 를 넣어주자.
    gender = models.CharField(choices=GENDER_CHOICES, max_length=10, blank=True)
    bio = models.TextField(blank=True)
    # DateTimeField 는 시간까지 설정할 수 있는거다.
    birthdate = models.DateField(blank=True, null=True)
    language = models.CharField(choices=LANGUAGE_CHOICES, max_length=2, blank=True)
    currency = models.CharField(choices=CURRENCY_CHOICES, max_length=3, blank=True)

    superhost = models.BooleanField(default=False)

    def __str__(self):
        return self.username