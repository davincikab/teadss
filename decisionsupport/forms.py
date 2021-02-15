from django import forms
from .models import NoticeBoard

class NoticeBoardForm(forms.ModelForm):
    class Meta:
        model = NoticeBoard
        fields = "__all__"