from django import forms
from .models import NoticeBoard, FarmerIssue

class NoticeBoardForm(forms.ModelForm):
    class Meta:
        model = NoticeBoard
        fields = "__all__"

class FarmerIssueForm(forms.ModelForm):
    class Meta:
        model = FarmerIssue
        fields = ("title", "description", "issues", "location_name", )
