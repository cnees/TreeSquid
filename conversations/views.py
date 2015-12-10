from django.shortcuts import get_object_or_404, render
from django.db.models import F
from django_ajax.decorators import ajax
import logging
logging.basicConfig()
from .models import Message
import json
import urlparse
# from .models import Root

# def index(request):
# 	latest_root_list = Root.objects.order_by('-pub_date')[:5]
# 	context = {'latest_root_list': latest_root_list}
# 	return render(request, 'conversations/index.html', context)

# def root(request, root_id):
# 	root = get_object_or_404(Root, pk=root_id)
# 	return render(request, 'conversations/root.html', {'root': root})

# def replies(request, root_id):
#     response = "You're looking at the replies of root %s."
#     return HttpResponse(response % root_id)

def index(request):
	latest_root_list = Message.objects.filter(root_id=F('id')).order_by('-last_modified')[:5]
	context = {'latest_root_list': latest_root_list}
	return render(request, 'conversations/index.html', context)

def root(request, root_id):
	root = get_object_or_404(Message, pk=root_id)
	return render(request, 'conversations/root.html', {'root': root})

@ajax
def add_reply(request, root_id):
	if request.method == 'POST':
		parse = urlparse.parse_qs(request.body)
		node = parse['node'][0]
		message = parse['message'][0]
		print node
		print message
		parent = Message.objects.get(id=node)
		# user_id = request.user.id
		# reply = Message(text=message, parent=parent, root=parent.root, user_id=user_id)
		reply = Message(text=message, parent=parent, root=parent.root, user_id=1)
		reply.save()
		print reply
		return {'id': reply.id, 'text': reply.text, 'parent_id': parent.id}