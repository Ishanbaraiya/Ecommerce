from django.db import models


# from colorfield.fields import ColorField
# Create your models here.

class signup(models.Model):
    name=models.CharField(max_length=30,blank=True,null=True)
    email=models.EmailField(unique=True,blank=True,null=True)
    otp=models.CharField(max_length=6,default=0,blank=True,null=True)
    password=models.CharField(max_length=30, null=True)
    img = models.ImageField(upload_to="media", blank=True, null=True)


    def __str__(self) -> str:
        return self.name

class categories(models.Model):
    name=models.CharField(max_length=30,blank=True,null=True)
    def __str__(self) -> str:
        return self.name
    
class color(models.Model):
    name = models.CharField(max_length=100,blank=True,null=True)
    color_name = models.CharField(max_length=100,blank=True,null=True)

    def __str__(self) -> str:
        return self.name

class color_cart(models.Model):
    name = models.CharField(max_length=50,null=True,blank=True)

    def __str__(self) -> str:
        return self.name

class size_cart(models.Model):
    name = models.CharField(max_length=50,null=True,blank=True)

    def __str__(self) -> str:
        return self.name

class products(models.Model):
    categories_id = models.ForeignKey(categories,on_delete=models.CASCADE,blank=True,null=True)
    color_id = models.ForeignKey(color,on_delete=models.CASCADE,blank=True,null=True)
    name = models.CharField(max_length=100, blank=True, null=True)
    quantity = models.IntegerField(default=1,blank=True, null=True)
    img = models.ImageField(upload_to="media", blank=True, null=True)
    color = models.ManyToManyField(color_cart,blank=True,null=True)
    size = models.ManyToManyField(size_cart,blank=True,null=True)
    price = models.IntegerField()
    description = models.TextField()

    def __str__(self) -> str:
        return self.name

class add_to_cart(models.Model):
    products_id = models.ForeignKey(products, on_delete=models.CASCADE,blank=True,null=True)
    user_id = models.ForeignKey(signup, on_delete=models.CASCADE,blank=True,null=True)
    name = models.CharField(max_length=100, blank=True, null=True)
    total_prize = models.IntegerField()
    quantity = models.IntegerField(default=1,blank=True, null=True)
    img = models.ImageField(upload_to="media", blank=True, null=True)
    price = models.IntegerField()
    color = models.CharField(max_length=100, blank=True, null=True)
    size = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self) -> str:
        return self.name

class wish_list(models.Model):
    products_id = models.ForeignKey(products, on_delete=models.CASCADE,blank=True,null=True)
    user_id = models.ForeignKey(signup, on_delete=models.CASCADE,blank=True,null=True)
    name = models.CharField(max_length=100,null=True,blank=True)
    img = models.ImageField(upload_to="media",null=True,blank=True)

    def __str__(self) -> str:
        return self.name

class contacts(models.Model):
    email = models.EmailField(unique=True,blank=True,null=True)
    msg = models.TextField(blank=True,null=True)

    def __str__(self) -> str:
        return self.email
    
class coupon_code(models.Model):
    code = models.CharField(max_length=50,blank=True,null=True)
    discount = models.IntegerField()
    expiry_date = models.DateTimeField()
    one_time_use = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.code
    
class Billing_detail(models.Model):
    user_id = models.ForeignKey(signup,on_delete=models.CASCADE,null=True,blank=True)
    full_name = models.CharField(max_length=50,blank=True,null=True)
    mobile = models.IntegerField()
    pin_code = models.IntegerField()
    street_address = models.TextField()
    town = models.CharField(max_length=100,blank=True,null=True)
    district = models.CharField(max_length=100,blank=True,null=True)
    state = models.CharField(max_length=100,blank=True,null=True)

    def __str__(self) -> str:
        return self.user_id.name
    
choice = (("success", "success") ,("On the way", "On the way"),("Delivered", "Delivered"),("Cancelled","cancelled"),("Returned","Returned"))
class order(models.Model):
    user_id = models.ForeignKey(signup,on_delete=models.CASCADE,null=True,blank=True)
    address_id = models.ForeignKey(Billing_detail,on_delete=models.CASCADE,null=True)
    order_id = models.CharField(max_length=60, blank=True, null=True)
    name = models.CharField(max_length=50,null=True,blank=True)
    img = models.ImageField(null=True,blank=True)
    description = models.CharField(max_length=50,null=True,blank=True)
    size = models.CharField(max_length=50,null=True,blank=True)
    quantity = models.IntegerField()
    price = models.IntegerField()
    status = models.CharField(choices=choice,max_length=50,null=True,blank=True)
    total_price = models.IntegerField(default=1,null=True,blank=True)
    time = models.DateTimeField(auto_now_add=True,blank=True,null=True)
    add_date = models.DateTimeField(blank=True,null=True)

    def __str__(self) -> str:
        return self.name
       

class rating(models.Model):
    product_id=models.ForeignKey(products,on_delete=models.CASCADE,null=True,blank=True)         
    user_id=models.ForeignKey(signup,on_delete=models.CASCADE,null=True,blank=True) 
    rating_star = models.IntegerField(choices=[(i, i) for i in range(1, 6)], blank=True,null=True)
    image=models.ImageField(upload_to="media",blank=True,null=True)
    comment=models.TextField()
    name=models.CharField(max_length=50)
    email=models.EmailField(max_length=50)
    date=models.DateTimeField(auto_now=True,blank=True,null=True) 

    def __str__(self) -> str:
        return self.name       