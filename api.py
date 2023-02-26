import requests
import datetime

class functions:
	def __init__(self):
		self.apiKey = 'ecff27819a24453a847df5efec9cf275'
		self.__all__ = ['get_all', 'get_headlines']
		
	def get(self, query: str, sources: str=''):
		"""
		Args:
		    query (str): Query you want to find
		"""
		headers = {
			'x-api-key': self.apiKey
		}
		if sources!='':
			data['sources'] = sources
			
		req = requests.get(f'https://newsapi.org/v2/everything?q={query}', headers=headers)
		return req.text

