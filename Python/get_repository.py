#!/usr/bin/env python3

import json
from ciscoisesdk import api

api_ = api.IdentityServicesEngineAPI(username='admin',
            password='C1sco12345',
            base_url='https://ise-1.lab.devnetsandbox.local',
            verify=False)

try:
    response = api_.repository.get_repositories().response
    # response = api_.repository.get_repository_by_name('WindowsServerFTP').response


    print(json.dumps(response, indent=2))
except ApiError as e:
    print(e)
