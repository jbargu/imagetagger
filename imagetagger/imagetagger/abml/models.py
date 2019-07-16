from django.db import models
from imagetagger.images.models import ImageSet

# Create your models here.

class ABMLExperiment(models.Model):
    RECOMMENDER = [
        (0, 'baseline'),
        (1, 'abml'),
    ]

    name = models.CharField(max_length=200)
    image_set = models.ForeignKey(
        ImageSet, on_delete=models.CASCADE)

    recommender = models.IntegerField(choices=RECOMMENDER, default=0)
