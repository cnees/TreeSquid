# -*- coding: utf-8 -*-

from django.shortcuts import get_object_or_404, render, render_to_response, redirect
from django.db.models import F
from django.template import RequestContext
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect, HttpResponse
from django_ajax.decorators import ajax
import logging
logging.basicConfig()
from .models import Message
import json
import urlparse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout

from conversations.forms import UserForm
from .models import Message

def index(request):
    context = {}

    # If the user is logged on, show the conversation to which they last contributed
    if request.user.is_authenticated():
        # Get the user's most recent message
        most_recent_message = Message.objects.filter(user_id=request.user.id).latest('id')

        # Send the user to the conversation containing their most recent message
        root_id = most_recent_message.root_id
        return redirect('conversation/' + str(root_id), root_id=root_id)

    # Else, serve the user the welcome page
    #return render(request, 'conversations/index.html')
    return redirect('login/')

def about(request):
    return render(request, 'conversations/about.html')

def register(request):
    # Like before, get the request's context.
    context = RequestContext(request)

    # A boolean value for telling the template whether the registration was successful.
    # Set to False initially. Code changes value to True when registration succeeds.
    registered = False

    # If it's a HTTP POST, we're interested in processing form data.
    if request.method == 'POST':
        # Attempt to grab information from the raw form information.
        user_form = UserForm(data=request.POST)

        if user_form.is_valid():
            # Save the user's form data to the database.
            user = user_form.save()

            # Now we hash the password with the set_password method.
            # Once hashed, we can update the user object.
            user.set_password(user.password)
            user.save()

            # Update our variable to tell the template registration was successful.
            registered = True

        # Invalid form - mistakes or something else?
        # Print problems to the terminal.
        # They'll also be shown to the user.
        # else:
            # print user_form.errors

    # Not a HTTP POST, so we render our form using two ModelForm instances.
    # These forms will be blank, ready for user input.
    else:
        user_form = UserForm()

    # Render the template depending on the context.
    return render_to_response(
            'conversations/register.html',
            {'user_form': user_form, 'registered': registered},
            context)

def user_login(request):
    # Like before, obtain the context for the user's request.
    context = RequestContext(request)

    # If the request is a HTTP POST, try to pull out the relevant information.
    if request.method == 'POST':
        # Gather the username and password provided by the user.
        # This information is obtained from the login form.
        username = request.POST['username']
        password = request.POST['password']

        # Use Django's machinery to attempt to see if the username/password
        # combination is valid - a User object is returned if it is.
        user = authenticate(username=username, password=password)

        # If we have a User object, the details are correct.
        # If None (Python's way of representing the absence of a value), no user
        # with matching credentials was found.
        if user:
            # Is the account active? It could have been disabled.
            if user.is_active:
                # If the account is valid and active, we can log the user in.
                # We'll send the user back to the homepage.
                login(request, user)
                return HttpResponseRedirect('/')
            else:
                # An inactive account was used - no logging in!
                return HttpResponse("Your TreeSquid account is disabled.")
        else:
            # Bad login details were provided. So we can't log the user in.
            # print "Invalid login details: {0}, {1}".format(username, password)
            return HttpResponse("Invalid login details supplied.")

    # The request is not a HTTP POST, so display the login form.
    # This scenario would most likely be a HTTP GET.
    else:
        # No context variables to pass to the template system, hence the
        # blank dictionary object...
        return render_to_response('conversations/login.html', {}, context)

@login_required
def root(request, root_id):
    # Get the root requested in the url
    root = get_object_or_404(Message, pk=root_id)

    # Get the most recent messages from the logged in user, but only most recent from
    # a given conversation (most recent message per root)
    seen_root_ids = []
    latest_message_list = [] 
    # Look at all messages by the logged in user, in order of last modified
    for m in Message.objects.filter(user_id=request.user.id).order_by('-last_modified'):
        # If the root for the current message has not been seen, add the message to the 
        # list and keep record the its root's id.
        if m.root_id not in seen_root_ids:
            seen_root_ids.append(m.root_id)
            latest_message_list.append(m)

    # TODO: Change the following line to return the list as "latest_message_list" 
    return render(request, 'conversations/root.html', {'latest_message_list': latest_message_list, 'root': root})
 
def filterText(input):
	return input.replace('"', r'\"').rstrip()

@ajax
def add_root(request):
  if request.method == 'POST':
    parse = urlparse.parse_qs(request.body)
    message = parse['message'][0]
    topic = parse['topic'][0]
    user_id = request.user.id
    reply = Message(text=filterText(message), user_id=user_id, topic=topic)
    reply.save()
    return {'id': reply.id, 'text': reply.text}

@ajax
def add_reply(request, root_id):
	if request.method == 'POST':
		parse = urlparse.parse_qs(request.body)
		node = parse['node'][0]
		message = parse['message'][0]
		parent = Message.objects.get(id=node)
		user_id = request.user.id
		reply = Message(
			text=filterText(message),
			parent=parent,
			root=parent.root,
			user_id=user_id)
		reply.save()
		return {'id': reply.id, 'text': reply.text, 'parent_id': parent.id}

# Use the login_required() decorator to ensure only those logged in can access the view.
@login_required
def user_logout(request):
    # Since we know the user is logged in, we can now just log them out.
    logout(request)

    # Take the user back to the homepage.
    return HttpResponseRedirect('/')






# Just some code that I'm keeping around for reference ~~ Chris
 # latest_root_list = Message.objects.filter(root_id=F('id')).order_by('-last_modified')[:5]
        # latest_root_list = users_recent_messages.filter(root_id=F('id')).order_by('-last_modified')[:5]
        # latest_root_list = Message.objects.filter(root_id=F('id')).order_by('-last_modified')[:5]
        # root_id = Message.objects.filter(root_id=F('id')).latest('id').id
