from django.db import models
from django.contrib.auth.models import User
# import Pillow

# Create your models here.
class Client(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,null=True,blank=True)
    # test_var=models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)
    first_name = models.CharField(max_length=200,null=True)
    last_name = models.CharField(max_length=200,null=True)
    email = models.CharField(max_length=200,null=True)
    address = models.CharField(max_length=400,null=True)
    profile_pic = models.ImageField(null=True,blank=True) 
    
    published_at = models.DateTimeField(auto_now_add=True, db_index=True) #db_index field 


    def __str__(self):
        return self.first_name


class Solve(models.Model):
    client=models.ForeignKey(Client,on_delete=models.SET_NULL,null=True,blank=True)
    date_eval=models.DateTimeField(auto_now_add=True)
    # complete=models.BooleanField(default=False,null=True,blank=False)
    expr = models.CharField(max_length=200)
    valid_expr=models.BooleanField(default=False)
    result = models.FloatField(decimal_places=5) #upto maximum of 5 decimal places
    
    expr_id=models.CharField(max_length=200,null=True)

    try:
        result = eval (expr)
        print(result)
        valid_expr = True

    # except (SyntaxError, NameError, TypeError, ZeroDivisionError):
    #     valid_expr = False
    #     print()
    #     pass
    except Exception as e:
        print(e)
        valid_expr = False

    
    def __str__(self):
        return str(self.id)
    
    
    @property
    def get_cart_items(self):
        orderitems=self.orderitem_set.all()        
        item_total=sum([item.quantity for item in orderitems])
        return item_total

    @property
    def shipping(self):
        shipping=False
        orderitems=self.orderitem_set.all()
        for i in orderitems:
            if i.product.digital==False:
                shipping = True
                break # this is added by UNNAT seperately, to save some time
        return shipping 

