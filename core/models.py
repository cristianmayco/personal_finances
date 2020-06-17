from django.db import models
from django.urls import reverse

list_types = (
    ('W', 'Water'),
    ('L', 'Light'),
    ('M', 'Market'),
    ('P', 'Personal'),
    ('G', 'Gifts'),
    ('R', 'Repairs'),
    ('O', 'Others'))


class Bill(models.Model):
    type = models.CharField(
        max_length=1,
        default='O',
        choices=list_types
    )
    description = models.TextField(max_length=255)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    created = models.DateField(auto_now_add=True)
    due_date = models.DateField(blank=False)
    payday = models.DateField(null=True, blank=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.type

    def save(self, *args, **kwargs):
        if not self.active and not self.payday:
            raise ValueError('Inactive payments must have payment date')
        return super(Bill, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('index')

    def get_type(self):
        types = dict(list_types)
        return types[str(self.type)]
