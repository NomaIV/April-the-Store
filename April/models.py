from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


# Product
class Product(models.Model):
    """
     Represents product in the system.

    :param name: Name of the product.
    :type name: str
    :param price: Price of the product.
    :type price: decimal.Decimal
    :param description: Description of the product.
    :type description: str
    :param category: Category of the product.
    :type category: str

    :rtype: Product
    """
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    description = models.TextField()
    category = models.CharField(max_length=255)


# Order
class Order(models.Model):
    """
    Represents an order.

    :param product: Product associated with the order.
    :type product: Product
    :param quantity: Quantity of the product in the order.
    :type quantity: int
    :param total_price: Total price of the order.
    :type total_price: decimal.Decimal
    :param created_at: Timestamp when the order was created.
    :type created_at: datetime.datetime

    :rtype: Order
    """
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    total_price = models.DecimalField(max_digits=6, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)


# Customer
class Customer(models.Model):
    """
    Represents customer in the system.

    :param name: Name of the customer.
    :type name: str
    :param email: Email address of the customer.
    :type email: str
    :param phone: Phone number of the customer.
    :type phone: str

    :rtype: Customer
    """
    name = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=20)


# Payment
class Payment(models.Model):
    """
    Represents payment for an order in the system.

    :param order: Order associated with the payment.
    :type order: Order
    :param payment_method: Payment method used.
    :type payment_method: str
    :param amount: Amount of the payment.
    :type amount: decimal.Decimal
    :param created_at: Timestamp when the payment was created.
    :type created_at: datetime.datetime

    :rtype: Payment
    """
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    payment_method = models.CharField(max_length=255)
    amount = models.DecimalField(max_digits=6, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)


# Review
class Review(models.Model):
    """
    Represents review for a product by a customer in the system.

    :param product: Product associated with the review.
    :type product: Product
    :param customer: Customer who wrote the review.
    :type customer: Customer
    :param rating: Rating given in the review (1 to 5).
    :type rating: int
    :param created_at: Timestamp when the review was created.
    :type created_at: datetime.datetime

    :rtype: Review
    """
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    rating = models.PositiveIntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    created_at = models.DateTimeField(auto_now_add=True)

