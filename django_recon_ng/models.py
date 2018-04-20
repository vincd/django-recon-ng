# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.utils.encoding import python_2_unicode_compatible

from django.db import models

class ReconBaseModel(models.Model):
    id = models.IntegerField(primary_key=True, db_column='rowid')

    class Meta:
        abstract = True


@python_2_unicode_compatible
class ReconDomains(ReconBaseModel):
    class Meta:
        verbose_name = 'Recon-ng Domain'
        verbose_name_plural = 'Recon-ng Domains'
        db_table = 'domains'

    domain = models.TextField()
    module = models.TextField()

    def __str__(self):
        return '<ReconDomains: %s, %s>' % (self.domain, self.module)


@python_2_unicode_compatible
class ReconCompanies(ReconBaseModel):
    class Meta:
        verbose_name = 'Recon-ng Companie'
        verbose_name_plural = 'Recon-ng Companies'
        db_table = 'companies'

    company = models.TextField()
    description = models.TextField()
    module = models.TextField()

    def __str__(self):
        return '<ReconCompanies: %s, %s, %s>' % (self.company, self.description, self.module)


@python_2_unicode_compatible
class ReconNetblocks(ReconBaseModel):
    class Meta:
        verbose_name = 'Recon-ng Netblock'
        verbose_name_plural = 'Recon-ng Netblocks'
        db_table = 'netblocks'

    netblock = models.TextField()
    module = models.TextField()

    def __str__(self):
        return '<ReconNetblocks: %s, %s>' % (self.netblock, self.module)


@python_2_unicode_compatible
class ReconLocations(ReconBaseModel):
    class Meta:
        verbose_name = 'Recon-ng Location'
        verbose_name_plural = 'Recon-ng Locations'
        db_table = 'locations'

    latitude = models.TextField()
    longitude = models.TextField()
    street_address = models.TextField()
    module = models.TextField()

    def __str__(self):
        return '<ReconLocations: %s, %s, %s, %s>' % (self.latitude, self.longitude, self.street_address, self.module)


@python_2_unicode_compatible
class ReconVulnerabilities(ReconBaseModel):
    class Meta:
        verbose_name = 'Recon-ng Vulnerabilitie'
        verbose_name_plural = 'Recon-ng Vulnerabilities'
        db_table = 'vulnerabilities'

    host = models.TextField()
    reference = models.TextField()
    example = models.TextField()
    publish_date = models.TextField()
    category = models.TextField()
    status = models.TextField()
    module = models.TextField()

    def __str__(self):
        return '<ReconVulnerabilities: %s, %s, %s, %s, %s, %s, %s>' % (self.host, self.reference, self.example, self.publish_date, self.category, self.status, self.module)


@python_2_unicode_compatible
class ReconPorts(ReconBaseModel):
    class Meta:
        verbose_name = 'Recon-ng Port'
        verbose_name_plural = 'Recon-ng Ports'
        db_table = 'ports'

    ip_address = models.TextField()
    host = models.TextField()
    port = models.TextField()
    protocol = models.TextField()
    module = models.TextField()

    def __str__(self):
        return '<ReconPorts: %s, %s, %s, %s, %s>' % (self.ip_address, self.host, self.port, self.protocol, self.module)


@python_2_unicode_compatible
class ReconHosts(ReconBaseModel):
    class Meta:
        verbose_name = 'Recon-ng Host'
        verbose_name_plural = 'Recon-ng Hosts'
        db_table = 'hosts'

    host = models.TextField()
    ip_address = models.TextField()
    region = models.TextField()
    country = models.TextField()
    latitude = models.TextField()
    longitude = models.TextField()
    module = models.TextField()

    def __str__(self):
        return '<ReconHosts: %s, %s, %s, %s, %s, %s, %s>' % (self.host, self.ip_address, self.region, self.country, self.latitude, self.longitude, self.module)


@python_2_unicode_compatible
class ReconContacts(ReconBaseModel):
    class Meta:
        verbose_name = 'Recon-ng Contact'
        verbose_name_plural = 'Recon-ng Contacts'
        db_table = 'contacts'

    first_name = models.TextField()
    middle_name = models.TextField()
    last_name = models.TextField()
    email = models.TextField()
    title = models.TextField()
    region = models.TextField()
    country = models.TextField()
    module = models.TextField()

    def __str__(self):
        return '<ReconContacts: %s, %s, %s, %s, %s, %s, %s, %s>' % (self.first_name, self.middle_name, self.last_name, self.email, self.title, self.region, self.country, self.module)


