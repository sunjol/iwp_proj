from django.db import models

from django.contrib.auth import get_user_model
from django.db import models
from account.models import Account

# Create your models here.
User = Account

class Message(models.Model):
    author = models.ForeignKey(User, related_name='author_messages', on_delete=models.CASCADE)
    content = models.TextField()
    roomnumber=models.TextField()
    # reciever= models.ForeignKey(User,related_name='reciever_messages',on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.author.username

    def last_10_messages():
        return Message.objects.order_by('-timestamp').all()[:10]
# Create your models here.
