from django.contrib import admin

# 3rd party


# local code
from .models import NoticeBoard, FarmerIssue

admin.site.register(NoticeBoard)
admin.site.register(FarmerIssue)
