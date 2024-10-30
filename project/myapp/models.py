from django.db import models


class Subnet(models.Model):
    subnet = models.CharField(max_length=18)
    company_id = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "subnets"

    def __str__(self):
        return self.subnet
