from django.db import models


class Data2018(models.Model):
    tahun = models.CharField(max_length=4)
    wilayah = models.CharField(max_length=100)
    jumlah_bayi_lahir = models.IntegerField()
    kondisi_bayi = models.CharField(max_length=100)
    jumlah = models.IntegerField()


class Data2019(models.Model):
    tahun = models.CharField(max_length=4)
    wilayah = models.CharField(max_length=100)
    jumlah_bayi_lahir = models.IntegerField()
    kondisi_bayi = models.CharField(max_length=100)
    jumlah = models.IntegerField()


class Data2020(models.Model):
    tahun = models.CharField(max_length=4)
    wilayah = models.CharField(max_length=100)
    jumlah_bayi_lahir = models.IntegerField()
    kondisi_bayi = models.CharField(max_length=100)
    jumlah = models.IntegerField()
