from django.db import models


class River(models.Model):
    river_name = models.CharField(max_length=20)
    river_length = models.IntegerField()
    river_area = models.IntegerField()
    flows_in_states = models.CharField(max_length=20)
    choice = [('Perennial', 'PERENNIAL'), ('Seasonal', 'SEASONAL')]
    river_mode = models.CharField(max_length=10, choices=choice)

