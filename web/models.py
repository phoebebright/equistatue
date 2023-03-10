from urllib.request import urlopen

from django.db import models
from django_random_queryset import RandomManager
from galleryfield.fields import GalleryField
from django.utils.translation import ugettext_lazy as _
from django.utils import timezone

class WebPage(models.Model):
    '''Store pages being scraped so only need to get them once'''
    url = models.CharField(max_length=250)
    content = models.TextField(blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)

    @classmethod
    def get_or_create(cls, url):

        if not 'http' in url:
            url = 'http://' + url

        try:
            page = cls.objects.get(url=url)
            return page.content
        except cls.DoesNotExist:
            page_html = urlopen(url).read()
            x = type(page_html)
            print("Type %s" % x)
            print("Loading page from internet")

            #content = page_html.decode('iso-8859-1').encode('utf-8')
            content = page_html.decode('utf-8')
            cls.objects.create(url=url, content=content)
            return page_html


class Statue(models.Model):

    name = models.CharField(max_length=100)
    # main_image = models.ImageField(blank=True, null=True)
    main_image_url = models.URLField(blank=True, null=True)
    details_url = models.URLField(blank=True, null=True)
    other_img_url = models.URLField(blank=True, null=True)
    sculptor = models.CharField(max_length=100)
    year = models.CharField(max_length=10, blank=True, null=True)
    country = models.CharField(max_length=50, blank=True, null=True)
    location = models.CharField(max_length=50, blank=True, null=True)
    original = models.CharField(max_length=50, blank=True, null=True)
    skip = models.BooleanField(default=False)
    servant_partner = models.IntegerField(default=99)
    happy_horse = models.IntegerField(default=0, help_text=_("1 Yes, -1 No, 0 Unscored"))
    gallery = GalleryField(blank=True, null=True)
    notes = models.TextField(blank=True, null=True)
    updated = models.DateTimeField(blank=True, null=True)
    objects = RandomManager()

    def __str__(self):
        return f"{self.name} - {self.location},{self.country}"

    def save(self, *args, **kwargs):

        self.updated = timezone.now()
        super().save(*args, **kwargs)

class LikeDislike(models.Model):
    statue = models.ForeignKey(Statue, on_delete=models.CASCADE)
    score = models.SmallIntegerField(default=0, help_text=_("-1 for dislike, 1 for like, 0 for don't know"))
    created = models.DateTimeField(auto_created=True)

    def __str__(self):
        return f"{self.pk} - {self.statue} - {self.score}"

class Subscribe(models.Model):
    email = models.EmailField(unique=True)
    created = models.DateTimeField(auto_created=True)


