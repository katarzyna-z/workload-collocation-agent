# Copyright (c) 2019 Intel Corporation
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from wca.config import register
from wca.scheduler.algorithms.ffd_generic import FFDGeneric
from wca.scheduler.data_providers.prometheus_data_provider import PrometheusDataProvider


def register_algorithms():
    register(FFDGeneric)


def register_dataproviders():
    register(PrometheusDataProvider)
