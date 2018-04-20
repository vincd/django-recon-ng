# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf import settings

from .utils import is_recon_model

class ReconNGDBRouter(object):
    def db_for_read(self, model, **hints):
        """ reading SomeModel from otherdb """
        if is_recon_model(model):
            return settings.RECON_NG_DATABASE_NAME

        return None

    def db_for_write(self, model, **hints):
        """ writing SomeModel to otherdb """
        if is_recon_model(model):
            return settings.RECON_NG_DATABASE_NAME

        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        if model_name and 'model' in hints:
            model = hints['model']
            if is_recon_model(model):
                return False

        return None
