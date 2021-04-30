from django.db.models import CharField
from django.utils.translation import ugettext_lazy as _
from django.db import models


# ------------------------------------------------------------------------
# Movie Model
# ------------------------------------------------------------------------


class Movie(models.Model):

    name = CharField(_("Movie name"), blank=True, max_length=255)
    rating = CharField(_("Movie rating"), blank=True, max_length=255)
    description = models.TextField(_("Movie description"), blank=True, max_length=255)
    release_date = models.DateField(_("Movie release date"), blank=True, max_length=255)
    duration = CharField(_("Movie duration"), blank=True, max_length=255)
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True, null=True)

    class Meta:
        verbose_name = "Movie"
        verbose_name_plural = "Movies"

    def __str__(self):
        return "{0}".format(self.name)