#coding:utf-8
from django.db import models

class PB_Forum(models.Model):
	forum_id = models.IntegerField(max_length=10, primary_key=True, default=0, unique=True)
	forum_name = models.CharField(max_length=255, blank=True)
	forum_about = models.CharField(max_length=800, blank=True)

	def __unicode__(self):
		return self.forum_name, self.forum_about
	class Meta:
		db_table = u'pb_forum'
