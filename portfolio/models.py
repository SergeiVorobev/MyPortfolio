from django.db import models
from django.contrib.auth.models import User
# Create your models here.
from django.utils import timezone

class MyApp(models.Model):
    name = models.CharField(max_length=64, unique=True)
    desc = models.TextField(default='', blank=True)
    image = models.ImageField(upload_to='my_apps')
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='my_apps')

    def __str__(self):
        return f'{self.id} {self.name}'

    class Meta:
        verbose_name_plural = 'my apps'
        ordering = ['name']

# class Balance(models.Model):
#     BTC = models.DecimalField(max_digits=8, decimal_places=6)
#     USDT = models.DecimalField(max_digits=9, decimal_places=2)
#     date = models.DateField('Event Date', default=timezone.now)
#
#     def __str__(self):
#         return self.name