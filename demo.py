from conversations.models import Message
from django.contrib.auth.models import User

# Delete old entries
User.objects.all().delete()
Message.objects.all().delete()

## Uncomment this to delete the all messages created by "guest"
#Message.objects.filter(user=User.objects.get(username="guest")).delete()
#Message.objects.filter(user=User.objects.get(username="demo")).delete()
#
## Uncomment this to delete the existing user with username "guest" if you need to.
## Be sure to delete guest's messages FIRST if you want them gone.
#User.objects.get(username="guest").delete()
#User.objects.get(username="demo").delete()

u = User.objects.create_user('guest', 'guest@example.com', 'guest')
u.first_name = "Guest"
u.last_name = "User"
u.save()

u2 = User.objects.create_user('TreeSquid', 'treesquid@example.com', 'treesquid')
u2.first_name = "Team"
u2.last_name = "TreeSquid"
u2.save()

# Add a few users
user1 = User.objects.create_user('chris', 'chrisloechli@gmail.com', 'chrispassword')
user1.first_name = "Chris"
user1.last_name = "Loechli"
user1.save()

user2 = User.objects.create_user('clara', 'example@gmail.com', 'clarapassword')
user2.first_name = "Clara"
user2.last_name = "Nees"
user2.save()

user3 = User.objects.create_user('joe', 'joe@treesquid.com', 'joepassword')
user3.first_name = "Joe"
user3.last_name = "Pohlman"
user3.save()

user4 = User.objects.create_user('brendan', 'brendan@treesquid.com', 'brendanpassword')
user4.first_name = "Brendan"
user4.last_name = "Killalea"
user4.save()

b1 = Message(topic="Book Club", text="What should we read this month?", user=user1)
b1.save()
b2 = Message(text="Sci-fi!", parent=b1, user=u)
b2.save()
b3 = Message(text="Eh, how about something angsty with more symbolism than plot and an unsatisfactory ending?", parent=b2, user=user2)
b3.save()
b4 = Message(text="Ooh, fun! Misery is the best! Let's read something by Steinbeck!", parent=b3, user=user3)
b4.save()
b5 = Message(text="War and Peace!", parent=b3, user=user3)
b5.save()
b6 = Message(text="Staaaaaahhhhhhhp.", parent=b3, user=u)
b6.save()
b7 = Message(text="Dictionary, by Daniel Webster", parent=b1, user=user4)
b7.save()
b8 = Message(text="Diccionario de la lengua española - Edición del Tricentenario", parent=b7, user=user3)
b8.save()
b9 = Message(text="Even better", parent=b8, user=user4)
b9.save()
b10 = Message(text="Fantasy!", parent=b1, user=u)
b10.save()
b11 = Message(text="I QUIT.", parent=b8, user=u)
b11.save()
b12 = Message(text="How about Narnia?", parent=b10, user=user1)
b12.save()
n1 = Message(topic="Good Nerf Guns?", text="I'm looking for some advice on dart based ballistics.", user=user1)
n1.save()
n2 = Message(user=user2, parent=n1, text="Dude, totally depends on what you're using for? We looking for a casual game of sissy darts or you wanna deal some real dammage?")
n2.save()
n3 = Message(user=user3, parent=n1, text="Maverick all the way")
n3.save()
n4 = Message(user=user1, parent=n2, text="There's this academic researcher that needs to be put in his place, I'm looking to bring the pain!")
n4.save()
n5 = Message(user=user2, parent=n4, text="The RapidStrike CS-18 is gonna be the best choice for you, you nefarious guy you.")
n5.save()
n6 = Message(user=user1, parent=n5, text="Nice! He'll never see it coming!.")
n6.save()
n7 = Message(user=user4, parent=n4, text="Lol, you should just hack his website or something. The duck flies at midnight, amiright!?")
n7.save()
n7 = Message(user=user3, parent=n4, text="Hey man, be careful whatever you do. You'd be surprised at how easy it is to track someones actions even if they try to delete their search histories and flee the country.")
n7.save()
n8 = Message(user=user4, parent=n1, text="Why not just go all out and get an airsoft gun?")
n8.save()
n9 = Message(user=u, parent=n1, text="Nerf N-strike Rhino Fire")
n9.save()
n10 = Message(user=user1, parent=n1, text="I've heard good things about the Elite Rampage, thoughts?")
n10.save()

# Add some messages
n20 = Message(topic="Best EECS class?", text="I have a friend who wants recommendations for great classes!", user=user2)
n20.save()
n21 = Message(user=user1, parent=n20, text="EECS 388 was really fun!")
n21.save()
n22 = Message(user=user3, parent=n20, text="EECS 493 is great if you like front-end / user-experience material.")
n22.save()
n23 = Message(user=user4, parent=n22, text="I took 493, it was a class.")
n23.save()


