from django import forms

# Add to Cart Form
class AddToCartForm(forms.Form):
    quantity = forms.IntegerField(min_value=1)

# Checkout Form
class CheckoutForm(forms.Form):
    shipping_address = forms.CharField(max_length=255)
    payment_method = forms.ChoiceField(choices=[('credit_card', 'Credit Card'), ('paypal', 'PayPal')], required= True)
    

