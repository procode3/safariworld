from django.db import models
import uuid

# Create your models here.
class BaseModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def get_image_path(self, filename):
        """Function to define the upload path for images."""
        return os.path.join('images', str(self.id), filename)

    class Meta:
        abstract = True

class Adventure(BaseModel):
    description = models.CharField(max_length=250)
    departure_date = models.DateField()
    return_date = models.DateField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    slots = models.IntegerField()
    age_limit = models.IntegerField(null=True)
    activities = models.CharField(max_length=250)

class User(BaseModel):
    USER_TYPES = (
        ('A', 'Admin'),
        ('S', 'Staff'),
        ('U', 'User'),
    )

    GENDER_CHOICES = (
        (1, 'Male'),
        (2, 'Female'),
        (3, 'Other'),
    )
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=250)
    phone_number = models.CharField(max_length=20)
    gender = models.IntegerField(choices=GENDER_CHOICES, null=True)
    bio = models.CharField(max_length=250, null=True)
    password = models.CharField(max_length=128)
    user_type = models.IntegerField(choices=USER_TYPES)


class Reviews(Basemodel):
    description = models.CharField(max_length=250)
    rating = models.IntegerField()
    user_id = 'FK'
    adventure_id = 'FK'


class Place(BaseModel):
    name = CharField(max_length=250)
    description = models.CharField(max_length=250)
    latitude = models.DecimalField(max_digits=9, decimal_places=6)
    longitude = models.DecimalField(max_digits=9, decimal_places=6)
    image = models.FileField(upload_to='images')
    
class Amenities(BaseModel):
    SECTION_CHOICES = (
        ('transportation', 'Transportation'),
        ('accommodation', 'Accommodation'),
        ('dining', 'Dining'),
        ('facilities', 'Facilities'),
        ('entertainment', 'Entertainment and Activities'),
        ('accessibility', 'Amenities for Accessibility'),
        ('business', 'Business and Conference Facilities'),
        ('services', 'Special Services'),
        ('additional', 'Additional Services'),
    )
    
    name = CharField(max_length=250)
    description = models.CharField(max_length=250)
    price = models.DecimalField(max_digits=10, decimal_places=2)   
    section = models.CharField(max_length=50, choices=SECTION_CHOICES)

class Booking(BaseModel):
    user_id = 'FK'
    adventure_id = 'FK'
    is_confimed = models.BooleanField(default=False)
    

class Itenerary(BaseModel):
    adventure_id = 'FK'
    name = CharField(max_length=250)
    description = models.CharField(max_length=250)
    image = ImageField(upload_to='itenerary_images/')
    day = models.DateField()
    
