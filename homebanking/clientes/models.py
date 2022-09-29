from django.db import models


class Cliente(models.Model):
    customer_id = models.AutoField(primary_key=True, blank=True)
    customer_name = models.TextField()
    customer_surname = models.TextField()
    # Field name made lowercase.
    customer_dni = models.TextField(db_column='customer_DNI')
    dob = models.IntegerField()
    branch_id = models.IntegerField()
    customer_type_id = models.IntegerField(blank=True, null=True)
    address_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cliente'
