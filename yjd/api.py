# -*- coding: utf-8 -*-
'''
    yjd.api

    Generic API for YJD

    :license: MIT, see LICENSE for more details
'''
from zeep import Client
from zeep.cache import SqliteCache
from zeep.transports import Transport


class YjdAPI(object):

    def __init__(self, wsdl):
        if not wsdl:
            raise ValueError("No URL given for the wsdl")
        self.transport = Transport(cache=SqliteCache())
        self.client = Client(wsdl, transport=self.transport)

    def get_dump(self):
        return self.client.wsdl.dump()

    def set_header(self, header):
        if not header:
            raise ValueError("No header specified")
        self.client.set_default_soapheaders([header])

    def asn_submit(self, asn_data):
        if not asn_data:
            raise ValueError("No ASN details specified")
        response = self.client.service.AsnSubmit(asn=[asn_data])
        return response

    def order_status_update(self):
        raise NotImplementedError

    def order_submit(self):
        raise NotImplementedError

    def order_trans_plan(self):
        raise NotImplementedError

    def ownership_transfer(self):
        raise NotImplementedError

    def sku_submit(self, sku_data):
        if not sku_data:
            raise ValueError("No SKU details specified")
        response = self.client.service.SkuSubmit(sku=[sku_data])
        return response
