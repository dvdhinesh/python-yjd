YJD Python API
==============

Python library to connect to YJD Webservices.

Usage
-----

.. code-block:: python

	import yjd

	wsdl = 'http://www.example.com/Service.asmx?WSDL'

	# Create an instance of API
	ws = yjd.YjdAPI(wsdl)

	# Build Security Header.
	headerType = ws.client.get_element('ns0:SecurityHeader')
	header = headerType(SecurityKey='your-security-key')
	ws.set_header(header)

	# Get WSDL dump.
	ws.get_dump()

	# Build SKU data.
	sku_data = {
	    'DocHeader': {
	    },
	    'Details': {
	    }
	}
	ws.sku_submit(sku_data)

	# Build ASN data.
	asn_data = {
	    'DocHeader': {
	    },
	    'Header': {
	    },
	    'Parties': {
	        'Party': {
	        }
	    },
	    'Details': {
	        'AsnDetail': {
	        }
	    }
	}
	ws.asn_submit(asn_data)

	# Supports Context Managers.
	with yjd.YjdAPI(wsdl) as connection:
	    connection.get_dump()


License
-------

MIT

See LICENSE for more details
