# -*- coding: utf-8 -*-

from django.db import models
from django.utils.translation import ugettext_lazy as _

from ..models import Publication


class PublicationLink(models.Model):
    class Meta:
        verbose_name = _("publicationlink")
        verbose_name_plural = _("publicationlinks")

    url = models.URLField(
        verbose_name=_("publicationlink_field_url_verbose"),
        help_text=_("publicationlink_field_url_help"),
    )
    external = models.BooleanField(
        default=False,
        db_index=True,
        verbose_name=_("model_field_external_verbose"),
        help_text=_("publicationlink_field_external_help"),
    )
    description = models.TextField(
        verbose_name=_("model_fk_publication_verbose"),
        help_text=_("publicationfile_field_publication_help"),
    )
    publication = models.ForeignKey(
        Publication,
        on_delete=models.CASCADE,
        verbose_name=_("model_fk_publication_verbose"),
        help_text=_("publicationlink_field_publication_help"),
    )

    def __unicode__(self):
        return self.description

    def __str__(self):
        return self.description
