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


class IndexPerfTest(HttpUser):

	@task
	def locust_index(self):
		self.client.get('')


class PurchasePlacesPerfTest(HttpUser):

	club = loadClubs()[0]
	competition = loadCompetitions()[0]

	@task
	def locust_purchase_places(self):
		data = {
			'club': self.club['name'],
			'competition': self.competition['name'],
			'places': 10
		}
		self.client.post('purchasePlaces', data=data)


class ShowSummaryPerfTest(HttpUser):

	@task
	def locust_showSummary(self):
		club = loadClubs()[0]
		self.client.post('showSummary', data={'email': club['email']})


class TotalClubsPointsPerfTest(HttpUser):

	@task
	def locust_clubPoints(self):
		self.client.get('clubPoints')





