from django.db import models

class Root(models.Model):
    root_text = models.CharField(max_length=500)
    pub_date = models.DateTimeField('date published')

    def __unicode__(self):
    	return self.root_text

class Reply(models.Model):
	root = models.ForeignKey(Root)
	reply_text = models.CharField(max_length=500)
	pub_date = models.DateTimeField('date published')

	def __unicode__(self):
		return self.reply_text

class Message(models.Model):
	parent = models.ForeignKey('Message', null=True)
	text = models.CharField('message text', max_length=5000)
	created = models.DateTimeField('created', auto_now_add=True)
	last_modified = models.DateTimeField('last modified', auto_now=True)

	def __unicode__(self):
		return self.text
