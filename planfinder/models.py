from django.db import models
from django.utils import timezone

# Create your models here.

STATUS = (
    (0,"Draft"),
    (1,"Published")
)

JOINT = (
    (0,"No"),
    (1,"Yes")
)

class County(models.Model):
    county_id = models.IntegerField(primary_key=True)
    county_name = models.CharField(max_length=99)

    class Meta:
        verbose_name = "County"
        verbose_name_plural = "Counties"

    def __str__(self):
        return self.county_name

class Lpa(models.Model):
    lpa_id = models.IntegerField(primary_key=True)
    lpa_name = models.CharField(max_length=99)
    county = models.ForeignKey(County, on_delete=models.CASCADE, blank=True, null=True)
    LAD19CD = models.CharField(max_length=15, blank=True)
    LAD19NM = models.CharField(max_length=99, blank=True)
    lpa_text = models.CharField(max_length=200, blank=True)

    class Meta:
        verbose_name = "Local Planning Authority"
        verbose_name_plural = "Local Planning Authorities"

    def __str__(self):
        return self.lpa_name

class NationalPark(models.Model):
    natpark_id = models.IntegerField(primary_key=True)
    natpark_name = models.CharField(max_length=99)

    def __str__(self):
        return self.natpark_name

class NeighbourhoodPlan(models.Model):
    plan_name = models.CharField(max_length=200)
    plan_url = models.URLField(max_length=200)
    lpa = models.ForeignKey(Lpa, on_delete=models.CASCADE)
    natpark = models.ForeignKey(NationalPark, on_delete=models.CASCADE, blank=True, null=True)
    map_location = models.CharField(max_length=200)
    ref_date = models.DateField('referendum date', blank=True, null=True)
    supersededDate = models.DateField('date superseded by new plan', blank=True, null=True)
    supersededBy_desc = models.ForeignKey("self", on_delete=models.CASCADE, blank=True, null=True)
    created_date = models.DateTimeField(default=timezone.now, blank=True, null=True)
    status = models.IntegerField(choices=STATUS, default=0)
    cross_authority_plan = models.IntegerField(choices=JOINT, default=0)

    def __str__(self):
        return self.plan_name