from django.db import models


class Bill(models.Model):
    type = models.CharField(
        max_length=1,
        default='O',
        choices=(
            ('W', 'Water'),
            ('L', 'Light'),
            ('M', 'Market'),
            ('P', 'Personal'),
            ('G', 'Gifts'),
            ('R', 'Repairs'),
            ('O', 'Others'),
        )
    )
    description = models.TextField(max_length=255)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    create = models.DateField(auto_now_add=True)
    due_date = models.DateField(blank=False)
    payday = models.DateField(null=True, blank=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.type

    def save(self, *args, **kwargs):
        if self.payday is None or self.payday == '' and self.active is False:
            raise ValueError('Inactive payments must have payment date')
        return super(Bill, self).save(*args, **kwargs)
