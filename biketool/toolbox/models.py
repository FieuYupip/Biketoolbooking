from django.db import models
from django.urls import reverse

class Toolbox(models.Model):
    class Meta:
        verbose_name = 'Toolbox'
        verbose_name_plural = 'Toolboxs'

    # TODO: Define fields here
    building = models.ForeignKey('Building', on_delete = models.CASCADE, related_name='toolboxes')

    STATUS = [('A','Avaible'),
            ('U','Unavaiable'),
    ]
    Rent_status = models.CharField(max_length=1, choices= STATUS)
    Rent_date = models.DateField(null=True, blank = True)
    Avaiable_date = models.DateField(null=True, blank = True)

    class Meta:
        ordering = ['-pk']
        verbose_name = 'Toolbox'
        verbose_name_plural = 'Toolboxes'

    def __str__(self):
        return 'Toolbox ID %s, Buidling %s, Status %s' % (self.pk, self.building, self.Rent_status)

    def get_absolute_url(self):
        return reverse('Toolbox_view', kwargs={'pk': self.pk})

class Building(models.Model):
    Adress = models.CharField(max_length=200)

    class Meta:
        ordering = ['-Adress']

    def __str__(self):
        return self.Adress
    
    def get_absolute_url(self):
        return reverse('building_toolbox', args = [self.pk])
