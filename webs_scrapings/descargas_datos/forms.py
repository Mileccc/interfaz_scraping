from django import forms


class LinkForm(forms.Form):
    url_inicial = forms.CharField(
        max_length=1000,
        required=True,
        widget=forms.TextInput(attrs={'class': 'input-link'})
    )
    url_base = forms.CharField(
        max_length=1000,
        required=True,
        widget=forms.TextInput(attrs={'class': 'input-link'})
    )
    selector_enlace = forms.CharField(
        max_length=1000,
        required=True,
        widget=forms.TextInput(attrs={'class': 'input-link'})
    )
    selector_articulo = forms.CharField(
        max_length=1000,
        required=True,
        widget=forms.TextInput(attrs={'class': 'input-link'})
    )
    selector_titulo = forms.CharField(
        max_length=1000,
        required=True,
        widget=forms.TextInput(attrs={'class': 'input-link'})
    )
