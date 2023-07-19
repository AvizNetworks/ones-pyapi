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
from utils import get_request_handler


class FMClient(object):
    # FMClient will use for all Orchestration/ 
    # Configuration related operations

    # Since FM APIs is not returning any status
    # Directly sending response

    def __init__(self, url=None):
        self.url = url


    def get_controller_version(self):
        """
        Input params -> None
        Output -> return controller version
        """
        return get_request_handler(self.url, controller_version_endpoint, CONTROLLER_VERSION_INFO_ERROR)


    def get_intent_status(self):
        # Api to retrieve over all status for the given intent yaml file. 
        # This provides data to data grid which shows sub intent specific status single tick 
        # and double tick 

        # Query pararms - > intentName= .yamlfile
        pass


    def reboot(self):
        pass


    def ztp_enable(self):
        pass


    def controller_fm_version(self):
        pass


    def get_image_mgmnt_status(self):
        # Get ongoing reboot and image upgrade status, 
        # his will help in selecting particular device from grid
        pass


    def custom_image_upgrade(self):
        # To Trigger custom Image upgrade request
        pass


    def get_config_diff(self):
        #To get the data to show in config diff in UI, this getting called
        pass






