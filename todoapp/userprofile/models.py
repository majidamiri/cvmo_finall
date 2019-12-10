from __future__ import unicode_literals
from django.conf import settings

from django.db import models
from django.utils.encoding import smart_text as smart_unicode
from django.utils.translation import ugettext_lazy as _


class FreeLancer(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        #unique=True,
        on_delete=models.CASCADE,
        #error_messages={
        #    'unique': _("A data with that username already exists."),
        #}
    )
    name = models.CharField(_("Name"), max_length=255)
    family = models.CharField(_("Family"), max_length=255)
    father_name = models.CharField(_("Father Name"), max_length=255)
    done = models.BooleanField(_("Done"), default=False)
    date_created = models.DateTimeField(_("Date Created"), auto_now_add=True)

    class Meta:
        verbose_name = _("FreeLancer")
        verbose_name_plural = _("FreeLancers")

    def __unicode__(self):
        return smart_unicode(self.name)
