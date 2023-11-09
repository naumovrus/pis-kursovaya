from .models import Customer, Products
from django import forms
from django.core import validators
from django.forms import ModelForm, TextInput


class CustomerForm(ModelForm):
    class Meta:
        model = Customer
        fields = ['cust_name', 'amount_of_purchases', 'cust_balance', 'cust_ceiling', 'cust_debt', 'comment']

        widgets = {
            "cust_name": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Имя клиента'
            }),
            "amount_of_purchases": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Сумма покупок'
            }),
            "cust_balance": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Счёт'
            }),
            "cust_ceiling": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Потолок кредита'
            }),
            "cust_debt": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Долг'
            }),
            "comment": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Комментарий'
            }),
        }



class ProductsForm(ModelForm):
    class Meta:
        model = Products
        fields = ['prod_name', 'prod_cost', 'prod_amount']

        widgets = {
            "prod_name": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Название товара',
            }),
            "prod_amount": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Количество на складе'
            }),
        }

    prod_cost = forms.IntegerField(validators=[validators.MinValueValidator(1)], widget=TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Цена'
        }
    ))


class Deal(forms.Form):
    cust = forms.ModelChoiceField(label='Клиент', queryset=Customer.objects.all())
    prod = forms.ModelChoiceField(label='Товар', queryset=Products.objects.all())


class Barter(forms.Form):
    cust = forms.ModelChoiceField(label='Клиент', queryset=Customer.objects.all())
    homeprod = forms.ModelChoiceField(label='Товар для клиента', queryset=Products.objects.all())
    custprod = forms.ModelChoiceField(label='Товар для склада', queryset=Products.objects.all())