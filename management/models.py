from django.db import models
from django.utils.translation import gettext as _


# Create your models here.

class Member(models.Model):
    """
    Represents a gym member.
    """
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15)
    membership_start = models.DateField()
    membership_end = models.DateField()
    created_at = models.DateTimeField(_("creation time"), auto_now_add=True)
    updated_at = models.DateTimeField(_("update time"), auto_now=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    

class MemberEntry(models.Model):
    """
    Represents an entry record for a gym member.
    """
    member = models.ForeignKey(Member, on_delete=models.CASCADE)
    entry_time = models.DateTimeField(auto_now_add=True)
    exit_time = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"{self.member} - {self.entry_time}"
    
    
class Trainer(models.Model):
    """
    Represents a trainer at the gym.
    """
    name = models.CharField(max_length=100)
    specialty = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15)
    created_at = models.DateTimeField(_("creation time"), auto_now_add=True)
    updated_at = models.DateTimeField(_("update time"), auto_now=True)

    def __str__(self):
        return self.name
    
    
class GymClass(models.Model):
    """
    Represents a gym class.
    """
    name = models.CharField(max_length=100)
    trainer = models.ForeignKey(Trainer, on_delete=models.CASCADE)
    member = models.ForeignKey(Member, on_delete=models.CASCADE)
    start_time = models.TimeField()
    end_time = models.TimeField()
    created_at = models.DateTimeField(_("creation time"), auto_now_add=True)
    updated_at = models.DateTimeField(_("update time"), auto_now=True)

    def __str__(self):
        return self.name
    

class Payment(models.Model):
    """
    Represents a payment made by a gym member.
    """
    ONLINE = 'online'
    CASH = 'cash'
    PAYMENT_METHOD = (
        (ONLINE, 'Online'),
        (CASH, 'Cash'),
    )
    
    member = models.ForeignKey(Member, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_date = models.DateField()
    payment_method = models.CharField(max_length=50, choices=PAYMENT_METHOD)
    created_at = models.DateTimeField(_("creation time"), auto_now_add=True)
    updated_at = models.DateTimeField(_("update time"), auto_now=True)

    def __str__(self):
        return f"{self.member} - {self.amount}"