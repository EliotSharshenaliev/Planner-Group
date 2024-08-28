from django.db import models


class Months(models.Model):
    type = models.CharField(max_length=50)
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Месяц"
        verbose_name_plural = "Месяцы"


class TourItem(models.Model):
    months = models.ForeignKey(Months, related_name='items', on_delete=models.CASCADE)
    date_range = models.CharField(max_length=20)
    spots_total = models.PositiveIntegerField()
    price = models.CharField(max_length=20)
    spots_left = models.PositiveIntegerField()
    created_at = models.DateField()

    def __str__(self):
        return f"{self.date_range}"


class Tourists(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    status = models.CharField(max_length=20)
    tour_item = models.ForeignKey(TourItem, related_name='tourists', on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
