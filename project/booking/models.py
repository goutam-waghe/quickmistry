from django.db import models
from django.conf import settings
from serviceCategory.models import ServiceCategory

class Booking(models.Model):
    customer = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="customer_bookings",
        limit_choices_to={'role': 'customer'}
    )
    worker = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="worker_bookings",
        limit_choices_to={'role': 'worker'}
    )

    # Service and schedule
    service_category = models.ForeignKey(ServiceCategory, on_delete=models.SET_NULL, null=True)
    scheduled_date = models.DateTimeField()
    description = models.TextField(blank=True, null=True)


    STATUS_PENDING = 'pending'
    STATUS_ACCEPTED = 'accepted'
    STATUS_ONGOING = 'ongoing'
    STATUS_COMPLETED = 'completed'
    STATUS_CANCELED = 'canceled'

    STATUS_CHOICES = [
        (STATUS_PENDING, 'Pending'),
        (STATUS_ACCEPTED, 'Accepted'),
        (STATUS_ONGOING, 'Ongoing'),
        (STATUS_COMPLETED, 'Completed'),
        (STATUS_CANCELED, 'Canceled'),
    ]
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default=STATUS_PENDING)

    # Payment (optional for now)
    is_paid = models.BooleanField(default=False)
    amount = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)


    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.customer.name} → {self.worker.name} ({self.service_category.name}) on {self.scheduled_date.strftime('%d-%b-%Y %H:%M')}"

    class Meta:
        ordering = ['-scheduled_date']
