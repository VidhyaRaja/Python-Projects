from django import forms
from .models import Product

class ProductForm(forms.ModelForm):
    title = forms.CharField(label='',
     widget=forms.TextInput(attrs={"placeholder":"Your Title"}))
    description = forms.CharField(
        required=False,
        widget=forms.Textarea(
            attrs={
                'class':'new-class-name two',
                "placeholder":"Your Title",
                'id':'my-id-for-textarea',
                'rows':20,
                'cols':80
                }
            )
        )
    price = forms.DecimalField(initial=199.99)
    class Meta:
        model = Product
        fields = [
            'title',
            'description',
            'price'
        ]
    def clean_title(self, *args, **kwargs):
        title = self.cleaned_data.get('title')
        # if not "CFE" in title:
        #     raise forms.ValidationError("This is not a valid title")
        # if not "NEWS" in title:
        #     raise forms.ValidationError("This is not a valid title")
        return title

    def clean_email(self, *args, **kwargs):
        email = self.cleaned_data.get('email')
        if not email.endswith("edu"):
            raise forms.ValidationError("This is not a valid email")
            
class RawProductForm(forms.Form):
    title = forms.CharField(label='', widget=forms.TextInput(attrs={"placeholder":"Your Title"}))
    description = forms.CharField(
        required=False,
        widget=forms.Textarea(
            attrs={
                'class':'new-class-name two',
                "placeholder":"Your Title",
                'id':'my-id-for-textarea',
                'rows':20,
                'cols':80
                }
            )
        )
    price = forms.DecimalField(initial=199.99)