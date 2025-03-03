# lost_and_found_app/forms.py

from django import forms
from django.core.exceptions import ValidationError
from .models import Item


class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ['title', 'description', 'category', 'location', 'status']
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter title'
            }),
            'description': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 5,
                'placeholder': 'Enter description'
            }),
            'category': forms.Select(attrs={'class': 'form-control'}),
            'location': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter location'
            }),
            'status': forms.Select(attrs={'class': 'form-control'}),
        }
        error_messages = {
            'title': {
                'required': "Title is required.",
                'max_length': "Title is too long."
            },
            'description': {
                'required': "Please provide a description."
            }
        }

    # Валидация отдельного поля: заголовок должен содержать минимум 5 символов
    def clean_title(self):
        title = self.cleaned_data.get('title')
        if title and len(title) < 5:
            raise ValidationError("Title must be at least 5 characters long.")
        return title

    # Общая валидация формы: для найденных предметов обязательное наличие описания
    def clean(self):
        cleaned_data = super().clean()
        status = cleaned_data.get('status')
        description = cleaned_data.get('description')
        if status == 'found' and (not description or description.strip() == ''):
            self.add_error('description', "Please provide additional details for found items.")
        return cleaned_data


# Дополнительная форма для поиска (если понадобится более сложная логика)
class ItemSearchForm(forms.Form):
    q = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Search items...'
        })
    )