m = Message(text="Welcome!", user=u2, topic="This is TreeSquid")
m.save()
m16 = Message(text="About", user=u2, parent=m)
m16.save()
m17 = Message(text="TreeSquid is a nonlinear messaging platform. Conversations grow as trees.", user=u2, parent=m16)
m17.save()
m18 = Message(text="TreeSquid is one of the many names we proposed", user=u2, parent=m16)
m18.save()
m19 = Message(text="Built by Chris Loechli, Joe Pohlman, Brendan Killalea, and Clara Nees", user=u2, parent=m16)
m19.save()
m12 = Message(text="EECS 493, Fall 2015", user=u2, parent=m19)
m12.save()
m1 = Message(text="How to", user=u2, parent=m)
m1.save()
m2 = Message(text="Navigate", user=u2, parent=m1)
m2.save()
m3 = Message(text="Zoom", user=u2, parent=m2)
m3.save()
m4 = Message(text="Use two-finger or pinch zooming on a trackpad.", user=u2, parent=m3)
m4.save()
m5 = Message(text="Use the icons in the top left to zoom in and out", user=u2, parent=m3)
m5.save()
m6 = Message(text="Pan", user=u2, parent=m2)
m6.save()
m61 = Message(text="Click and drag the background to pan", user=u2, parent=m6)
m61.save()
m62 = Message(text="On a Mac trackpad, you can use three fingers to pan", user=u2, parent=m6)
m62.save()
m7 = Message(text="Pan with three fingers on a Mac trackpad", user=u2, parent=m6)
m7.save()
m7 = Message(text="Click and drag to pan", user=u2, parent=m6)
m7.save()
m8 = Message(text="Post", user=u2, parent=m)
m8.save()
m9 = Message(text="Click any message to reply to it.", user=u2, parent=m8)
m9.save()
m10 = Message(text="You can click and drag the bottom right corner of the text box as you type your reply to change its size.", user=u2, parent=m9)
m10.save()
m11 = Message(text="Create new conversations with the ''New Conversation'' button in the top left.", user=u2, parent=m8)
m11.save()
m12 = Message(text="See replies", user=u2, parent=m1)
m12.save()
m13 = Message(text="The left bar shows conversations you're part of.", user=u2, parent=m12)
m13.save()
m14 = Message(text="Click on a message in the tree to see its full contents.", user=u2, parent=m12)
m14.save()
m15 = Message(text="Replies from different users have different border colors.", user=u2, parent=m12)
m15.save()

# Chris: I moved a few things down here to change the oder in which the conversations
# are shown for the guest user. I did this to accomodate the user tests I wrote. The
# originals are commented out above.
m_chris_made1 = Message(text="This is what a reply made by you would look like", user=u, parent=m9)
m_chris_made1.save()
b11 = Message(text="I've already read all of them.", parent=b12, user=u)
b11.save()




# u = User.objects.create_user('guest', 'guest@example.com', 'guest')
# u.first_name = "Guest"
# u.last_name = "User"
# u.save()

# u2 = User.objects.create_user('demo', 'demo@example.com', 'demopassword')
# u2.first_name = "Demo"
# u2.last_name = "User"
# u.save()

# # Add a few users
# user1 = User.objects.create_user('chris', 'chrisloechli@gmail.com', 'chrispassword')
# user1.first_name = "Chris"
# user1.last_name = "Loechli"
# user1.save()

# user2 = User.objects.create_user('clara', 'example@gmail.com', 'clarapassword')
# user2.first_name = "Clara"
# user2.last_name = "Nees"
# user2.save()

# user3 = User.objects.create_user('joe', 'joe@treesquid.com', 'joepassword')
# user3.first_name = "Joe"
# user3.last_name = "Pohlman"
# user3.save()

# user4 = User.objects.create_user('brendan', 'brendan@treesquid.com', 'brendanpassword')
# user4.first_name = "Brendan"
# user4.last_name = "Killalea"
# user4.save()

