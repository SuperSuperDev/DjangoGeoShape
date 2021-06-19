from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from model_utils.fields import UUIDField
from model_utils import Choices
from model_utils.models import TimeStampedModel
import datetime
# Create your models here.

def current_year():
    return datetime.date.today().year

def max_value_current_year(value):
    return MaxValueValidator(current_year())(value)
    

class Property_Listing(models.Model):
    
    
    title = models.CharField(max_length=100)
    STATUS = Choices(('Visible', ['new', 'archived', 'active']), ('Invisible', ['draft', 'deleted']))
    status = models.CharField(choices=STATUS, default=STATUS.draft, max_length=30)
    LISTING_STATUS = Choices(
        ('for_sale', ('For Sale')),
        ('for_rent', ('For Rent')),
        ('for_rent', ('For Sale and Rent')),
        ('rental_under_offer', ('Rental - Under Offer')),
        ('sale_under_offer', ('Sale - Under Offer')),
        ('sold', ('Sold')), ('rented', ('Rented'))
        )
    listing_status = models.CharField(choices=LISTING_STATUS, default=LISTING_STATUS.for_sale, max_length=30)
    LISTING_TYPE = Choices(
        ('commercial', ('Commercial')),
        ('residential', ('Residential')),
        ('business', ('Business')),
    )
    listing_type = models.CharField(choices=LISTING_TYPE, default=LISTING_TYPE.residential, max_length=20)
    PROPERTY_TYPE = Choices(
        ('house', ('House')),
        ('flat', ('Flat')),
        ('office', ('Office')),
        ('business', ('Business')),
        ('industrial', ('Industrial')),
        ('retail', ('Retail')),
        ('hospitality', ('Hospitality')),
    )
    property_type = models.CharField(choices=PROPERTY_TYPE, default=PROPERTY_TYPE.house, max_length=20)
    bed_num =  models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(5000)], default=0)
    bath_num = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(5000)], default=0)
    floors_num = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(5000)], default=0)
    floor_location = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(5000)], default=0)
    sq_meters = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(5000)], default=0)
    year_built = models.IntegerField(('year'), validators=[MinValueValidator(0), max_value_current_year], default=2000)
    # models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(5000)], default=0)
    land_size = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(5000)], default=0)
    FURNISHINGS = Choices(
        ('fully_furnished', ('Fully Furnished')),
        ('partly_furnished', ('Partly Furnished')),
        ('unfurnished', ('Unfurnished')),
        ('not_applicable', ('N/A'))
    )
    furnishings = models.CharField(choices=FURNISHINGS, default=FURNISHINGS.unfurnished, max_length=50)
    parking_spaces = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(5000)], default=0)
    reference = models.CharField(null=True, max_length=20)
    # address_id FK >- Addresses.id
    # media - img, vid, pdf, files/docs
    short_description = models.CharField(null=False, max_length=500)
    full_description = models.TextField(null=False, max_length=50000)

    def __str__(self):
        return f'{self.title} - {self.listing_type} {self.property_type} {self.listing_status}'
    
