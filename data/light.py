import logging
import requests

logger = logging.getLogger(__name__)

class LightController:
    def __init__(self, api: str):
        self._api = api
        self._session = requests.Session()
        # self._session.proxies = {
        #     'http': 'http://',
        #     'https': 'http://',
        # }
        logger.info("Light controller initialized")
    
    def turn_on(self):
        logger.info("Turning on light")
        self._session.post(self._api, json={'on': 1})
        logger.info("Light turned on")
    
    def turn_off(self):
        logger.info("Turning off light")
        self._session.post(self._api, json={'on': 0})
        logger.info("Light turned off")
    