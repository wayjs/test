from django.db import models

# Create your models here.


class Consumer(models.Model):
    username = models.CharField(max_length=32)
    user_password = models.CharField(max_length=32)
    user_type = models.IntegerField()
    user_phone = models.IntegerField()


class Seed(models.Model):
    seed_num = models.CharField(max_length=20)
    seed_name = models.CharField(max_length=20)
    ke_name = models.CharField(max_length=20, null=True,blank=True)
    shu_name = models.CharField(max_length=20, null=True,blank=True)
    ya_name = models.CharField(max_length=20, null=True,blank=True)
    seed_image = models.CharField(max_length=60, null=True,blank=True)
    character = models.CharField(max_length=50, null=True,blank=True)
    main_use = models.CharField(max_length=30, null=True,blank=True)
    climate = models.CharField(max_length=30, null=True,blank=True)
    live = models.TextField(null=True,blank=True)
    flower = models.CharField(max_length=40, null=True,blank=True)
    feature = models.TextField(null=True,blank=True)
    seed_use = models.TextField(null=True,blank=True)
    watch_place = models.CharField(max_length=50, null=True,blank=True)
    breed = models.CharField(max_length=30, null=True,blank=True)
    grow_year = models.CharField(max_length=20, null=True,blank=True)
    save_year = models.CharField(max_length=20, null=True,blank=True)
    altitude = models.CharField(max_length=10, null=True,blank=True)
    podu = models.CharField(max_length=20, null=True,blank=True)
    poxiang = models.CharField(max_length=20, null=True,blank=True)
    soil_type = models.CharField(max_length=30, null=True,blank=True)
    gps_x = models.CharField(max_length=30, null=True,blank=True)
    gps_y = models.CharField(max_length=30, null=True,blank=True)
    status = models.IntegerField(null=True,blank=True)
    auditor = models.CharField(max_length=20, null=True,blank=True)




