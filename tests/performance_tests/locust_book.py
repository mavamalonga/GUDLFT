from locust import HttpUser, task
import os
import sys

path = 'C:\\Users\\HP\\Desktop\\GUDLFT\\'
os.chdir(path)
sys.path.insert(1, path)

from server import app, loadClubs, loadCompetitions

class BookPerfTest(HttpUser):

	@task
	def locust_book(self):
		club = loadClubs()[0]
		competition = loadCompetitions()[0]
		endpoint = f"book/{competition['name']}/{club['name']}"
		self.client.get(endpoint)