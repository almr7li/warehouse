from django import forms
from .models import Goods

class GoodsForm(forms.ModelForm):
    class Meta:
        model = Goods
        fields = ('name', 'price', 'quantity')
    
    def __init__(self, *args, **kwargs):
        super(GoodsForm, self).__init__(*args, **kwargs)
        self.fields['name'].empty_label = "Select"
