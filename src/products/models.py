from django.db import models
from django.utils import timezone
from phone_field import PhoneField
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin,BaseUserManager # custom model
from django.utils.translation import gettext_lazy as _


# custom manager for our custom user model
# You should also define a custom manager for your user model. If your user model defines username, email, is_staff, is_active, is_superuser, last_login, and date_joined

class CustomUserManager(BaseUserManager,):    
    # create_superuser is method inherits from django BaseUserManager to create superuser
        
    def create_superuser(self,email,username,password, **kwargs):

        user  = self.create_user(email=self.normalize_email(email),username=username,password=password)

        user.is_admin = True
        user.is_user = True
        user.is_superuser = True
        
        # using=self.db is used to save data in configured db in settings
        user.save(using=self.db)
        return user

    # create_user is method inherits from django BaseUserManager to create user
    def create_user(self, email,username,password=None, **kwargs):
        if not email:
            raise ValueError(_('Users must have an email address'))
        if not username:
            raise ValueError("User must have an username")
        
        email = self.normalize_email(email) #Normalizes email addresses by lowercasing the domain portion of the email address.
        
        # self.model is inherits from BaseUserManager class property
        user  = self.model(email=email, username=username)
        user.set_password(password) # Sets the user's password to the given raw string, taking care of the password hashing. Doesn't save the User object.
        user.save(using=self._db)
        return user

    
# The easiest way to construct a compliant custom user model is to inherit from AbstractBaseUser. AbstractBaseUser provides the core implementation of a User model, including hashed passwords and tokenized password resets. You must then provide some key implementation details:
# To make it easy to include Django’s permission framework into your own user class, Django provides PermissionsMixin. This is an abstract model you can include in the class hierarchy for your user model, giving you all the methods and database fields necessary to support Django’s permission model.

# custom user model
# PermissionsMixin is used to create group
class User(AbstractBaseUser,PermissionsMixin):
  username = models.CharField(max_length = 50, blank = True, null = True, unique = True)
  email = models.EmailField(_('email address'), unique = True)
  about =  models.CharField(max_length = 50, blank = True, null = True)
  date_joined = models.DateTimeField(verbose_name='date joined', auto_now_add=True )
  last_login = models.DateTimeField(verbose_name='last_login',  auto_now=True)
  
  is_active = models.BooleanField(default=True)
  is_user = models.BooleanField(default=True)
  is_admin = models.BooleanField(default=False)
  is_superuser = models.BooleanField(default=False)
  
  # we need to specify user manger here to create user and get objects from Manager
  objects = CustomUserManager()
  
  USERNAME_FIELD = 'email' # to change username to email as login we need to specify 'email' here
  REQUIRED_FIELDS = ['username'] # need this field to use required fields 

 # set default property is_staff for replacement of is_user
  @property
  def is_staff(self):
        return self.is_user
  
  def has_perm(self, perm, obj=None):
      return True

  def has_module_perms(self, app_label):
      return True

 # post model
class Post(models.Model):
    author_fk = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    description= models.TextField(default='')
    image = models.ImageField(upload_to='pics',default='profile.png',blank=True)
    CreatedDate= models.DateField(auto_now_add=True, null=True)
    
    def __str__(self):
        return self.title
    
    
    # extra custom permissions to this model
    class Meta:
        permissions = (
            ('can_view_post', 'customer_can_view_post'),
            ('can_change_post', 'customer_can_change_post')
        )
        
        ordering = ('CreatedDate',)


  # return created username/email for successful process verification
#   # python string method to return str value 
 
# class CustomPermissions(models.Model):
#      class Meta:
#         managed = False # no database table creation or deletion 
#         default_permissions = () # disable default permissions
                
