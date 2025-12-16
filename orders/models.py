from django.db import models



class coupon(models.Model):
    code = models.CharField(max_length=50, unique=True)
    discount_percentage = models.DecimalField(max_digits=5, decimal_places=2)
    is_active = models.booleanField(default=True)
    valid_from = models.DataField()
    valid_untill = models.DataField()

    def _str_(self):
        return f"{self.code} ({self.discount_percentage * 100}% off)"