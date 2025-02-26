from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name


class Service(models.Model):
    name = models.CharField(max_length=255)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="services")
    base_price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    is_active = models.BooleanField(default=True)
    is_deleted = models.BooleanField(default=False)

    def __str__(self):
        return self.name

class ServiceField(models.Model):
    service = models.ForeignKey(Service, on_delete=models.CASCADE, related_name="fields")
    value = models.CharField(max_length=350)

    def __str__(self):
        return f"{self.service.name} - {self.value}"  # Fix: Use service.name instead of service.value

class ConsultationRequest(models.Model):
    service = models.ForeignKey(Service, on_delete=models.SET_NULL, null=True, blank=True, related_name="consultations")
    name = models.CharField(max_length=255)
    email = models.EmailField()
    mobile_number = models.CharField(max_length=15)
    city_or_pincode = models.CharField(max_length=100, null=True, blank=True)
    whatsapp_opt_in = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.service.name if self.service else 'General Inquiry'}"