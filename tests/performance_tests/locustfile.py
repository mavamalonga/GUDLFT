from locust import HttpUser, task
import os
import sys

path = 'C:\\Users\\HP\\Desktop\\GUDLFT\\'
os.chdir(path)
sys.path.insert(1, path)

from server import app, loadClubs, loadCompetitions

class ProjectPerfTest(HttpUser):
	@task
	def index(self):
		self.client.get('')

	@task 
	def totalClubPoints(self):
		self.client.get('clubPoints')

	@task 
	def show_summary(self):
		self.client.post('showSummary', data={'email': 'john@simplylift.co'})

	@task
	def book(self):
		club = loadClubs()[0]
		competition = loadCompetitions()[0]
		endpoint = f"book/{competition['name']}/{club['name']}"
		self.client.get(endpoint)

	@task 
	def clubPoints(self):
		club = loadClubs()[1]
		competition = loadCompetitions()[0]
		data = {
			"club": club['name'],
			"competition": competition['name'],
			"places": 10
		}
		self.client.post('purchasePlaces', data=data)

	



