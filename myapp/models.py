# myapp/models.py
from django.db import models

class TelegramSubscriber(models.Model):
    chat_id = models.BigIntegerField(unique=True)

    def __str__(self):
        return str(self.chat_id)
