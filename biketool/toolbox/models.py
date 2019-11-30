from django.db import models
from django.urls import reverse
import datetime
from datetime import timedelta
class Toolbox(models.Model):
    class Meta:
        verbose_name = 'Toolbox'
        verbose_name_plural = 'Toolboxs'

    # TODO: Define fields here
    STATUS = [('A','Avaible'),
            ('U','Unavaiable'),
    ]
    Rent_status = models.CharField(max_length=1, choices= STATUS)
    building = models.ForeignKey('Building', on_delete = models.CASCADE, related_name='Toolbox')
    Rent_date = models.DateTimeField(null=True, blank = True)
    Avaiable_date = models.DateTimeField(null=True, blank = True)

    class Meta:
        ordering = ['-pk']
        verbose_name = 'Toolbox'
        verbose_name_plural = 'Toolboxes'

    def __str__(self):
        return 'Toolbox ID %, Buidling %, Status %' % (self.pk, self.building, self.Rent_status)

    def get_absolute_url(self):
        return reverse('Toolbox_view', kwargs={'pk': self.pk})

class Building(models.Model):
    Adress = models.CharField(max_length=200)

    class Meta:
        ordering = ['-Adress']
        verbose_name = 'Adress'
        verbose_name_plural = 'Adressses'

    def __str__(self):
        return self.Adress
    
    def get_absolute_url(self):
        return reverse('address_views', args = [self.pk])
