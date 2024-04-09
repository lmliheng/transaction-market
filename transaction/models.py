from django.db import models
from django.contrib.auth.models import User

class Item(models.Model):
    title = models.CharField(max_length=12)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='items/')
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='items')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class Contact(models.Model):
    name = models.CharField(max_length=10, default="保密")
    phone = models.CharField(max_length=11, default="保密")
    email = models.EmailField(default="保密")
    wechat = models.CharField(max_length=50, default="保密")
    qq = models.CharField(max_length=15, default="保密")
    campus = models.CharField(max_length=50, default="保密")
    user = models.OneToOneField(User, on_delete=models.CASCADE, default=3)
    item = models.OneToOneField(Item, on_delete=models.CASCADE)

    def __str__(self):
        return self.name