from django import forms
from django.core import validators

class FormArticle(forms.Form):
    titulo = forms.CharField(
        label = "Título",
        max_length = 20,
        required = True,
        widget = forms.TextInput(
            attrs = {
                'placeholder': 'Mete el título',
                'class': 'titulo_form_article' 
            }
        ),
        validators = [
            validators.MinLengthValidator(4, 'El título es demasiado corto'),
            validators.RegexValidator('^[A-Za-z0-9ñ ]*$', message = 'El título está mal formado', code = 'invalid_title')
        ]
    )

    contenido = forms.CharField(
        label = "Contenido",
        widget = forms.Textarea,
        validators = [
            validators.MaxLengthValidator(50, 'Te has pasado, has puesto mucho texto')
        ]
    )

    contenido.widget.attrs.update({
        'placeholder': 'Mete el contenido YAA',
        'class': 'contenido_form_article',
        'id': 'contenido_form'
    })

    public_options = [
        (1, 'Si'),
        (0, 'No')
    ]

    publicado = forms.TypedChoiceField(
        label = "¿Publicado?",
        choices = public_options
    )
