from django.db import models


# from pygments.lexers import get_all_lexers
# from pygments.styles import get_all_styles
#
# LEXERS = [item for item in get_all_lexers() if item[1]]
# LANGUAGE_CHOICES = sorted([(item[1][0], item[0]) for item in LEXERS])
# STYLE_CHOICES = sorted((item, item) for item in get_all_styles())


class Users(models.Model):
    LANGUAGES = (
        ('en', 'English'),
        ('de', 'German'),
        ('it', 'Italian'),
        ('ot', 'Others'),
    )
    GENDER = (
        ('MALE', 'MALE'),
        ('FEMALE', 'FEMALE'),
        ('OTHER', 'OTHER'),
        ('-unknown-', '-unknown-'),
    )
    LOCATIONS = (
        ('US', 'US'),
        ('DE', 'Germany'),
        ('AU', 'Australia'),
        ('CA', 'Canada'),
        ('IT', 'Italy'),
        ('FR', 'France'),
        ('GB', 'Britain'),
        ('ES', 'Spain'),
        ('PT', 'Portugal'),
        ('NL', 'Netherlands'),
        ('other', 'Others'),
    )
    created = models.DateTimeField(auto_now_add=True)
    # timestamp_first_active = models.DateField(auto_now_add=True)
    account = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    gender = models.CharField(choices=GENDER, max_length=100, default='-unknown-')
    age = models.IntegerField(blank=True, default=0)
    signup_method = models.CharField(max_length=20, default='basic')
    language = models.CharField(choices=LANGUAGES, blank=True, default='en', max_length=100)
    affiliate_channel = models.CharField(max_length=20, default='direct')
    affiliate_provider = models.CharField(max_length=20, default='direct')
    first_affiliate_tracked = models.CharField(max_length=20, default='untracked')
    signup_app = models.CharField(max_length=20, default='Web')
    os = models.CharField(max_length=100, default='Windows')
    browser = models.CharField(max_length=100, default='Chrome')
    location = models.CharField(choices=LOCATIONS, blank=True, default='us', max_length=100)

    class Meta:
        ordering = ('created',)

        # class Snippet(models.Model):
        # 	created = models.DateTimeField(auto_now_add=True)
        # 	title = models.CharField(max_length=100, blank=True, default='')
        # 	code = models.TextField()
        # 	linenos = models.BooleanField(default=False)
        # 	language = models.CharField(choices=LANGUAGE_CHOICES, default='python', max_length=100)
        # 	style = models.CharField(choices=STYLE_CHOICES, default='friendly', max_length=100)
        #
        # 	class Meta:
        # 		ordering = ('created',)


class UsersLocation(models.Model):
    LOCATIONS = (
        ('US', 'US'),
        ('DE', 'Germany'),
        ('AU', 'Australia'),
        ('CA', 'Canada'),
        ('IT', 'Italy'),
        ('FR', 'France'),
        ('GB', 'Britain'),
        ('ES', 'Spain'),
        ('PT', 'Portugal'),
        ('NL', 'Netherlands'),
        ('other', 'Others'),
    )
    account = models.CharField(max_length=100)
    location_1 = models.CharField(choices=LOCATIONS, blank=True, default='US', max_length=100)
    location_2 = models.CharField(choices=LOCATIONS, blank=True, default='DE', max_length=100)
    location_3 = models.CharField(choices=LOCATIONS, blank=True, default='AU', max_length=100)
    location_4 = models.CharField(choices=LOCATIONS, blank=True, default='CA', max_length=100)
    location_5 = models.CharField(choices=LOCATIONS, blank=True, default='FR', max_length=100)

    class Meta:
        ordering = ('account',)