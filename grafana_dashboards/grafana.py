# Copyright 2015 Red Hat, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.

import json
import requests


class Grafana(object):
    def __init__(self, url, key):
        self.url = url
        self.session = requests.Session()
        self.session.headers.update({
            'Authorization': 'Bearer %s' % key,
        })

    def create_dashboard(self, data, overwrite=False):
        data['overwrite'] = overwrite
        headers = {
            'Content-Type': 'application/json',
        }
        res = self.session.post(
            self.url, data=json.dumps(data), headers=headers)
        res.raise_for_status()