# -*- coding: utf-8 -*-

from django.db import models
from django.utils.translation import ugettext_lazy as _

from .publication import Publication


class Catalog(models.Model):
    """
    Model representing a list of publications.
    """

    class Meta:
        verbose_name = _("catalog")
        verbose_name_plural = _("catalogs")
        ordering = ("title",)

    title = models.TextField(
        unique=True,
        db_index=True,
        verbose_name=_("model_field_title_verbose"),
        help_text=_("catalog_field_title_help"),
    )
    description = models.TextField(
        verbose_name=_("model_field_description_verbose"),
        help_text=_("catalog_field_description_help"),
    )
    publications = models.ManyToManyField(
        Publication,
        blank=True,
        db_index=True,
        verbose_name=_("model_fk_publications_verbose"),
        help_text=_("catalog_field_publications_help"),
    )

    def __unicode__(self):
        return self.title

    def __str__(self):
        return self.title
