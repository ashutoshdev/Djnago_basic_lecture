from django.db.models import *


class About(Model):
    title = TextField(max_length=500, blank=False, null=False)
    content = TextField(max_length=500, blank=False, null=False)
    status = BooleanField(default=False)
    created = DateTimeField(auto_now_add=True)
    updated = DateTimeField(auto_now=True)



