#!/usr/bin/python

# (c) Copyright 2016 Hewlett Packard Enterprise Development Company LP
#
# Licensed under the Apache License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.
#

import sys

networks = [
    {
      "bridge_port": "bond0",
      "device": "br-bond0",
      "address": "192.168.10.5",
      "network": "MANAGEMENT-NET",
      "tags": [
        {
          "data_values": {
            "provider-physical-network": "physnet1"
          },
          "tag": "neutron.networks.vlan",
          "component": "neutron-openvswitch-agent",
          "service": "neutron"
        }
      ]
    },
    {
      "bridge_port": "vlan102",
      "device": "br-vlan102",
      "address": None,
      "network": "EXTERNAL-VM-NET",
      "tags": [
        {
          "data_values": None,
          "tag": "neutron.l3_agent.external_network_bridge",
          "component": "neutron-vpn-agent",
          "service": "neutron"
        }
      ]
    },
    {
      "device": "vlan103",
      "address": "10.1.1.4",
      "network": "GUEST-NET",
      "tags": [
        {
          "data_values": None,
          "tag": "neutron.networks.vxlan",
          "component": "neutron-openvswitch-agent",
          "service": "neutron"
        }
      ]
    },
    {
      "device": "vlan106",
      "address": "10.1.1.34",
      "network": "GUEST-NET",
      "tags": [
        {
          "data_values": None,
          "tag": "vsa.iscsi",
          "component": "neutron-openvswitch-agent",
          "service": "neutron"
        }
      ]
    },
    {
      "device": "vlan206",
      "address": "10.1.1.84",
      "network": "GUEST-NET",
      "tags": [
        {
          "data_values": None,
          "tag": "vsa.iscsi",
          "component": "neutron-openvswitch-agent",
          "service": "neutron"
        }
      ]
    }
  ]


def extra_network_attr(networks, attribute, tag='vsa.iscsi'):
    """Extract network attribute if it is marked with
    specific tag.

    :param networks: list of networks to be searched for a tag
    :param attribute: attribute name for which value needs to be extracted
    :param tag: tag name for which enquiry need to be made

    :return: None if failed else value of attribute
    """
    for net in networks:
        for e in net['tags']:
            if e['tag'] == tag and attribute in net:
                return net[attribute]

if __name__ == "__main__":
    result = extra_network_attr(networks, attribute='device')
    print(result)
