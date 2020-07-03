from django.forms import ModelForm
from Customer.models import Customer

class CustomerRegForm(ModelForm):
    class Meta:
       model=Customer
       fields="__all__"

    def clean(self):
        pass

class CustomerLoginForm(ModelForm):
    class Meta:
        model=Customer
        fields=['username','password']
    def clean(self):
        pass