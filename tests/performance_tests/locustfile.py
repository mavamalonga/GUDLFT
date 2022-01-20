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


class ClubPointsPerfTest(HttpUser):

	@task
	def locust_club_point_zero(self):
		club = loadClubs()[3]
		competition = loadCompetitions()[0]
		data = {
			'club': club['name'],
			'competition': competition['name'],
			'places': 10
		}
		self.client.post('purchasePlaces', data=data)

	@task
	def locust_club_points_lte_placeRequired(self):
		club = loadClubs()[1]
		competition = loadCompetitions()[0]
		data = {
			"club": club['name'],
			"competition": competition['name'],
			"places": 10
		}
		self.client.post('purchasePlaces', data=data)


class CompetitionPlacesPerfTest(HttpUser):

	@task
	def locust_places_lte_placesRequired(self):
		club = loadClubs()[-1]
		competition = loadCompetitions()[-1]
		data = {
			"club": club['name'],
			"competition": competition['name'],
			"places": 8
		}
		self.client.post('purchasePlaces', data=data)


class IndexPerfTest(HttpUser):

	@task
	def locust_index(self)
		self.client.get('/')

