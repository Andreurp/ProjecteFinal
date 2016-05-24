from django import forms

class compra_producte(forms.Form):
    id_producte = forms.IntegerField()
    quantitat = forms.IntegerField()