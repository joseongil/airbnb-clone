from django.db import models
from core import models as core_models

# Create your models here.


class Conversation(core_models.TimeStampedModel):

    """ Converstation model definition """

    participants = models.ManyToManyField("users.User", blank=True)

    def __str__(self):
        return f"{self.created}"


class Message(core_models.TimeStampedModel):

    """ Message model definition """

    message = models.TextField()
    user = models.ForeignKey("users.User", on_delete=models.CASCADE)
    conversation = models.ForeignKey(
        "conversations.Conversation", on_delete=models.CASCADE
    )

    def __str__(self):
        return f"{self.user} says: {self.message}"