from django.db import models
from django.conf import settings
from imagetagger.images.models import ImageSet, Team

# Create your models here.

class ABMLExperiment(models.Model):
    RECOMMENDER = [
        (0, 'baseline'),
        (1, 'abml'),
    ]

    time = models.DateTimeField(auto_now_add=True)
    creator = models.ForeignKey(settings.AUTH_USER_MODEL,
                                default=None,
                                on_delete=models.SET_NULL,
                                null=True,
                                blank=True)
    team = models.ForeignKey(
        Team,
        on_delete=models.SET_NULL,
        null=True,
    )
    name = models.CharField(max_length=200)
    description = models.TextField(max_length=1000, null=True, blank=True)

    image_set = models.ForeignKey(
        ImageSet, on_delete=models.CASCADE)
    recommender = models.IntegerField(choices=RECOMMENDER, default=0)
