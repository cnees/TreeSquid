from django.db import models
from django.contrib.auth.models import User

class Message(models.Model):
	user = models.ForeignKey(User)
	parent = models.ForeignKey('Message', null=True, related_name="children")
	root = models.ForeignKey('Message', null=True, related_name="descendants", related_query_name="children_of")
	text = models.CharField('message text', max_length=5000)
	topic = models.CharField('conversation topic', max_length=300, default="")
	created = models.DateTimeField('created', auto_now_add=True)
	last_modified = models.DateTimeField('last modified', auto_now=True)

	def __unicode__(self):
		return self.text

	def save(self):	

		super(Message, self).save()

		if self.parent:
			self.root_id = self.parent.root_id
			self.topic = self.parent.topic
		else:
			self.root_id = self.id
		
		super(Message, self).save()

