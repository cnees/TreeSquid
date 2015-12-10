# Usage:
# python manage.py makemigrations
# python manage.py migrate
# python manage.py < populateDatabase.py

from conversations.models import Message
m = Message(text="This was a triumph", user_id=1)
m.save()
m2 = Message(text="I'm making a note here…", parent=m, user_id=1)
m2.save()
m3 = Message(text="Huge success", parent=m, user_id=1)
m3.save()
m4 = Message(text="It's hard to overstate my satisfaction", parent=m2, user_id=1)
m4.save()