import requests
from django.conf import settings

API_KEY = getattr(settings, "IPSTACK_KEY", None)


class IpstackService:
    """Service for making calls to IPStack API"""

    @staticmethod
    def get_geodata_for_host(hostname):
        if API_KEY:

            data = requests.get(
                f"http://api.ipstack.com/{hostname}?access_key={API_KEY}")

            print(data.json())
            return data.json()


class JsonAttributeParser:
    """Service for quickly parsing response and input data"""

    @staticmethod
    def add_attributes(data, **kwargs):
        """Adds specified key arguments and values in input data dict"""
        for key in kwargs:
            data[key] = kwargs[key]