#         permissions =(
#             ('create_post', 'can create post'),
#             ('view_post', 'can view post'),
#             ('change_post', 'can change post'),
#             ('delete_post', 'can delete post')
#         )
        
        
# customer model
class Customerdata(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE, related_name='customer_fk', related_query_name='customer_fk')
    Customer_Name = models.CharField(max_length=500,null=False, blank=False)
    Email = models.EmailField(max_length=500,null=False, blank=False)
    Phone_No = PhoneField(blank=True, help_text='Contact phone number')
    Profile_pic = models.ImageField(default='profile.png',null=True, blank=True)
    Date_of_join = models.DateField(auto_now_add=True, null=True)
    
    def __str__(self):
      return (self.Customer_Name)
  
    class Meta:
        ordering = ('Date_of_join',)
    
    
class Type(models.Model): 
    name = models.CharField(max_length=200, null=True)
    
    def __str__(self):
        return self.name


# product model
class Productdata(models.Model):
    CATEGORY = [
        ('ELECTRONICS','ELECTRONICS'),
        ('TOYS','TOYS'),
        ('FASHION','FASHION'),
        ('GROCERY','GROCERY'),
    ]
    Product_Name = models.CharField(max_length=500,null=False, blank=False)
    Price = models.FloatField(null=True , blank=True, max_length=100)
    Category = models.CharField(max_length=500,null=False, blank=False, choices=CATEGORY)
    CreatedDate= models.DateField(auto_now_add=True, null=True)
    type = models.ManyToManyField(Type)
    Product_image = models.ImageField(upload_to='product_pics',default='profile.png',null=True, blank=True)
    digital = models.BooleanField(default=False, null=True, blank=False)
    
    def __str__(self):
        return self.Product_Name
    
    class Meta:
        ordering = ('CreatedDate',)

    @property
    def imageURL(self):
        try:
            url = self.Product_image.url
        except:
            url = '' 
        return url
    

class Order(models.Model): 
    STATUS = (
        ('Pending','Pending'),
        ('Out for delivery','Out for delivery'),
        ('Delivered','Delivered'),  
    ) 

    # foreign key should be placed in the child table. without customer and product we cant make order
    # one customer can make multiple orders. 
    customer_fk = models.ForeignKey(Customerdata, null=True, on_delete=models.SET_NULL  )
    Product_fk = models.ForeignKey(Productdata, null=True, on_delete=models.SET_NULL)      
    CreatedDate= models.DateField(auto_now_add=True, null=True)
    status = models.CharField(max_length=200, null=True,choices=STATUS)
    quantity = models.IntegerField(default=0, null=True, blank=True)
    note = models.CharField(max_length=1000, null=True)
    
    def __str__(self):
        return self.Product_fk.Product_Name
    
    class Meta:
        ordering = ('CreatedDate',)
    
    @property
    def get_total(self):
        total_price = self.Product_fk.Price * self.quantity        
        return total_price
    
    
class ShippingAddress(models.Model):
     customer_fk = models.ForeignKey(Customerdata, null=True, on_delete=models.SET_NULL  )
     order = models.ForeignKey(Order, on_delete=models.SET_NULL, blank=True, null=True)
     address = models.CharField(max_length=200, null=True)
     city = models.CharField(max_length=200, null=True)
     state = models.CharField(max_length=200, null=True)
     zipcode = models.CharField(max_length=200, null=True)
     CreatedDate= models.DateField(auto_now_add=True, null=True)
     
     def __str__(self):
         return self.address


#on_delete=models.SET_NULL: does not delete order data when customer data deleted
#on_delete=models.CASCADE: When the referenced object is deleted, also delete the objects that have references to it (when you remove a blog post for instance, you might want to delete comments as well). SQL equivalent: CASCADE.

# AUTH_USER_MODEL is the recommended approach when referring to a user model in a models.py file.

# For this you need to create custom User Model by either subclassing AbstractUser or AbstractBaseUser.

# AbstractUser: Use this option if you are happy with the existing fields on the User model and just want to remove the username field.
# AbstractBaseUser: Use this option if you want to start from scratch by creating your own, completely new User model.



class Movies(models.Model):
   file = models.FileField(upload_to='documents/', null=True)
   image = models.ImageField(upload_to='images/', null=True)
   
# print(help(models.Model))