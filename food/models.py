from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
# Create your models here.
class Item(models.Model):
    # เวลาโชว์ list ของ obj จะให้แสดงเป็นค่่าอะไร (df เป๋น pk)
    def __str__(self):
        return self.item_name
    user_name = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    item_name = models.CharField(max_length=200)
    item_desc = models.CharField(max_length=200)
    item_price = models.IntegerField()
    item_img = models.CharField(max_length=500, default="https://image.shutterstock.com/image-vector/dish-sketch-vector-illustration-isolated-260nw-582588370.jpg")

    def get_absolute_url(self):
        return reverse("food:detail", kwargs={"pk": self.pk})