from django.db import models



class RentalRecord(models.Model):
    name = models.CharField(max_length=255)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    amount_remaining = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='images/', blank=True, null=True)
    address = models.TextField(blank=True)

    def __str__(self):
        return self.name
