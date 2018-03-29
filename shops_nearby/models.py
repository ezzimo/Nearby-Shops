from django.contrib.gis.db import models as gis_models
from django.contrib.gis import geos
from django.contrib.gis.measure import Distance
from django.db import models
import uuid # Required for unique shop
from django.urls import reverse #Used to generate URLs by reversing the URL patterns
from django.contrib.auth.models import AbstractUser, BaseUserManager ## A new class is imported. ##
from django.db.models.signals import post_save
from django.utils.translation import ugettext_lazy as _ # for translation

"""Declare models for Shops Nearby app."""
class UserManager(BaseUserManager):
    """Define a model manager for User model with no username field."""

    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        """Create and save a User with the given email and password."""
        if not email:
            raise ValueError('The given email must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        """Create and save a regular User with the given email and password."""
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        """Create and save a SuperUser with the given email and password."""
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(email, password, **extra_fields)







class Shop(models.Model):
    name = models.CharField(max_length=200)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text="Unique ID for this particular shop across whole library")
    email = models.EmailField(max_length=70,blank=False)
    city = models.CharField('city', blank=False, default='Rabat', max_length=200, null=False)
    shop_pic = models.ImageField(upload_to = 'pic_folder/', default = 'http://placehold.it/150x150', null= True)
    location = gis_models.PointField("longitude/latitude",
                                     geography=True, blank=False, null=True)
    #gis = gis_models.GeoManager()




    def __unicode__(self):
        return self.name, 'maplocation'


class User(AbstractUser):
    """User model."""

    username = None
    email = models.EmailField(_('email address'), unique=True)
    location = models.CharField('Address',max_length=200, default='', blank=False)
    preferred = models.ManyToManyField(Shop, related_name='Preferred')
    maplocation = gis_models.PointField("longitude/latitude",
                                         geography=True, blank=False, null=True)
    #gis = gis_models.GeoManager()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []


    @classmethod
    def make_preferred(cls, current_email, new_pref_shop):
        user, created = cls.objects.get_or_create(
            email=current_email
        )
        user.preferred.add(new_pref_shop)

    @classmethod
    def remove_preferred(cls, current_email, pref_shop):
        user, created = cls.objects.get_or_create(
            email=current_email
        )
        user.preferred.remove(pref_shop)
