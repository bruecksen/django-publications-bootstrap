# -*- coding: utf-8 -*-

from django.db import models
from django.utils.translation import ugettext_lazy as _

from ..models import Publication


class Citation(models.Model):
    """Model representing a citation"""

    class Meta:
        verbose_name = _("citation")
        verbose_name_plural = _("citations")

    citekey = models.CharField(
        max_length=256,
        blank=False,
        null=False,
        db_index=True,
        verbose_name=_("citation_field_citekey_verbose"),
        help_text=_("citation_field_citekey_help"),
    )
    field_name = models.CharField(
        max_length=256,
        blank=False,
        null=False,
        db_index=True,
        verbose_name=_("citation_field_fieldname_verbose"),
        help_text=_("citation_field_fieldname_help"),
    )
    publication = models.ForeignKey(
        Publication,
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
        verbose_name=_("model_fk_publication_verbose"),
        help_text=_("citation_field_publication_help"),
    )

    def __repr__(self):
        return "<Citation citekey=%r field_name=%r publication=%r>" % (
            self.citekey,
            self.field_name,
            self.publication,
        )

    def __unicode__(self):
        return u"[%s]" % self.citekey
