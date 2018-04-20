# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from .models import ReconDomains, ReconHosts
from core.utils import prettify_json

def recon_graph(request):
    data = []
    links = []

    for host in ReconHosts.objects.all():
        host_name = host.host
        host_id = 'hosts_%s' % host.id

        data.append({'id': host_id, 'label': host_name})

    for domain in ReconDomains.objects.all():
        domain_id = 'domains_%s' % domain.id
        domain_name = domain.domain
        data.append({'id': domain_id, 'label': domain_name})

        hosts = ReconHosts.objects.filter(host__endswith='.' + domain.domain)
        for h in hosts:
            links.append({ 'from': domain_id, 'to': 'hosts_%s' % h.id, 'color':{'color':'red'}})

    return render(request, 'recon/graph.html', context={
        'data': prettify_json(data),
        'links': prettify_json(links),
    })