from django.db import models

class Message(models.Model):
	parent = models.ForeignKey('Message', null=True)
	text = models.CharField('message text', max_length=5000)
	created = models.DateTimeField('created', auto_now_add=True)
	last_modified = models.DateTimeField('last modified', auto_now=True)

	def __unicode__(self):
		return self.text
