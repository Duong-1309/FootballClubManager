from django.db import models

# Create your models here.
class DoiBong(models.Model):
    ma_doi_bong = models.AutoField(primary_key=True)
    ten = models.CharField(max_length=100)
    san_van_dong = models.CharField(max_length=100)
    nam_thanh_lap = models.IntegerField()

    class Meta:
        db_table = 'DoiBong'


class ThanhTichDoiBong(models.Model):
    ma_thanh_tich = models.AutoField(primary_key=True)
    doi_bong_id = models.ForeignKey(DoiBong, on_delete=models.CASCADE)
    ten_thanh_tich = models.CharField(max_length=255)
    nam_thanh_tich = models.IntegerField()
    mo_ta = models.TextField()

    class Meta:
        db_table = 'ThanhTichDoiBong'