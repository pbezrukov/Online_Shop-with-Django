
from django.db import models

# Create your models here.


class UserStripe(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    stripe_id = models.CharField(max_length=120)

    def __str__(self):
        return str(self.stripe_id)

# cus_FnpaLcT0sdIFx6
# cus_Fnq95IzzIkv69S


