from django import forms
from django.core.exceptions import ValidationError
from .models import Category, Product


class LoginForm(forms.Form):
    username = forms.CharField(
        max_length=150,
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "Enter username",
            "autofocus": True,
        })
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            "class": "form-control",
            "placeholder": "Enter password",
        })
    )


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ["name"]
        widgets = {
            "name": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Category name",
            })
        }


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = [
            "name", "sku", "category", "price", "stock",
            "image", "description", "status"
        ]
        widgets = {
            "name": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Product name",
            }),
            "sku": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "SKU",
            }),
            "category": forms.Select(attrs={"class": "form-select"}),
            "price": forms.NumberInput(attrs={
                "class": "form-control",
                "placeholder": "0.00",
                "step": "0.01",
                "min": "0.01",
            }),
            "stock": forms.NumberInput(attrs={
                "class": "form-control",
                "placeholder": "0",
                "min": "0",
            }),
            "image": forms.ClearableFileInput(attrs={
                "class": "form-control",
                "accept": "image/*",
            }),
            "description": forms.Textarea(attrs={
                "class": "form-control",
                "placeholder": "Product description",
                "rows": 4,
            }),
            "status": forms.Select(attrs={"class": "form-select"}),
        }

    def clean_name(self):
        name = self.cleaned_data.get("name", "").strip()
        if not name:
            raise ValidationError("Product name is required.")
        return name

    def clean_sku(self):
        sku = self.cleaned_data.get("sku", "").strip()
        if not sku:
            raise ValidationError("SKU is required.")
        return sku

    def clean_category(self):
        category = self.cleaned_data.get("category")
        if not category:
            raise ValidationError("Category is required.")
        return category

    def clean_price(self):
        price = self.cleaned_data.get("price")
        if price is None or price <= 0:
            raise ValidationError("Price must be greater than 0.")
        return price

    def clean_stock(self):
        stock = self.cleaned_data.get("stock")
        if stock is None or stock < 0:
            raise ValidationError("Stock cannot be negative.")
        return stock
