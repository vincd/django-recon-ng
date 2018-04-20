# -*- coding: utf-8 -*-

from .models import ReconBaseModel

def is_recon_model(model):
    return issubclass(model, ReconBaseModel)
