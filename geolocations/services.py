import requests
from django.conf import settings

API_KEY = getattr(settings, "IPSTACK_KEY", None)


class IpstackService():

    @staticmethod
    def get_geodata_for_host(hostname):
        if API_KEY:

            data = requests.get(
                f"http://api.ipstack.com/{hostname}?access_key={API_KEY}")

            return data.json()
