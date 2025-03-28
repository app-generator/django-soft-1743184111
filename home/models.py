# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

# Create your models here.

class UserProfile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    #__PROFILE_FIELDS__

    #__PROFILE_FIELDS__END

    def __str__(self):
        return self.user.username
    
    class Meta:
        verbose_name        = _("UserProfile")
        verbose_name_plural = _("UserProfile")

#__MODELS__
class Verbale(models.Model):

    #__Verbale_FIELDS__
    cronologico = models.ForeignKey(Accertatori, on_delete=models.CASCADE)
    spv = models.IntegerField(null=True, blank=True)
    data = models.DateTimeField(blank=True, null=True, default=timezone.now)
    ora = models.DateTimeField(blank=True, null=True, default=timezone.now)
    luogo = models.TextField(max_length=255, null=True, blank=True)
    tipo veicolo = models.CharField(max_length=255, null=True, blank=True)

    #__Verbale_FIELDS__END

    class Meta:
        verbose_name        = _("Verbale")
        verbose_name_plural = _("Verbale")


class Accertatori(models.Model):

    #__Accertatori_FIELDS__
    nome = models.CharField(max_length=255, null=True, blank=True)
    cognome = models.CharField(max_length=255, null=True, blank=True)
    matricola = models.IntegerField(null=True, blank=True)

    #__Accertatori_FIELDS__END

    class Meta:
        verbose_name        = _("Accertatori")
        verbose_name_plural = _("Accertatori")



#__MODELS__END
