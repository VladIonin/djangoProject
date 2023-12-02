from .models import Card
from django.forms import ModelForm, TextInput, FileInput


class CardForm(ModelForm):
    class Meta:
        model = Card
        fields = ["title", "photo"]
        widgets = {
            "title": TextInput(attrs={
                "type": "text",
                "maxlength": "50",
                "class": "form-control",
                "id": "title"
                }),
            "photo": FileInput(attrs={
                "type": "file",
                "class": "form-control",
                "id": "photo"
            })
        }
