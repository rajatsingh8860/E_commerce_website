from django.db import models

# Create your models here.
class Product(models.Model):
    product_id=models.AutoField
    product_name=models.CharField(max_length=50)
    category=models.CharField(max_length=50,default="")
    subcategory=models.CharField(max_length=50,default="")
    price=models.IntegerField(default="0")
    desc=models.CharField(max_length=50000,default="")
    pub_date=models.DateField()
    image=models.ImageField(upload_to="shop/images",default="")

    def __str__(self):
        return self.product_name

class Contact(models.Model):
    msg_id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=70)
    email=models.CharField(max_length=70,default="")
    phone_no=models.CharField(max_length=70,default="")
    desc=models.CharField(max_length=500,default="")
    

    def __str__(self):
        return self.name  

class Order(models.Model):
    order_id=models.AutoField(primary_key=True)
    item_json=models.CharField(max_length=5000)
    amount=models.IntegerField(default=0)
    name=models.CharField(max_length=200)
    email=models.CharField(max_length=200)
    phone_no=models.CharField(max_length=70)
    address=models.CharField(max_length=70)
    city=models.CharField(max_length=70)
    state=models.CharField(max_length=70)
    zip_code=models.CharField(max_length=70)

class orderUpdate(models.Model):
    update_id=models.AutoField(primary_key=True)
    order_id=models.IntegerField(default="")
    update_desc=models.CharField(max_length=2000)
    timestamp=models.DateField(auto_now_add=True)

    def __str__(self):
        return self.update_desc[0:7]+"..." 


class Register(models.Model):
    user_id=models.AutoField(primary_key=True)
    first_name=models.CharField(max_length=50,default="")
    last_name=models.CharField(max_length=50,default="")
    user_name=models.CharField(max_length=50,default="")
    email=models.CharField(max_length=50)
    password=models.CharField(max_length=50000,default="")
    confirm_password=models.CharField(max_length=50000,default="")
    def __str__(self):
        return self.first_name


    



