import requests
import json

from steamclient.exeptions import *


class SteamClient:
	"""Login, Generate 2FA and confirmation codes."""

	def __init__(self, path_to_config: str) -> None:
		"""
		:param path_to_config: path to file with login account data
		:type path_to_config: str
		"""
		self._load_config_from_file(path_to_config)

	def _load_config_from_file(self, path_to_config: str) -> None:
		"""Loading account config from file
	
		:param path_to_config: path to file with login account data
		:type path_to_config: str
		:raises: :class:`UnknownConfigKeyError`
		"""
		self.config = {
			"username": None,
			"password": None,
			"apikey": None,
			"steamid": None,
		    "shared_secret": None,
		    "identity_secret": None,
		    "proxy": None
		}
		with open(path_to_config, "r") as file:
			_json_data = json.load(file)
			for key, value in _json_data.items():
				if key not in self.config:
					raise UnknownConfigKeyError(f"Check the spelling of keys in the configuration file")
				self.config[key] = value

	def login(self) -> bool:
		pass

