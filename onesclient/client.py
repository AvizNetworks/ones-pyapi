# Importing neccessery modules
import logging
import json
import requests

# importing endpoints
from .endpoints import *

from .excpetions import OnesClientExpection
from .constants import *
from .util import request_handler, request_handler_with_payload, request_handler_with_query_params


# Loading Environment Variables
# from dotenv import load_dotenv
# load_dotenv()


class ONESClient(object):
    def __init__(self, username=None, password=None, url=None):
        self.username = username
        self.password = password
        self.url = url
        self.access_token = None

    def connect(self):
        """
            This method will use to make connection
            with Ones API,
            It will use user, url,password, and  Authentication API
        """
        try:
            url = self.url + connect

            payload = {"username": self.username, "password": self.password}

            payload = json.dumps(payload)
            headers = {"Content-Type": "application/json"}
            response = requests.post(
                url, data=payload, headers=headers, verify=False
            )
            if response.status_code == 200:
                temp = response.json()
                access_token = temp["data"]["token"]
                logging.debug(access_token)
                self.access_token = access_token

            else:
                logging.error("Something went wrong")

        except Exception as err:
            logging.error(f"Error -> ${err}")
            raise OnesClientExpection()

    def get_hardware_info(self):
        """
            This function will return all Hardware Info
            Includes the following Details
            Devices, Regions, SwitchSKUs, Role and ASICs
        """
        try:
            url = self.url + hardware_info
            headers = {
                "Authorization": self.access_token,
                "Content-Type": "application/json",
            }
            response = requests.get(url, headers=headers, verify=False)
            if response.status_code == 200:
                res = response.json()
                print(json.dumps(res, indent=4))
                return True
            else:
                raise OnesClientExpection(HARDWARE_INFO_ERROR)

        except Exception as err:
            logging.error(f"Error -> ${err}")
            raise OnesClientExpection(HARDWARE_INFO_ERROR)

        
    def get_roles(self):
        """
        This function will return all existings roles
                Spine
                SuperSpine
                Tor
                Leaf
        """
        try:
            url = self.url + roles
            headers = {
                "Authorization": self.access_token,
                "Content-Type": "application/json",
            }
            response = requests.get(url, headers=headers, verify=False)
            if response.status_code == 200:
                res = response.json()
                print(json.dumps(res, indent=4))
                return True
        except Exception as err:
            logging.error(err)
            raise OnesClientExpection(ROLES_ERROR)
        
    def get_switch_skus(self):
        """
        Return all switch SKUs
        """
        request_handler(self.url, switch_skus, self.access_token, None)

    def get_asics_info(self):
        """
        Return all ASICs info
        """
        request_handler(self.url, asics, self.access_token, None)

    def get_agent_version(self):
        """
        Return Agent version
        """
        request_handler(self.url, agent_version, self.access_token, None)

    def get_nos_version(self):
        """
        Return NOS version
        """
        request_handler(self.url, nos_version, self.access_token, None)

    def get_linux_version(self):
        """
        Return linux version
        """
        request_handler(self.url, linux_version, self.access_token, None)

    def get_onie_version(self):
        """
        Return ONIE version
        """
        request_handler(self.url, onie_version, self.access_token, None)

    def get_cabling_info(self):
        """
        Return cabling INFO
        """
        request_handler(self.url, cabling, self.access_token, None)

    def get_device_interfaces(self, arg1):
        """
        Payload -> "filter": {
                 "deviceAddress": "0c:29:ef:ce:92:20"
                }
        Output -> List of interfaces of a device
        """
        request_handler_with_payload(self.url, device_interfaces, self.access_token, None, arg1)

    def get_device_peripherals(self, arg1):
        """
        query_params -> "filter": {
                    {
                    "deviceAddress" : "0c:29:ef:ce:92:20"
                    }
            }
        Output -> List of peripherals
        """
        request_handler_with_query_params(self.url, device_peripherals, self.access_token, None, arg1)

    def get_device_info(self,arg1):
        """
        query_params -> {"ipAddress": "10.4.4.61"}
        Output -> List of device info
        """
        request_handler_with_query_params(self.url, device_info_endpoint, self.access_token,None, arg1)

        
    def get_network_topology(self):
        """
        Output -> List of device info
        """
        request_handler(self.url, network_topology, self.access_token,None)

    def get_faulty_psus(self):
        """
        output -> list of devices and connections
        """
        request_handler(self.url, faulty_psus,self.access_token, None)
        
    def get_faulty_fans(self):
        """
        Return Fan List
        """
        request_handler(self.url, faulty_fans, self.access_token, None)
        
    def get_link_flaps(self, arg1):
        """
        Return interface status
        """
        request_handler_with_query_params(self.url, link_flaps, self.access_token, None, arg1)
        
    def get_cpu_utilization(self, arg1):
        """
        query_params -> {
            "fromDate" : "2023-05-12 11:55:24",
            "toDate" : "2023-05-12 12:55:24",
            "deviceAddress" : "10.4.4.55"
        }
        """
        request_handler_with_query_params(self.url, cpu_utilization, self.access_token, None, arg1)
        
    def get_memory_utilization(self, arg1):
        """
        query_params -> {
            "fromDate" : "2023-05-12 11:55:24",
            "toDate" : "2023-05-12 12:55:24",
            "deviceAddress" : "10.4.4.55"
        }
        """
        request_handler_with_query_params(self.url, memory_utilization, self.access_token, None, arg1)
        
    def get_cpu_core_temperaure(self, arg1):
        """
        query_params -> {
            "fromDate" : "2023-05-12 11:55:24",
            "toDate" : "2023-05-12 12:55:24",
            "deviceAddress" : "10.4.4.55"
        }
        """
        request_handler_with_query_params(self.url, cpu_core_temperaure, self.access_token, None, arg1)
        
    def get_psu_temperature(self, arg1):
        """ 
        query_params -> {
            "fromDate" : "2023-05-12 11:55:24",
            "toDate" : "2023-05-12 12:55:24",
            "deviceAddress" : "10.4.4.55"
        }
        """
        request_handler_with_query_params(self.url, psu_temperature, self.access_token, None, arg1)
        
    def get_psu_voltage(self, arg1):
        """ 
        query_params -> {
            "fromDate" : "2023-05-12 11:55:24",
            "toDate" : "2023-05-12 12:55:24",
            "deviceAddress" : "10.4.4.55"
        }
        """
        request_handler_with_query_params ( self.url, psu_voltage, self.access_token, None, arg1)
        
    def get_psu_current(self, arg1):
        """ 
        query_params -> {
           "fromDate" : "2023-05-12 11:55:24",
           "toDate" : "2023-05-12 12:55:24",
           "deviceAddress" : "10.4.4.55"
        }
        """
        request_handler_with_query_params(self.url, psu_current, self.access_token, None, arg1)
        
    def get_fan_speed(self, arg1):
        """ 
        query_params -> {
            "fromDate" : "2023-05-12 11:55:24",
            "toDate" : "2023-05-12 12:55:24",
            "deviceAddress" : "10.4.4.55"
        }
        """
        request_handler_with_query_params(self.url, fan_speed, self.access_token, None, arg1)
        
    def get_psu_power(self, arg1):
        """ 
        query_params -> {
            "fromDate" : "2023-05-12 11:55:24",
            "toDate" : "2023-05-12 12:55:24",
            " deviceAddress" : "10.4.4.55"
        }
        """
        request_handler_with_query_params(self.url, psu_power, self.access_token, None, arg1)
        
    def get_health_services_cpu(self, arg1):
        """ 
        query_params -> {
            "fromDate" : "2023-05-12 11:55:24",
            "toDate" : "2023-05-12 12:55:24",
            "deviceAddress" : "10.4.4.55"
        }
        """
        request_handler_with_query_params(self.url, health_services_cpu, self.access_token, None, arg1)
        
    def get_health_services_memory(self, arg1):
        """ 
        query_params -> {
            "fromDate" : "2023-05-12 11:55:24",
            "toDate" : "2023-05-12 12:55:24",
            "deviceAddress" : "10.4.4.55"
        }
        """
        request_handler_with_query_params(self.url, health_services_memory, self.access_token, None, arg1)
        
    def get_health_bgp_neighbors(self, arg1):
        """ 
        query_params -> {
            "fromDate" : "2023-04-04 04:54:27",
            "toDate" : "2023-04-04 05:54:27",
            "deviceAddress" : "10.4.4.55"
        }
        """
        request_handler_with_query_params(self.url, health_bgp_neighbors, self.access_token, None, arg1)
     
    def get_health_trancievers(self, arg1):
        """ 
        query_params -> {
            "ipAddress" : "10.4.4.55",
            "ifName" : "Ethernet0",
            "fromDate" : "2023-06-26 10:48:55",
            "toDate" : "2023-06-26 11:48:55"
        }
        """    
        request_handler_with_query_params(self.url, health_transcievers, self.access_token, None, arg1)
        
    def get_health_running_services(self, arg1):
        """ 
        query_params -> {
                    "fromDate" : "2023-05-12 11:55:24",
                    "toDate" : "2023-05-12 12:55:24",
                    "deviceAddress" : "10.4.4.55"
        }
        """
        request_handler_with_query_params(self.url, health_running_services, self.access_token, None, arg1)
    
    def get_traffic_util(self, arg1):
        """ 
        query_params -> "filter" : {
            {
                "fromDate" : "2023-04-04 04:54:27",
                "toDate" : "2023-04-04 05:54:27",
                "deviceAddress" : "10.4.4.55",
                "ifname" : "Ethernet0"
            }
        }
        """
        request_handler_with_query_params(self.url, traffic_util, self.access_token, None, arg1)
        
    def get_traffic_counters(self, arg1):
        """ 
        query_params -> "filter" : {
            {
                "fromDate" : "2023-04-04 04:54:27",
                "toDate" : "2023-04-04 05:54:27",
                "deviceAddress" : "10.4.4.55",
                "ifname" : "Ethernet0"
            }
        }
        """
        request_handler_with_query_params(self.url, traffic_counters, self.access_token, None, arg1)
        
            
        
        
    
