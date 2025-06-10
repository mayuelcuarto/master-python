from django import forms

class FormArticle(forms.Form):
    titulo = forms.CharField(
        label = "Título"
    )

    contenido = forms.CharField(
        label = "Contenido",
        widget = forms.Textarea
    )
