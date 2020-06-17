from django.db import models
from django.urls import reverse
from decimal import Decimal


# Create your models here.

class County(models.Model):
    name = models.CharField(max_length=99)

    class Meta:
        verbose_name = "County"
        verbose_name_plural = "Counties"

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('county-detail', args=[str(self.id)])


class LocalAuthorityLHN(models.Model):
    la_code = models.CharField(max_length=99, default ="")
    la_area = models.CharField(max_length=99)
    county = models.ForeignKey(County, on_delete=models.CASCADE, blank=True, null=True)
    hp_2018 = models.DecimalField(max_digits=10, decimal_places=3, default=0, blank=True, null=True)
    hp_2019 = models.DecimalField(max_digits=10, decimal_places=3, default=0, blank=True, null=True)
    hp_2020 = models.DecimalField(max_digits=10, decimal_places=3, default=0, blank=True, null=True)
    hp_2021 = models.DecimalField(max_digits=10, decimal_places=3, default=0, blank=True, null=True)
    hp_2022 = models.DecimalField(max_digits=10, decimal_places=3, default=0, blank=True, null=True)
    hp_2023 = models.DecimalField(max_digits=10, decimal_places=3, default=0, blank=True, null=True)
    hp_2024 = models.DecimalField(max_digits=10, decimal_places=3, default=0, blank=True, null=True)
    hp_2025 = models.DecimalField(max_digits=10, decimal_places=3, default=0, blank=True, null=True)
    hp_2026 = models.DecimalField(max_digits=10, decimal_places=3, default=0, blank=True, null=True)
    hp_2027 = models.DecimalField(max_digits=10, decimal_places=3, default=0, blank=True, null=True)
    hp_2028 = models.DecimalField(max_digits=10, decimal_places=3, default=0, blank=True, null=True)
    hp_2029 = models.DecimalField(max_digits=10, decimal_places=3, default=0, blank=True, null=True)
    hp_2030 = models.DecimalField(max_digits=10, decimal_places=3, default=0, blank=True, null=True)
    hp_2031 = models.DecimalField(max_digits=10, decimal_places=3, default=0, blank=True, null=True)
    hp_2032 = models.DecimalField(max_digits=10, decimal_places=3, default=0, blank=True, null=True)
    hp_2033 = models.DecimalField(max_digits=10, decimal_places=3, default=0, blank=True, null=True)
    hp_2034 = models.DecimalField(max_digits=10, decimal_places=3, default=0, blank=True, null=True)
    hp_2035 = models.DecimalField(max_digits=10, decimal_places=3, default=0, blank=True, null=True)
    hp_2036 = models.DecimalField(max_digits=10, decimal_places=3, default=0, blank=True, null=True)
    hp_2037 = models.DecimalField(max_digits=10, decimal_places=3, default=0, blank=True, null=True)
    hp_2038 = models.DecimalField(max_digits=10, decimal_places=3, default=0, blank=True, null=True)
    hp_2039 = models.DecimalField(max_digits=10, decimal_places=3, default=0, blank=True, null=True)
    med_aff_rat_2017 = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    med_aff_rat_2018 = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    med_aff_rat_2019 = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    notes = models.TextField(blank=True, null=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Local Authority area"
        verbose_name_plural = "Local Authority areas"
        ordering = ['la_area']

    def __str__ (self):
        return self.la_area

    def get_absolute_url(self):
        return reverse('lhn-detail', args=[str(self.id)])


    #### calc 2018 ####
    def projected_household_growth_2018(self):
        return Decimal((self.hp_2028 - self.hp_2018) * 1000)

    def adj_factor_2018(self):
        x = Decimal(self.med_aff_rat_2017)
        y = Decimal(4)
        z = Decimal(0.25)
        return (1 + (((x-y)/y)*z))

    def lhn_2018(self):
         x = Decimal(self.projected_household_growth_2018())
         y = Decimal(self.adj_factor_2018())
         return Decimal((x * y) / 10)

    #### calc 2019 ####
    def projected_household_growth_2019(self):
        return Decimal((self.hp_2029 - self.hp_2019) * 1000)

    def adj_factor_2019(self):
        x = Decimal(self.med_aff_rat_2018)
        y = Decimal(4)
        z = Decimal(0.25)
        return (1 + (((x-y)/y)*z))

    def lhn_2019(self):
         x = Decimal(self.projected_household_growth_2019())
         y = Decimal(self.adj_factor_2019())
         return Decimal((x * y) / 10)

    #### calc 2020 ####
    def projected_household_growth_2020(self):
        return Decimal((self.hp_2030 - self.hp_2020) * 1000)

    def adj_factor_2020(self):
        x = Decimal(self.med_aff_rat_2019)
        y = Decimal(4)
        z = Decimal(0.25)
        return (1 + (((x-y)/y)*z))

    def lhn_2020(self):
         x = Decimal(self.projected_household_growth_2020())
         y = Decimal(self.adj_factor_2020())
         return Decimal((x * y) / 10)


