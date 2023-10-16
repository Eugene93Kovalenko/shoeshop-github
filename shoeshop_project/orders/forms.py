from django import forms
from django_countries.fields import CountryField
from django_countries.widgets import CountrySelectWidget


class CheckoutForm(forms.Form):
    country = CountryField(blank_label="(Select country)").formfield(widget=CountrySelectWidget(attrs={
        'class': 'custom-select d-block w-100',
    }))
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control',
                                                               'placeholder': 'Your firstname'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control',
                                                              'placeholder': 'Your lastname'}))
    address = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control',
                                                            'placeholder': 'Enter your address'}))
    city = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control',
                                                         'placeholder': 'Town or city'}))
    region = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control',
                                                           'placeholder': 'State or region'}))
    zip = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control',
                                                        'placeholder': 'Zip / Postal'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control',
                                                            'placeholder': 'Enter your email'}))
    phone = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control',
                                                          'placeholder': 'Enter your phone number'}))
    create_account = forms.BooleanField(label='CREATE AN ACCOUNT?', widget=forms.CheckboxInput, required=False)
    payment_method = forms.BooleanField(widget=forms.CheckboxInput)
    accept_terms = forms.BooleanField(widget=forms.CheckboxInput)
