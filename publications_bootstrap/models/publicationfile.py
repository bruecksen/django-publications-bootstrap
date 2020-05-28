# -*- coding: utf-8 -*-

from django.db import models
from django.utils.translation import ugettext_lazy as _

from ..models import Publication


class PublicationFile(models.Model):
    class Meta:
        verbose_name = _("publicationfile")
        verbose_name_plural = _("publicationfiles")

    file = models.FileField(
        upload_to="publications_bootstrap/",
        verbose_name=_("model_field_file_verbose"),
        help_text=_("publicationfile_field_file_help"),
    )
    description = models.TextField(
        verbose_name=_("model_field_description_verbose"),
        help_text=_("catalog_field_publications_help"),
    )
    publication = models.ForeignKey(
        Publication,
        on_delete=models.CASCADE,
        verbose_name=_("model_fk_publication_verbose"),
        help_text=_("publicationfile_field_publication_help"),
    )

    def __unicode__(self):
        return self.description

    def __str__(self):
        return self.description
