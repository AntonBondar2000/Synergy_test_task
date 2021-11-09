from django.db import models


class Occupation(models.Model):
    name = models.CharField(
        max_length=200
    )
    company_name = models.CharField(
        max_length=100
    )
    position_name = models.CharField(
        max_length=100
    )
    hire_date = models.DateField()
    fire_date = models.DateField(
        blank=True,
        null=True
    )
    salary = models.IntegerField(
        "Salary(rub)"
    )
    fraction = models.IntegerField(
        "Fraction(%)"
    )
    base = models.IntegerField()
    advance = models.IntegerField()
    by_hours = models.BooleanField()

    class Meta:
        verbose_name = "Occupation"
        verbose_name_plural = "Occupation"
        ordering = ['name']

    def __str__(self):
        return '{}({})'.format(self.name, self.company_name)
