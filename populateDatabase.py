# Usage:
# python manage.py makemigrations
# python manage.py migrate
# python manage.py < populateDatabase.py

from conversations.models import Message
m = Message(text="This was a triumph")
m.save()
m2 = Message(text="I'm making a note here…", parent=m)
m2.save()
m3 = Message(text="Huge success", parent=m)
m3.save()
m4 = Message(text="It's hard to overstate my satisfaction", parent=m2)
m4.save()