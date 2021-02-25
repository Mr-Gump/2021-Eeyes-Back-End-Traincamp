from django.db import models
from django.contrib.auth.models import User

# Create your models here.
from datetime import datetime


class Articles(models.Model):
    """
    文章
    """
    articleid = models.CharField(
        max_length=30, verbose_name='文章id', default='')
    article = models.CharField(max_length=30, verbose_name='文章内容', default='')
    createtime = models.DateTimeField(auto_now_add=True)
    # 第一次migrations需注释掉owner
    owner = models.ForeignKey(
        'auth.User', related_name='articles', on_delete=models.CASCADE , default='')

    class Meta:
        ordering = ['createtime']

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):

        super(Articles, self).save(*args, **kwargs)