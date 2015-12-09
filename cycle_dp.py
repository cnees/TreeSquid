from django.contrib.auth.models import User
from conversations.models import Message

# Delete old entries
User.objects.all().delete()
Message.objects.all().delete()

# Add a few users
user1 = User.objects.create_user('chris', 'chris@treesquid.com', 'chrispassword')
user1.first_name = "Chris"
user1.last_name = "Loechli"
user1.save()

user2 = User.objects.create_user('clara', 'clara@treesquid.com', 'clarapassword')
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

# Add some messages
m1 = Message(text="ROOT 1", user=user1)
m1.save()
m2 = Message(text="1st CHILD OF ROOT 1", user=user2, parent=m1)
m2.save()
m3 = Message(text="2nd CHILD OF ROOT 1", user=user1, parent=m1)
m3.save()
m4 = Message(text="A descendant of root 1", user=user1, parent=m2)
m4.save()
m5 = Message(text="Another descendant of root 1", user=user2, parent=m3)
m5.save()
m6 = Message(text="Yet another descendant of root 1", user=user2, parent=m2)
m6.save()

m7 = Message(text="ROOT2", user=user4)
m7.save()