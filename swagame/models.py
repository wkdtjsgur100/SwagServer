from __future__ import unicode_literals

from django.db import models
#for recoding time
from django.utils import timezone

class Login(models.Model):
	user_id = models.TextField()
	user_nickname = models.TextField()
	user_score = models.BigIntegerField(blank=True,null=True)
	user_signin_time = models.DateTimeField(default=timezone.now)
	connect_time = models.DateTimeField(blank=True,null=True)
	shutgame_time = models.DateTimeField(blank=True,null=True)
	lastplay_time = models.DateTimeField(blank=True,null=True)
	
	def updateConnectTime(self):
		self.connect_time = timezone.now()
		self.save()

	def updateShutGame(self):
		self.shutgame_time = timezone.now()
		self.save()

	def updateLastPlayTime(self):
		self.lastplay_time = timezone.now()
		self.save()

# Create your models here.
