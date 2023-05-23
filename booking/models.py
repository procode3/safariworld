from django.db import models
import uuid


class BaseModel(models.Model):
    """Handles the creation of id, created_at and updated_at attributes for all classes"""
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def get_image_path(self, filename):
        """Function to define the upload path for images."""
        return os.path.join('images', str(self.id), filename)
    
    def __str__(self):
        try:
            if self.__class__.__name__ == 'User':
                return f'{self.first_name} ({self.id})'
            if self.name:
                return f'{self.name} ({self.id})'
        except:
            return str(self.id)
    
    class Meta:
        abstract = True


class Place(BaseModel):
    """Instantiats the exact desistation that the adventure will occur"""
    name = models.CharField(max_length=250)
    description = models.CharField(max_length=250)
    latitude = models.DecimalField(max_digits=30, decimal_places=18)
    longitude = models.DecimalField(max_digits=30, decimal_places=18)
    image = models.FileField(upload_to='images')

class Adventure(BaseModel):
    """Describes all the details of a particular trip"""
    name = models.CharField(max_length=250)
    place_id = models.ForeignKey(Place, on_delete=models.SET_NULL, null=True, related_name='adventures')
    description = models.CharField(max_length=250)
    departure_date = models.DateField()
    return_date = models.DateField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    slots = models.IntegerField()
    age_limit = models.IntegerField(default=0)
    activities = models.CharField(max_length=250)


class User(BaseModel):
    """Instantiate users for the safariworld system"""
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
    user_type = models.CharField(choices=USER_TYPES, max_length=250)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=250)
    phone_number = models.CharField(max_length=20)
    gender = models.IntegerField(choices=GENDER_CHOICES, null=True)
    bio = models.CharField(max_length=250, blank=True)
    password = models.CharField(max_length=128)


class Review(BaseModel):
    """Describes how user reviews will be stored in the db"""
    description = models.CharField(max_length=250)
    rating = models.IntegerField()
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reviews')
    adventure_id = models.ForeignKey(Adventure, on_delete=models.CASCADE, related_name='review_advs')



    
class Amenity(BaseModel):
    """Amenities for adventures specifing the specific section for a particular amenity"""
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
    adventure_id = models.ForeignKey(Adventure, on_delete=models.CASCADE, related_name='amenity_advs')
    section = models.CharField(max_length=50, choices=SECTION_CHOICES)
    name = models.CharField(max_length=250)
    description = models.CharField(max_length=250)
    price = models.DecimalField(max_digits=10, decimal_places=2)   
    image = models.ImageField(upload_to='amenity_images', null=True)


class Booking(BaseModel):
    """Model for handling bookings for a specific adventure
       amount paid will be entered manually by staff
       in future the amount_paid will be retrieved from an MPESA API
    """
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name='bookings')
    adventure_id = models.ForeignKey(Adventure, on_delete=models.CASCADE, related_name='booking_advs')
    number_of_persons = models.IntegerField(default=1)
    amount_paid = models.DecimalField(max_digits=10, decimal_places=2)
    is_confimed = models.BooleanField(default=False)
    

class Itinerary(BaseModel):
    """Itinerary will store the day to day schedule of the adventure"""
    adventure_id = models.ForeignKey(Adventure, on_delete=models.CASCADE, related_name='itinerary_advs')
    name = models.CharField(max_length=250)
    description = models.CharField(max_length=250)
    image = models.ImageField(upload_to='itinerary_images/')
    day = models.DateField()
    
