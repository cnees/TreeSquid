from django.contrib.auth.models import User
from conversations.models import Message

# Delete old entries
User.objects.all().delete()
Message.objects.all().delete()

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
n9 = Message(user=user3, parent=n1, text="Nerf N-strike Rhino Fire")
n9.save()
n10 = Message(user=user1, parent=n1, text="I've heard good things about the Elite Rampage, thoughts?")
n10.save()
n10.save()

# Add some messages
# Chris shouldn't be able to see any of these messages.
n11 = Message(topic="No Chris allowed", text="Guys, let's have a conversation without Chris.", user=user2)
n11.save()
n12 = Message(user=user3, parent=n11, text="Yeah, that guy sucks. He won't stop asking me which classes I'm taking next semester...")
n12.save()
n13 = Message(user=user4, parent=n11, text="That guy drinks way too much caffeine.")
n13.save()

# Add some messages
n20 = Message(topic="Best EECS class?", text="I have a friend who wants recommendations for great classes!", user=user2)
n20.save()
n21 = Message(user=user1, parent=n20, text="EECS 388 was really fun!")
n21.save()
n22 = Message(user=user3, parent=n20, text="EECS 493 is great if you like front-end / user-experience material.")
n22.save()
n23 = Message(user=user4, parent=n22, text="I took 493, it was a class.")
n23.save()

# Add some messages
# This conversation should be the one that shows up as the most recent conversation for everyone
n30 = Message(topic="Most recent messages", text="Chris's most recent message at time of initialization", user=user1)
n30.save()
n31 = Message(user=user2, parent=n30, text="Clara's most recent message at time of initialization")
n31.save()
n32 = Message(user=user3, parent=n30, text="Joe's most recent message at time of initialization")
n32.save()
n33 = Message(user=user4, parent=n30, text="Brendan's most recent message at time of initialization")
n33.save()

