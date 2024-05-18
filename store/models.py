from django.db import models
import datetime
from django.contrib.auth.models import User
from django.db.models.signals import post_save

# Create your models here.

# Create Customer Profile
class Profile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	date_modified = models.DateTimeField(User, auto_now=True)
	phone = models.CharField(max_length=20, blank=True)
	address1 = models.CharField(max_length=200, blank=True)
	address2 = models.CharField(max_length=200, blank=True)
	city = models.CharField(max_length=200, blank=True)
	state = models.CharField(max_length=200, blank=True)
	zipcode = models.CharField(max_length=200, blank=True)
	country = models.CharField(max_length=200, blank=True)
	old_cart = models.CharField(max_length=200, blank=True, null=True)

	def __str__(self):
		return self.user.username

# Create a user Profile by default when user signs up
def create_profile(sender, instance, created, **kwargs):
	if created:
		user_profile = Profile(user=instance)
		user_profile.save()

# Automate the profile thing
post_save.connect(create_profile, sender=User)



class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

    class Meta:
      verbose_name_plural = "Categories"



#customer
class customer(models.Model):
    first_name =  models.CharField(max_length=20)
    last_name =  models.CharField(max_length=20)
    phone =  models.CharField(max_length=12)
    email = models.EmailField(max_length=100)
    password =  models.CharField(max_length=100)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
    
    #product

class Product(models.Model):
    name =  models.CharField(max_length=30)
    price =   models.DecimalField(default=0, decimal_places=2, max_digits=6)
    Category = models.ForeignKey(Category, on_delete=models.CASCADE, default=1)
    description = models.CharField(max_length=250, default='', blank=True, null=True)
    image = models.ImageField(upload_to='products/')
    #sale stuff
    is_sale = models.BooleanField(default=False)
    sale_price = models.DecimalField(default=0, decimal_places=2, max_digits=6)


    def __str__(self):
        return self.name
        


#order
class order(models.Model):
    product = models.ForeignKey(Product,on_delete=models. CASCADE)
    customer =  models.ForeignKey(customer,on_delete=models. CASCADE)
    quantity = models.IntegerField(default=1)
    address =  models.CharField(max_length=100)
    phone =  models.CharField(max_length=12, default='', blank=True)
    date_ordered = models.DateTimeField(default=datetime.datetime.today)
    status =  models.BooleanField(default=False)

    def  __str__(self):
        return self.product

  

