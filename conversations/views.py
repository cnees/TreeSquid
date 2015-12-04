from django.shortcuts import get_object_or_404, render

from .models import Message
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
	latest_root_list = Message.objects.exclude(parent=True).order_by('-last_modified')[:5]
	context = {'latest_root_list': latest_root_list}
	return render(request, 'conversations/index.html', context)

def root(request, root_id):
	root = get_object_or_404(Message, pk=root_id)
	return render(request, 'conversations/root.html', {'root': root})

def replies(request, root_id):
    response = "You're looking at the replies of root %s."
    return HttpResponse(response % root_id)