# b1 = Message(topic="Book Club", text="What should we read this month?", user=user1)
# b1.save()
# b2 = Message(text="Sci-fi!", parent=b1, user=u)
# b2.save()
# b3 = Message(text="Eh, how about something angsty with more symbolism than plot and an unsatisfactory ending?", parent=b2, user=user2)
# b3.save()
# b4 = Message(text="Ooh, fun! Misery is the best! Let's read something by Steinbeck!", parent=b3, user=user3)
# b4.save()
# b5 = Message(text="War and Peace!", parent=b3, user=user3)
# b5.save()
# b6 = Message(text="Staaaaaahhhhhhhp.", parent=b3, user=u)
# b6.save()
# b7 = Message(text="Dictionary, by Daniel Webster", parent=b1, user=user4)
# b7.save()
# b8 = Message(text="Diccionario de la lengua española - Edición del Tricentenario", parent=b7, user=user3)
# b8.save()
# b9 = Message(text="Even better", parent=b8, user=user4)
# b9.save()
# b10 = Message(text="Fantasy!", parent=b1, user=u)
# b10.save()
# b11 = Message(text="I QUIT.", parent=b8, user=u)
# b11.save()
# b12 = Message(text="How about Narnia?", parent=b10, user=user1)
# b12.save()
# n1 = Message(topic="Good Nerf Guns?", text="I'm looking for some advice on dart based ballistics.", user=user1)
# n1.save()
# n2 = Message(user=user2, parent=n1, text="Dude, totally depends on what you're using for? We looking for a casual game of sissy darts or you wanna deal some real dammage?")
# n2.save()
# n3 = Message(user=user3, parent=n1, text="Maverick all the way")
# n3.save()
# n4 = Message(user=user1, parent=n2, text="There's this academic researcher that needs to be put in his place, I'm looking to bring the pain!")
# n4.save()
# n5 = Message(user=user2, parent=n4, text="The RapidStrike CS-18 is gonna be the best choice for you, you nefarious guy you.")
# n5.save()
# n6 = Message(user=user1, parent=n5, text="Nice! He'll never see it coming!.")
# n6.save()
# n7 = Message(user=user4, parent=n4, text="Lol, you should just hack his website or something. The duck flies at midnight, amiright!?")
# n7.save()
# n7 = Message(user=user3, parent=n4, text="Hey man, be careful whatever you do. You'd be surprised at how easy it is to track someones actions even if they try to delete their search histories and flee the country.")
# n7.save()
# n8 = Message(user=user4, parent=n1, text="Why not just go all out and get an airsoft gun?")
# n8.save()
# n9 = Message(user=u, parent=n1, text="Nerf N-strike Rhino Fire")
# n9.save()
# n10 = Message(user=user1, parent=n1, text="I've heard good things about the Elite Rampage, thoughts?")
# n10.save()

# # Add some messages
# n20 = Message(topic="Best EECS class?", text="I have a friend who wants recommendations for great classes!", user=user2)
# n20.save()
# n21 = Message(user=user1, parent=n20, text="EECS 388 was really fun!")
# n21.save()
# n22 = Message(user=user3, parent=n20, text="EECS 493 is great if you like front-end / user-experience material.")
# n22.save()
# n23 = Message(user=user4, parent=n22, text="I took 493, it was a class.")
# n23.save()


# m = Message(text="Welcome!", user=u, topic="This is TreeSquid")
# m.save()
# m16 = Message(text="About", user=u, parent=m)
# m16.save()
# m17 = Message(text="TreeSquid is a nonlinear messaging platform. Conversations grow as trees.", user=u, parent=m16)
# m17.save()
# m18 = Message(text="TreeSquid is one of the many names we proposed", user=u, parent=m16)
# m18.save()
# m19 = Message(text="Built by Chris Loechli, Joe Pohlman, Brendan Killalea, and Clara Nees", user=u, parent=m16)
# m19.save()
# m12 = Message(text="EECS 493, Fall 2015", user=u, parent=m19)
# m12.save()
# m1 = Message(text="How to", user=u, parent=m)
# m1.save()
# m2 = Message(text="Navigate", user=u, parent=m1)
# m2.save()
# m3 = Message(text="Zoom", user=u, parent=m2)
# m3.save()
# m4 = Message(text="Use two-finger or pinch zooming on a trackpad.", user=u, parent=m3)
# m4.save()
# m5 = Message(text="Use the icons in the top left to zoom in and out", user=u, parent=m3)
# m5.save()
# m6 = Message(text="Pan", user=u, parent=m2)
# m6.save()
# m61 = Message(text="Click and drag the background to pan", user=u, parent=m6)
# m61.save()
# m62 = Message(text="On a Mac trackpad, you can use three fingers to pan", user=u, parent=m6)
# m62.save()
# m7 = Message(text="Pan with three fingers on a Mac trackpad", user=u, parent=m6)
# m7.save()
# m7 = Message(text="Click and drag to pan", user=u, parent=m6)
# m7.save()
# m8 = Message(text="Post", user=u, parent=m)
# m8.save()
# m9 = Message(text="Click any message to reply to it.", user=u, parent=m8)
# m9.save()
# m10 = Message(text="You can click and drag the bottom right corner of the text box as you type your reply to change its size.", user=u, parent=m9)
# m10.save()
# m11 = Message(text="Create new conversations with the ''New Conversation'' button in the top left.", user=u, parent=m8)
# m11.save()
# m12 = Message(text="See replies", user=u, parent=m1)
# m12.save()
# m13 = Message(text="The left bar shows conversations you're part of.", user=u, parent=m12)
# m13.save()
# m14 = Message(text="Click on a message in the tree to see its full contents.", user=u, parent=m12)
# m14.save()
# m15 = Message(text="Replies from different users have different border colors.", user=u, parent=m12)
# m15.save()
# m01 = Message(text="This is TreeSquid!", user=u, parent=m)
# m01.save()