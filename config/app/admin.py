from django.contrib import admin
from django import forms

from .models import Menu


class MenuForm(forms.ModelForm):

    @staticmethod
    def get_choices():
        _choices = [(item.name, item.name) for item in Menu.objects.all()]
        _choices.append(('None', None))
        return tuple(_choices)

    def __init__(self, *args, **kwargs):
        super(MenuForm, self).__init__(*args, **kwargs)
        self.fields['parent'] = forms.ChoiceField(choices=self.get_choices())

    class Meta:
        model = Menu
        fields = '__all__'


@admin.register(Menu)
class MenuAdmin(admin.ModelAdmin):

    form = MenuForm
