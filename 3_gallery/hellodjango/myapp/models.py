# -*- coding: utf-8 -*-
from django.db import models


class MyImage(models.Model):
    image = models.ImageField(upload_to='download')
    code = models.CharField(max_length=100)
    original_name = models.CharField(max_length=255)
    uploaded = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return 'original name:{0}, new name:{1}, uploaded:{2})'.format(
            self.original_name,
            self.code,
            self.uploaded)
