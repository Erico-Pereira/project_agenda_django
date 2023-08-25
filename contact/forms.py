from django import forms
from contact.models import Contact
from django.core.exceptions import ValidationError


class ContactForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['first_name'].widget.attrs.update({
            'class': 'classe-a classe-b',
            'placeholder': 'Escreva seu nome',
        })

    class Meta:
        model = Contact
        fields = (
            'first_name', 'last_name', 'phone',
            'email', 'description', 'category'
        )

        # widgets = {
        #     # 'first_name': forms.PasswordInput()
        #     'first_name': forms.TextInput(
        #         attrs={
        #             'class': 'classe-a classe-b',
        #             'placeholder': 'Escreva seu nome',
        #         }
        #     )
        # }

    def clean(self):
        first_name = self.cleaned_data.get('first_name')
        last_name = self.cleaned_data.get('last_name')

        if first_name == last_name:
            self.add_error(
                'first_name',
                ValidationError(
                    'O primeiro nome não deve ser igual ao segundo nome',
                    code='invalid'
                )
            )
            self.add_error(
                'last_name',
                ValidationError(
                    'O primeiro nome não deve ser igual ao segundo nome',
                    code='invalid'
                )
            )

        return super().clean()

    def clean_first_name(self):
        first_name = self.cleaned_data.get('first_name')

        if len(first_name) <= 3:
            self.add_error(
                'first_name',
                ValidationError(
                    'Nome menor que 3 digitos',
                    code='invalid'
                )
            )
        return first_name
