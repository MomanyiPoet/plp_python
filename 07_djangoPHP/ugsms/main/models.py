from django.db import models

# Create your models here.
class about(models.Model):
    title = models.CharField(max_length=20)
    description = models.CharField(max_length=300)
    class Meta:
        db_table = 'tblpage'