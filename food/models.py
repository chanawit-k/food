from django.db import models

# Create your models here.
class Item(models.Model):
    # เวลาโชว์ list ของ obj จะให้แสดงเป็นค่่าอะไร (df เป๋น pk)
    def __str__(self):
        return self.item_name

    item_name = models.CharField(max_length=200)
    item_desc = models.CharField(max_length=200)
    item_price = models.IntegerField()