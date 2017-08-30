from django.db import models
from django.core.urlresolvers import reverse
from django.utils.text import slugify #remove any characters that are not alphanuermica, /'s, or -'s

# Create your models here.

class Glass(models.Model):
    name=models.CharField(max_length=256)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "glasses"


class Beer(models.Model):
    name=models.CharField(max_length=256)
    slug=models.SlugField(unique=True, allow_unicode=True, default='')
    calories=models.PositiveIntegerField()
    abv=models.DecimalField(max_digits=3, decimal_places=1)
    style=models.CharField(default="It's a beer", max_length=256)
    location=models.CharField(max_length=256)
    glass=models.ManyToManyField(Glass)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('mybeerapp:details', kwargs={'slug':self.slug})


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

    aroma=models.PositiveIntegerField(choices=five_choices)
    appearance=models.PositiveIntegerField(choices=five_choices)
    taste=models.PositiveIntegerField(choices=ten_choices) #taste is weighted
    palate=models.PositiveIntegerField(choices=five_choices)
    bottle_style=models.PositiveIntegerField(choices=five_choices)
    beer=models.ForeignKey(Beer, related_name='ratings')

    def _get_average(self):
        return round(((self.aroma + self.appearance + self.taste + self.palate + self.bottle_style)/30)*100)
    average = property(_get_average)

    def __str__(self):
        return str(self.average)
