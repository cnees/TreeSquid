from conversations.models import Message
from conversations.models import User

# Uncomment this to delete the all messages created by "guest"
#Message.objects.filter(user=User.objects.get(username="guest")).delete()

# Uncomment this to delete the existing user with username "guest" if you need to.
# Be sure to delete guest's messages FIRST if you want them gone.
#User.objects.get(username="guest").delete()

u = User.objects.create_user('guest', 'guest@example.com', 'guest')
u.first_name = "Guest"
u.last_name = "User"
u.save()
m = Message(text="Welcome!", user=u)
m.save()

m01 = Message(text="This is TreeSquid!", user=u, parent=m)
m01.save()

m16 = Message(text="About", user=u, parent=m)
m16.save()
m17 = Message(text="TreeSquid is a nonlinear messaging platform. Conversations grow as trees.", user=u, parent=m16)
m17.save()
m18 = Message(text="TreeSquid is one of the many names we proposed", user=u, parent=m16)
m18.save()
m19 = Message(text="Built by Chris Loechli, Joe Pohlman, Brendan Killalea, and Clara Nees", user=u, parent=m16)
m19.save()
m12 = Message(text="EECS 493, Fall 2015", user=u, parent=m19)
m12.save()

m1 = Message(text="How to", user=u, parent=m)
m1.save()
m2 = Message(text="Navigate", user=u, parent=m1)
m2.save()
m3 = Message(text="Zoom", user=u, parent=m2)
m3.save()
m4 = Message(text="Use two-finger or pinch zooming on a trackpad.", user=u, parent=m3)
m4.save()
m5 = Message(text="Use the icons in the top left to zoom in and out", user=u, parent=m3)
m5.save()
m6 = Message(text="Pan", user=u, parent=m2)
m6.save()
m61 = Message(text="Click and drag the background to pan", user=u, parent=m6)
m61.save()
m62 = Message(text="On a Mac trackpad, you can use three fingers to pan", user=u, parent=m6)
m62.save()
m7 = Message(text="Pan with three fingers on a Mac trackpad", user=u, parent=m6)
m.save()
m7 = Message(text="Click and drag to pan", user=u, parent=m6)
m.save()
m8 = Message(text="Post", user=u, parent=m)
m8.save()
m9 = Message(text="Click any message to reply to it.", user=u, parent=m8)
m9.save()
m10 = Message(text="You can click and drag the bottom right corner of the text box as you type your reply to change its size.", user=u, parent=m9)
m10.save()
m11 = Message(text="Create new conversations with the ''New Conversation'' button in the top left.", user=u, parent=m8)
m11.save()
m12 = Message(text="See replies", user=u, parent=m1)
m12.save()
m13 = Message(text="The left bar shows conversations you're part of.", user=u, parent=m12)
m13.save()
m14 = Message(text="Click on a message in the tree to see its full contents.", user=u, parent=m12)
m14.save()
m15 = Message(text="Replies from different users have different border colors.", user=u, parent=m12)
m15.save()