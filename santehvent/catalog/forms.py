from django import forms


class InvoiceForm(forms.Form):
    good_id = forms.CharField(label='ID')
    good_count = forms.IntegerField(label='count in', min_value=1)
    good_price = forms.FloatField(label='price by one', min_value=0)
