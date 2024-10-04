from django.db import models
from django.contrib.auth import get_user_model
from django.forms import ValidationError
from configurations.models import CustomUser, State, City, Location, Services, Specialization, degree, University, college, Memberships, Registration
user = get_user_model()

class Education(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='educations')
    degree = models.ForeignKey(degree, on_delete=models.DO_NOTHING, related_name='educations')
    institute = models.ForeignKey(University, on_delete=models.DO_NOTHING, related_name='educations')
    college = models.ForeignKey(college, on_delete=models.DO_NOTHING, related_name='educations')
    city = models.ForeignKey(City, on_delete=models.DO_NOTHING, related_name='educations')
    year = models.PositiveIntegerField()
    status = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.degree} - {self.user.name}'
    
class Training(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='training')
    degree = models.ForeignKey(degree, on_delete=models.DO_NOTHING, related_name='training')
    institute = models.ForeignKey(University, on_delete=models.DO_NOTHING, related_name='training')
    college = models.ForeignKey(college, on_delete=models.DO_NOTHING, related_name='training')
    city = models.ForeignKey(City, on_delete=models.DO_NOTHING, related_name='training')
    year = models.PositiveIntegerField()
    status = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.degree} - {self.user.name}'
    
class Experience(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='experiences')
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)
    status = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.title} - {self.user.name}'

class RegistrationList(models.Model):
    name = models.ForeignKey(Registration, on_delete=models.DO_NOTHING, related_name='registrations')
    year = models.PositiveIntegerField()
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.name    

class Listing(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='listings')
    title = models.CharField(max_length=100)
    description = models.TextField()
    contact_number = models.CharField(max_length=15)
    address = models.TextField(blank=True, null=True)
    city = models.ForeignKey(City, on_delete=models.DO_NOTHING, related_name='listings')
    state = models.ForeignKey(State, on_delete=models.DO_NOTHING, related_name='listings')
    location = models.ForeignKey(Location, on_delete=models.DO_NOTHING, related_name='listings')
    map_link = models.URLField(blank=True, null=True)
    whatsapp_number = models.CharField(max_length=15, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    status = models.BooleanField(default=True)
    search_tags = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    online_verified = models.BooleanField(default=False)
    offline_verified = models.BooleanField(default=False)
    services = models.ManyToManyField(Services, related_name='listings')
    qna = models.BooleanField(default=False)
    slug = models.SlugField(max_length=255, unique=True)
    experienceyear = models.PositiveIntegerField()
    fee = models.PositiveIntegerField()
    profile_image = models.ImageField(upload_to='listing/profile_images', blank=True, null=True)
    banner_image = models.ImageField(upload_to='listing/banner_images', blank=True, null=True)
    video_link = models.URLField(blank=True, null=True)
    claimed = models.BooleanField(default=False, verbose_name='Profile Claimed')
    specialization = models.ManyToManyField(Specialization, related_name='listings')
    services = models.ManyToManyField(Services, related_name='listings')
    education = models.ManyToManyField(Education, related_name='listings')
    memberships = models.ManyToManyField(Memberships, related_name='listings')
    experience = models.ManyToManyField(Experience, related_name='listings')
    registration = models.ManyToManyField(RegistrationList, related_name='listings')


    def __str__(self):
        return self.title

    
class Availability(models.Model):
    SLOT_TIME_CHOICES = [
        ('5', '5 minutes'),
        ('10', '10 minutes'),
        ('15', '15 minutes'),
        ('30', '30 minutes'),
        ('45', '45 minutes'),
        ('60', '60 minutes'),
    ]
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE, related_name='availabilities')  # Changed related_name
    day = models.CharField(max_length=10, choices=[
        ('MONDAY', 'Monday'), ('TUESDAY', 'Tuesday'), ('WEDNESDAY', 'Wednesday'), 
        ('THURSDAY', 'Thursday'), ('FRIDAY', 'Friday'), ('SATURDAY', 'Saturday'), 
        ('SUNDAY', 'Sunday')
    ])
    start_time = models.TimeField()
    end_time = models.TimeField()
    start_time2 = models.TimeField(blank=True, null=True)  # Made optional
    end_time2 = models.TimeField(blank=True, null=True)  # Made optional
    start_time3 = models.TimeField(blank=True, null=True)  # Made optional
    end_time3 = models.TimeField(blank=True, null=True)  # Made optional
    slot_time = models.CharField(max_length=3, choices=SLOT_TIME_CHOICES, default='15')
    max_in_slot = models.IntegerField(default=10)
    max_in_day = models.IntegerField(default=30)
    status = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.listing.title} - {self.day}'

class Unavailability(models.Model):
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE, related_name='unavailabilities')  # Changed related_name
    dateofunavailability = models.DateField()
    allday = models.BooleanField(default=True)
    start_time = models.TimeField(blank=True, null=True)
    end_time = models.TimeField(blank=True, null=True)
    status = models.BooleanField(default=True)

    def clean(self):
        if not self.allday and (not self.start_time or not self.end_time):
            raise ValidationError('Start time and end time are required if not an all-day unavailability.')

    def __str__(self):
        return f'{self.listing.title} - {self.dateofunavailability}'

class Review(models.Model):
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE, related_name='reviews')  # Changed related_name
    rating = models.PositiveIntegerField()
    comment = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)
    user = models.ForeignKey(user, on_delete=models.CASCADE, related_name='user_reviews')

    def __str__(self):
        return f'Review by {self.user} - {self.listing.title}'

    class Meta:
        constraints = [
            models.CheckConstraint(check=models.Q(rating__gte=1) & models.Q(rating__lte=5), name='rating_range'),
        ]

