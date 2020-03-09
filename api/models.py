from django.db import models
from django.utils import timezone

OPTIONS = [
    ('Severe', 'S'),
    ('Less Severe', 'LS'),
    ('Casual', 'C'),
]


# a case MUST have a catergory
class Category(models.Model):
    name = models.CharField(max_length=200, choices=OPTIONS)

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name


# the List of CASEs to report
class Report(models.Model):
    title = models.CharField(max_length=250)
    description = models.TextField()
    reported_time = models.TimeField(auto_now=timezone.now)
    date_reported = models.DateField(auto_now=True)
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, related_name='categories'
    )
    reporter = models.ForeignKey(
        'auth.User', on_delete=models.CASCADE, related_name='reporters'
    )

    class Meta:
        verbose_name_plural = 'Emergency Cases'
        ordering = ['-reported_time']

    def __str__(self):
        return f'{self.reporter} reported a case by {self.reported_time} under {self.category.name}'
