from locust import HttpUser, task
import os
import sys

path = 'C:\\Users\\HP\\Desktop\\GUDLFT\\'
os.chdir(path)
sys.path.insert(1, path)

from server import app, loadClubs, loadCompetitions

class ClubPointsPerfTest(HttpUser):

	@task
	def test_club_point_zero(self):
		club = loadClubs()[3]
		competition = loadCompetitions()[0]
		data = {
			'club': club['name'],
			'competition': competition['name'],
			'places': 10
		}
		self.client.post('purchasePlaces', data=data)

	@task
	def test_club_points_lte_placeRequired(self):
		club = loadClubs()[1]
		competition = loadCompetitions()[0]
		data = {
			"club": club['name'],
			"competition": competition['name'],
			"places": 10
		}
		self.client.post('purchasePlaces', data=data)