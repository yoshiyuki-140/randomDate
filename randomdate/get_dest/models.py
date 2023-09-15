from django.db import models

# Create your models here.


class URLs(models.Model):
    # QRコードから読み込んだurlの長さの最大値はわからないので、とりあえず256を最大値にしてる
    # バグ起きたらそのつど編集してね
    url = models.CharField(max_length=256)


class Dest(models.Model):
    url = models.ForeignKey(URLs, on_delete=models.CASCADE)
    dest = models.CharField(max_length=256)
