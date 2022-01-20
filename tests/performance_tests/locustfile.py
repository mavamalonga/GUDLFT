from locust import HttpUser, task
import os
import sys

class ProjectPerfTest(HttpUser):
	@task
	def index(self):
		self.client.get('')

	@task 
	def clubPoints(self):
		self.client.get('clubPoints')

	@task 
	def show_summary(self):
		self.client.post('showSummary', data={'email': 'john@simplylift.co'})
