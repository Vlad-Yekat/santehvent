from django import forms


class InvoiceForm(forms.Form):
    goodID = forms.CharField(label="ID")
    goodcount = forms.IntegerField(label="count in", min_value=1)
    goodPrice = forms.FloatField(label="price by one", min_value=0)
