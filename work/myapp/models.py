from django.db import models
from django.core.exceptions import ValidationError
import ipaddress


class Subnet(models.Model):
    subnet = models.CharField(max_length=18)
    company_id = models.IntegerField()
    created_at = models.DateTimeField(
        auto_now_add=True
    )  # Автоматическое время создания

    class Meta:
        db_table = "subnets"

    def __str__(self):
        return self.subnet

    def save(self, *args, **kwargs):
        try:
            ipaddress.IPv4Network(self.subnet, strict=False)
        except ValueError:
            raise ValidationError(
                "Введите корректное значение IP-адреса с маской в формате CIDR"
            )
        super().save(*args, **kwargs)
