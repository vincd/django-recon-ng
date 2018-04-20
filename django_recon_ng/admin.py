# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import ReconDomains, ReconCompanies, ReconNetblocks, ReconLocations, ReconVulnerabilities, ReconPorts, ReconHosts, ReconContacts, ReconCredentials, ReconLeaks, ReconPushpins, ReconProfiles, ReconRepositories, ReconDashboard

admin.site.register(ReconDomains)
admin.site.register(ReconCompanies)
admin.site.register(ReconNetblocks)
admin.site.register(ReconLocations)
admin.site.register(ReconVulnerabilities)
admin.site.register(ReconPorts)
admin.site.register(ReconHosts)
admin.site.register(ReconContacts)
admin.site.register(ReconCredentials)
admin.site.register(ReconLeaks)
admin.site.register(ReconPushpins)
admin.site.register(ReconProfiles)
admin.site.register(ReconRepositories)
admin.site.register(ReconDashboard)
