from django.db import models
from django.contrib.auth.models import User



class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    description = models.TextField()
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name

class Item(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='items')
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    available = models.BooleanField(default=True)
    image = models.ImageField(upload_to='items/', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    popular = models.BooleanField(default=False)


    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField()
    image = models.ImageField(upload_to='products/')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
class LoyaltyProgram(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='loyalty_program')
    total_spent = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    reward_earned = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    last_updated = models.DateTimeField(auto_now=True)  # Keep track of the last time this record was updated

    def _str_(self):
        return f"Loyalty Program for {self.user.username}"

    def update_total_spent(self, amount_spent):
        # Adds to the total amount spent in the loyalty program.
        self.total_spent += amount_spent
        self.save()

    def check_reward(self):
        # Check if the user is eligible for a reward
        if self.total_spent >= 10000:  # Adjust the condition as needed
            self.reward_earned = self.total_spent * 0.10  # Example: 10% reward
            self.save()
