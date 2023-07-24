"""
Copyright (c) 2023, Aviz Networks

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

from endpoints import *
from exceptions import *
from constants import *
from utils import get_request_handler, post_request_handler
import requests
import logging

class FMClient(object):
    """
    FMClient will use for all Orchestration/ 
    Configuration related operations

    Since FM APIs is not returning any status
    Directly sending response
    """

    def __init__(self, url=None):
        self.url = url


    def get_controller_version(self):
        """
        Input params -> None
        Output -> return controller version
        """
        return get_request_handler(self.url, controller_version_endpoint, CONTROLLER_VERSION_INFO_ERROR, None)


    def get_intent_status(self, intent_name_file):
        """
        Api to retrieve over all status for the given intent yaml file. 
        This provides data to data grid which shows sub intent specific status single tick 
        and double tick \

        Query pararms - > intentName= .yamlfile
        """
        return get_request_handler(self.url, intent_status_endpoint, INTENT_STATUS_ERROR, intent_name_file)


    def reboot(self, list_of_ips):
        """
        To trigger the reboot request

        Method -> Post
        Payload -> list of IPs -> ["10.x.x.1","11.x.x.2"]
        """
        return post_request_handler(self.url, reboot_endpoint, REBOOT_ERROR, list_of_ips)
        

    def ztp_enable(self, list_of_ips):
        """
        Trigger the ZTP, it take one more device IPs as input

        Method -> Post 
        Payload -> list of IPs -> ["10.x.x.1","11.x.x.2"]
        """
        return post_request_handler(self.url, ztp_enable_endpoint, ZTP_ENABLE_ERROR, list_of_ips)


    def controller_fm_version(self, list_of_ips):
        """
        To get the Controller version and FM agent version
        Method -> Post 
        Payload -> list of IPs -> ["10.x.x.1","11.x.x.2"]
        """
        return post_request_handler(self.url, controller_fm_version_endpoint, CONTROLLER_VERSION_INFO_ERROR, list_of_ips)


    def get_image_mgmnt_status(self, list_of_ips):
        """
        Get ongoing reboot and image upgrade status, 
        this will help in selecting particular device from grid.
        Method -> Post
        Payload -> list of IPs -> ["10.x.x.1","11.x.x.2"]
        """
        return post_request_handler(self.url, image_mgmnt_status_endpoint, IMG_MGMNT_ERROR, list_of_ips)


    def custom_image_upgrade(self, payload):
        """
        To Trigger custom Image upgrade request
        Method -> Post
        payload -> [{"ip":"1.x.x.x","pathToImage":"path_of_image"}]
        """
        return post_request_handler(self.url, custom_image_upgrade_endpoint, payload)


    def get_config_diff(self, ip_address):
        """
        To get the data to show in config diff in UI, this getting called
        payload -> { "ip": "10.x.x.x"}
        """
        return post_request_handler(self.url, config_diff_endpoint, CONFIG_DIFF_ERROR, ip_address)
    
    def backup_config_endpoint(self, payload):
        """ 
        To take backup on cofiguration
        Method -> Post
        payload -> [{"ip":"10.x.x.1","label":"kuldip created13"}]
        """
        return post_request_handler(self.url, backup_config_endpoint, BACKUP_CONFIG_ERROR, payload)
    
    def configs_list_to_restore_endpoint(self, list_of_ips):
        """ 
        List of all available backup configuration snapshots.
        Method -> Post
        Payload -> list of IPs -> ["10.x.x.12","10.x.x.11"]
        """
        return post_request_handler(self.url, configs_list_to_restore_endpoint, CONFIGS_LIST_RESTORE_ERROR, list_of_ips)
    
    def restore_config_endpoint(self, payload):
        """ 
        To restoring the specific configuration on the target device/s.
        Method -> Post
        Payload -> [{"ip":"10.x.x.12","timestamp":"USERINPUT"},
                    {"ip":"10.x.x.11","timestamp":"USERINPUT"}]
        """
        return post_request_handler(self.url, restore_config_endpoint, RESTORE_CONFIG_ERROR, payload)
    
    # Generate and Apply Config

    def upload_image(self, template_path):
        """
        This API will take a YAML template as input to automatically generate the network configuration for the following 
        deployments, validate the same and apply to make the data center fabric Operational with single click.

        BGP IP CLOS
        BGP IP CLOS with MC LAG
        Layer 2 VXLAN with MCLAG
        Layer 2 VXLAN with BGP-EVPN
        VXLAN + EVPN Symmetric IRB
        VXLAN + EVPN Asymmetric IRB

        All configuartion depends on a YAML file
        """
        try:
            file_upload = {'file': open(template_path, 'rb')}
            url_for_upload = self.url + upload_endpoint
            getdata = requests.post(url_for_upload, files=file_upload)
            track_id = getdata.text

            return track_id

        except Exception as err:
            logging.error(err)
            raise FMClientExpection(UPLOAD_IMAGE_ERROR)


    def bgp_operation(self, config_file_path, diff_flag):
        """
        Params -> config_file_path, diff_flag
        config_file_path --> path of yaml file
        diff_flag  True --> is will show onlyconfig
                   False --> is will dump the config from file to device
        """
        try: 
            result_dict = {}
            cfg_file_upload = {'file': open(config_file_path, 'rb')}
            values = {'onlydiff':diff_flag}

            url_for_bgp_operation = self.url + bgp_operations_endpoint
            getdata = requests.post(url_for_bgp_operation, files=cfg_file_upload, data=values)
            if getdata.status_code != 200:
                print(BGP_OPERATION_ERROR)
                result_dict ['status'] = 'FAIL'
            else:
                result_dict ['status'] = 'PASS'
            result_dict ['logs'] = getdata.json()    
            return result_dict
        
        except Exception as err:
            logging.error(err)
            raise FMClientExpection(BGP_OPERATION_ERROR)

            
        
    
    
    
