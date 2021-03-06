from __future__ import unicode_literals
from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

class Portal(models.Model):
    portal_id = models.AutoField(primary_key=True)
    portal_keyword = models.CharField('KEYWORD', max_length=100, blank=True)
    portal_icons = models.IntegerField(default=0)
    portal_nouns = models.IntegerField(default=0)
    portal_chars = models.IntegerField(default=0)
    portal_imgexifs = models.IntegerField(null=False, default=0)
    class Meta:
        verbose_name = 'portal'  # 이 이름을 이용해서 표시 가능
        verbose_name_plural = 'portal'
        db_table = 'portal'

    def __str__(self):
        return self.chart_id

    # def get_absolute_url(self):
    #     return reverse('chart:post_detail', args=(self.slug,))
    #     # return reverse('blog:post_detail', kwargs={'slug': self.slug})
