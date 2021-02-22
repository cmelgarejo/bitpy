from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.utils import timezone
from datetime import timedelta
from hashid_field import HashidField, Hashid


def tomorrow():
    return timezone.now() + timedelta(days=1)


def default_hashid():
    return Hashid(int(timezone.now().timestamp()))


class Shrt(models.Model):
    url = models.CharField(max_length=1024)
    shrt = models.CharField(default=default_hashid, max_length=64, unique=True)
    active = models.BooleanField(default=True)
    expires_at = models.DateTimeField(_('expires_at'), default=tomorrow)
    created_at = models.DateTimeField(_('created_at'), default=timezone.now)