@python_2_unicode_compatible
class ReconCredentials(ReconBaseModel):
    class Meta:
        verbose_name = 'Recon-ng Credential'
        verbose_name_plural = 'Recon-ng Credentials'
        db_table = 'credentials'

    username = models.TextField()
    password = models.TextField()
    hash = models.TextField()
    type = models.TextField()
    leak = models.TextField()
    module = models.TextField()

    def __str__(self):
        return '<ReconCredentials: %s, %s, %s, %s, %s, %s>' % (self.username, self.password, self.hash, self.type, self.leak, self.module)


@python_2_unicode_compatible
class ReconLeaks(ReconBaseModel):
    class Meta:
        verbose_name = 'Recon-ng Leak'
        verbose_name_plural = 'Recon-ng Leaks'
        db_table = 'leaks'

    leak_id = models.TextField()
    description = models.TextField()
    source_refs = models.TextField()
    leak_type = models.TextField()
    title = models.TextField()
    import_date = models.TextField()
    leak_date = models.TextField()
    attackers = models.TextField()
    num_entries = models.TextField()
    score = models.TextField()
    num_domains_affected = models.TextField()
    attack_method = models.TextField()
    target_industries = models.TextField()
    password_hash = models.TextField()
    password_type = models.TextField()
    targets = models.TextField()
    media_refs = models.TextField()
    module = models.TextField()

    def __str__(self):
        return '<ReconLeaks: %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s>' % (self.leak_id, self.description, self.source_refs, self.leak_type, self.title, self.import_date, self.leak_date, self.attackers, self.num_entries, self.score, self.num_domains_affected, self.attack_method, self.target_industries, self.password_hash, self.password_type, self.targets, self.media_refs, self.module)


@python_2_unicode_compatible
class ReconPushpins(ReconBaseModel):
    class Meta:
        verbose_name = 'Recon-ng Pushpin'
        verbose_name_plural = 'Recon-ng Pushpins'
        db_table = 'pushpins'

    source = models.TextField()
    screen_name = models.TextField()
    profile_name = models.TextField()
    profile_url = models.TextField()
    media_url = models.TextField()
    thumb_url = models.TextField()
    message = models.TextField()
    latitude = models.TextField()
    longitude = models.TextField()
    time = models.TextField()
    module = models.TextField()

    def __str__(self):
        return '<ReconPushpins: %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s>' % (self.source, self.screen_name, self.profile_name, self.profile_url, self.media_url, self.thumb_url, self.message, self.latitude, self.longitude, self.time, self.module)


@python_2_unicode_compatible
class ReconProfiles(ReconBaseModel):
    class Meta:
        verbose_name = 'Recon-ng Profile'
        verbose_name_plural = 'Recon-ng Profiles'
        db_table = 'profiles'

    username = models.TextField()
    resource = models.TextField()
    url = models.TextField()
    category = models.TextField()
    notes = models.TextField()
    module = models.TextField()

    def __str__(self):
        return '<ReconProfiles: %s, %s, %s, %s, %s, %s>' % (self.username, self.resource, self.url, self.category, self.notes, self.module)


@python_2_unicode_compatible
class ReconRepositories(ReconBaseModel):
    class Meta:
        verbose_name = 'Recon-ng Repositorie'
        verbose_name_plural = 'Recon-ng Repositories'
        db_table = 'repositories'

    name = models.TextField()
    owner = models.TextField()
    description = models.TextField()
    resource = models.TextField()
    category = models.TextField()
    url = models.TextField()
    module = models.TextField()

    def __str__(self):
        return '<ReconRepositories: %s, %s, %s, %s, %s, %s, %s>' % (self.name, self.owner, self.description, self.resource, self.category, self.url, self.module)


@python_2_unicode_compatible
class ReconDashboard(ReconBaseModel):
    class Meta:
        verbose_name = 'Recon-ng Dashboar'
        verbose_name_plural = 'Recon-ng Dashboard'
        db_table = 'dashboard'

    module = models.TextField()
    runs = models.IntegerField()

    def __str__(self):
        return '<ReconDashboard: %s, %s>' % (self.module, self.runs)
