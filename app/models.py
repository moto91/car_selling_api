from django.db import models

class CarAd(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    brand = models.CharField(max_length=100, blank=False)
    model = models.CharField(max_length=100, blank=False)
    model_year = models.IntegerField(blank=False)
    description = models.TextField(blank=True)
    price = models.FloatField(blank=False)
    email = models.CharField(max_length=100, blank=False)
    
    class Meta:
        db_table = "car_ads"
        app_label = "app"

    def __str__(self):
        return self.brand