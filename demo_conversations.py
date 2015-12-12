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

user2 = User.objects.create_user('clara', 'claracc@gmail.com', 'clarapassword')
user2.first_name = "Clara"
user2.last_name = "Ness"
user2.save()

user3 = User.objects.create_user('joe', 'joe@treesquid.com', 'joepassword')
user3.first_name = "Joe"
user3.last_name = "Pohlman"
user3.save()

user4 = User.objects.create_user('brendan', 'brendan@treesquid.com', 'brendanpassword')
user4.first_name = "Brendan"
user4.last_name = "Killalea"
user4.save()

m1 = Message(topic="Good Nerf Guns?", text="I'm looking for some advice on dart based ballistics.", user=user1)
m1.save()
m2 = Message(user=user2, parent=m1, text="Dude, totally depends on what you're using for? We looking for a casual game of sissy darts or you wanna deal some real dammage?")
m2.save()
m3 = Message(user=user3, parent=m1, text="Maverick all the way")
m3.save()
m4 = Message(user=user1, parent=m2, text="There's this academic researcher that needs to be put in his place, I'm looking to bring the pain!")
m4.save()
m5 = Message(user=user2, parent=m4, text="The RapidStrike CS-18 is gonna be the best choice for you, you nefarious guy you.")
m5.save()
m6 = Message(user=user1, parent=m5, text="Nice! He'll never see it coming!.")
m6.save()
m7 = Message(user=user4, parent=m4, text="Lol, you should just hack his website or something. The duck flies at midnight, amiright!?")
m7.save()
m7 = Message(user=user3, parent=m4, text="Hey man, be careful whatever you do. You'd be surprised at how easy it is to track someones actions even if they try to delete their search histories and flee the country.")
m7.save()
m8 = Message(user=user4, parent=m1, text="Why not just go all out and get an airsoft gun?")
m8.save()
m9 = Message(user=user3, parent=m1, text="Nerf N-strike Rhino Fire")
m9.save()
m10 = Message(user=user1, parent=m1, text="I've heard good things about the Elite Rampage, thoughts?")
m10.save()
m10.save()

# Add some messages
# Chris shouldn't be able to see any of these messages.
m11 = Message(topic="No Chris allowed", text="Guys, let's have a conversation without Chris.", user=user2)
m11.save()
m12 = Message(user=user3, parent=m11, text="Yeah, that guy sucks. He won't stop asking me which classes I'm taking next semester...")
m12.save()
m13 = Message(user=user4, parent=m11, text="That guy drinks way too much caffeine.")
m13.save()

# Add some messages
# This conversation should be the one that shows up as the most recent conversation for everyone
m20 = Message(topic="Best EECS class?", text="I have one semester left, so I'm looking for great classes!", user=user2)
m20.save()
m21 = Message(user=user1, parent=m20, text="EECS 388 was delightful!")
m21.save()
m22 = Message(user=user3, parent=m20, text="EECS 493 is great if you like front-end / user-experience material.")
m22.save()
m23 = Message(user=user4, parent=m22, text="I took 493, it was a class.")
m23.save()