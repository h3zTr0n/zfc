from __future__ import unicode_literals

from django.db import models
# from image_cropping import ImageRatioField
from django.utils import timezone

class Author(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()

    def __unicode__(self):
        return "%s (%s)" %(self.name, self.email)

class Post(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(Author)
    slug = models.SlugField()
    body_summary = models.CharField(max_length=300)
    body = models.TextField()
    modified = models.DateTimeField(auto_now=True)
    img = models.ImageField(upload_to='news_uploaded_pics/%Y-%m-%d/',
                                null=True,
                                blank=True)


    created = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    class Meta:
        ordering = ['published_date']
        verbose_name_plural = "Posts"
    def __unicode__(self):
        return self.title

    # def get_absolute_url(self):
    #     return ('news', [self.slug])

    # def get_absolute_url(self):
    #     return reverse("list")

    #
    # def __unicode__(self):
    #     return "%s (%s)" %(self.title, self.author.name)

class Sponser(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField()
    logo = models.ImageField(
                            # upload_to="sponserImg/%Y-%m-%d/",
                            null=True,
                            blank=True
                            )
    created = models.DateTimeField(auto_now=True)
    # cropping = ImageRatioField('image', '85x150')

    class Meta:
        ordering = ['-created']
        verbose_name = "Sponser"
        verbose_name_plural = "Sponsers"

    def __unicode__(self):
        return self.name

class JuvenilePlayer(models.Model):
    name = models.CharField(max_length=255)
    number = models.IntegerField()
    img = models.ImageField(upload_to="player_img%Y-%m-%d", blank=True)

    verbose_name = "Juvenile Player"
    verbose_name_plural = "Juvenile Players"

    class Meta:
        verbose_name = "Juvenile Player"
        verbose_name_plural = "Juvenile Players"

    def __unicode__(self):
        return self.name

class VeteranPlayer(models.Model):
    name = models.CharField(max_length=255)
    number = models.IntegerField()
    img = models.ImageField(upload_to="player_img%Y-%m-%d", blank=True)

    class Meta:
        verbose_name = "Veteran Player"
        verbose_name_plural = "Veteran Players"

    def __unicode__(self):
        return self.name

class SeniorPlayer(models.Model):
    name = models.CharField(max_length=255)
    number = models.IntegerField()
    img = models.ImageField(upload_to="player_img%Y-%m-%d", blank=True)

    def __unicode__(self):
        return self.name

class History(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField()
    body = models.TextField()
    summary = models.CharField(max_length=300, help_text="300 characters for the summary filed.")
    from_year = models.DateField(auto_now_add=False, help_text="please use numbers: mm/dd/yyyy")
    to_year = models.DateField(auto_now=False, help_text="please use numbers: mm/dd/yyyy", null=True)
    img = models.ImageField(blank=True)

    class Meta:
        verbose_name_plural = "Histories"

    def __unicode__(self):
        return self.title

    def get_absolute_url(self):
        return ('history', [self.slug])

class Ticket(models.Model):
    '''
    * Denotes a mandatory field
    '''
    first_name = models.CharField("First Name", max_length=255)
    last_name = models.CharField("Last Name", max_length=255)
    email_address = models.EmailField("Email Address")
    mobile = models.IntegerField("Phone Number")
    birthday = models.DateField("Date of Birth", help_text="format: yyyy-dd-mm", auto_now=False)
    address = models.CharField("Home Address", max_length=255)
    town_city = models.CharField("Town or City", max_length=255)
    postcode = models.IntegerField("Postcode", default=10101)
    country = models.CharField("Country", max_length=255)
    # accessibility_requirements = models.CharField(max_length=255)
    priority_deposit = models.CharField("Priority Deposit", max_length=255)
    number_of_seats = models.IntegerField(default=1)
    timestamp = models.DateTimeField(auto_now_add=True)

# Please read the ZUFC Privacy Policy and for an updated list of MU Group companies & MU Commercial Partners.
    class Meta:
        verbose_name = "Ticket"
        verbose_name_plural = "Tickets"
        ordering = ["-timestamp"]

    def __unicode__(self):
        return self.first_name
