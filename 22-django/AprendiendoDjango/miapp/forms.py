from django import forms

class FormArticle(forms.Form):
    titulo = forms.CharField(
        label = "Título"
    )

    contenido = forms.CharField(
        label = "Contenido",
        widget = forms.Textarea
    )

    public_options = [
        (1, 'Si'),
        (0, 'No')
    ]

    publicado = forms.TypedChoiceField(
        label = "¿Publicado?",
        choices = public_options
    )
