#!/usr/bin/env python3

import json
from ciscoisesdk import api

api_ = api.IdentityServicesEngineAPI(username='admin',
            password='C1sco12345',
            base_url='https://ise-1.lab.devnetsandbox.local',
            verify=False)

try:
    response = api_.network_device.get_all_network_device().response
    # response = api_.network_device.get_network_device_by_name('WLC').response

    print(json.dumps(response, indent=2))
except ApiError as e:
    print(e)
