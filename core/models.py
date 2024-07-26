from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.db import models


class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name


class Retreat(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    date = models.DateTimeField()
    location = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    type = models.CharField(max_length=100)
    condition = models.CharField(max_length=100)
    image = models.URLField()
    tags = models.ManyToManyField(Tag, related_name='retreats')
    duration = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    retreat = models.ForeignKey(Retreat, on_delete=models.CASCADE)
    payment_details = models.CharField(max_length=200)
    booking_date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if Booking.objects.filter(retreat=self.retreat, user=self.user).exists():
            raise ValidationError("You have already booked this retreat.")
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Booking of {self.retreat.title} by {self.user.username}"