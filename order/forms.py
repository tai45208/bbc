from django import forms
from order.models import order


class OrderForm(forms.ModelForm):
    name = forms.CharField(label='姓名',widget=forms.TextInput)
    cellphone = forms.CharField(label='電話',widget=forms.TextInput)
    c1 = forms.CharField(label='腿',widget=forms.TextInput)
    c2 = forms.CharField(label='翅膀',widget=forms.TextInput)
    c3 = forms.CharField(label='雞桶',widget=forms.TextInput)
    c4 = forms.CharField(label='可樂',widget=forms.TextInput)
    take = forms.CharField(label='備註', widget=forms.Textarea)
    class Meta:
        model = order
        fields = ['name', 'cellphone','c1','c2','c3','c4','take']