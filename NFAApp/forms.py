from django import forms
from .models import Entry,Vendors
from django.forms.models import(
    inlineformset_factory,
    modelform_factory,
    modelformset_factory
)

class EntryForm(forms.ModelForm):
      class Meta:
        model = Entry
        fields = ('project_name','division','subject_line','summary','intimation','FillName')
        widgets = {
        'project_name': forms.TextInput(attrs={'class': 'form-control'}),
        'division': forms.TextInput(attrs={'class': 'form-control'}),
        'subject_line': forms.TextInput(attrs={'class': 'form-control'}),
        'summary': forms.TextInput(attrs={'class': 'form-control'}),
         }


class VendorForm(forms.ModelForm):
    class Meta:
        model = Vendors
        fields = ('project','vendor_name', 'item_name','total_base_value','quantity','unit_of_measurement' ,'freight_charges', 
                'pf_charges','custom_duty' , 'installation_charges' , 'amc_charges' , 'third_party_inspection_charges',
                  'other_charges' ,'total_value' , 'gst' , 'landed_cost', 'delivery','payment_terms','remark')


        widgets = {
        'vendor_name': forms.TextInput(attrs={'class': 'form-control'}),
        'item_name': forms.TextInput(attrs={'class': 'form-control'}),
        'total_base_value': forms.NumberInput(attrs={'class': 'form-control'}),
        'quantity': forms.NumberInput(attrs={'class': 'form-control'}),
        'unit_of_measurement': forms.NumberInput(attrs={'class': 'form-control'}),
        'freight_charges': forms.NumberInput(attrs={'class': 'form-control'}),
        'pf_charges': forms.NumberInput(attrs={'class': 'form-control'}),
        'custom_duty': forms.NumberInput(attrs={'class': 'form-control'}),
        'installation_charges': forms.NumberInput(attrs={'class': 'form-control'}),
        'amc_charges': forms.NumberInput(attrs={'class': 'form-control'}),
        'third_party_inspection_charges': forms.NumberInput(attrs={'class': 'form-control'}),
        'other_charges': forms.NumberInput(attrs={'class': 'form-control'}),
        'total_value': forms.NumberInput(attrs={'class': 'form-control'}),
        'gst': forms.NumberInput(attrs={'class': 'form-control'}),
        'landed_cost': forms.NumberInput(attrs={'class': 'form-control'}),
        'delivery': forms.NumberInput(attrs={'class': 'form-control'}),
        'payment_terms': forms.NumberInput(attrs={'class': 'form-control'}),
        'remark': forms.TextInput(attrs={'class': 'form-control'}),
         }

VendorFormSet = inlineformset_factory(
    Entry,
    Vendors,
    VendorForm,
    can_delete=True,
    extra=1,
)
