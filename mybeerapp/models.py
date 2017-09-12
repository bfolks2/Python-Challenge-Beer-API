from django.db import models
from django.core.urlresolvers import reverse
from django.utils.text import slugify #remove any characters that are not alphanuermica, /'s, or -'s
from accounts.models import User

# Create your models here.

class Glass(models.Model):
    name=models.CharField(max_length=256)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "glasses"


class Beer(models.Model):
    user=models.ForeignKey(User, related_name='beers', default=1)
    name=models.CharField(max_length=256)
    slug=models.SlugField(unique=True, allow_unicode=True, default='')
    calories=models.PositiveIntegerField()
    abv=models.DecimalField(max_digits=3, decimal_places=1)
    style=models.CharField(default="It's a beer", max_length=256)
    location=models.CharField(max_length=256)
    created_at = models.DateTimeField(auto_now=True)
    glass=models.ManyToManyField(Glass)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def _get_total_average(self):
        count=self.ratings.count()
        total=0
        for rating in self.ratings.all():
            total=total+rating.average
        if count==0:
            count=1
        return (total/count)
    total_average = property(_get_total_average)

    # def get_absolute_url(self):
    #     return reverse('mybeerapp:details', kwargs={'slug':self.slug,'username':self.user.username,'pk':self.pk})


class Rating(models.Model):

    five_choices=(
        (1,'1/5'),
        (2,'2/5'),
        (3,'3/5'),
        (4,'4/5'),
        (5,'5/5'),
    )

    ten_choices=(
        (1,'1/10'),
        (2,'2/10'),
        (3,'3/10'),
        (4,'4/10'),
        (5,'5/10'),
        (6,'6/10'),
        (7,'7/10'),
        (8,'8/10'),
        (9,'9/10'),
        (10,'10/10'),
    )

    user=models.ForeignKey(User, related_name='user_ratings', default=1)
    beer=models.ForeignKey(Beer, related_name='ratings')
    aroma=models.PositiveIntegerField(choices=five_choices)
    appearance=models.PositiveIntegerField(choices=five_choices)
    taste=models.PositiveIntegerField(choices=ten_choices) #taste is weighted

    def _get_average(self):
        return round(((self.aroma + self.appearance + self.taste)/20)*100)
    average = property(_get_average)

    def __str__(self):
        return self.beer.name + ': ' + str(self.average) + '%'
