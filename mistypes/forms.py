
from django import forms

from .models import Mistype


class MistypeForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(MistypeForm, self).__init__(*args, **kwargs)
        self.fields['before'].strip = False
        self.fields['mistype'].strip = False
        self.fields['after'].strip = False

    class Meta:
        model = Mistype
        fields = ['url', 'before', 'mistype', 'after', 'comment']
        widgets = {
            'url': forms.HiddenInput(),
            'before': forms.HiddenInput(),
            'mistype': forms.HiddenInput(),
            'after': forms.HiddenInput(),
            'comment': forms.TextInput()
        }
