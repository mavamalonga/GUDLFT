# -*- coding: utf-8 -*-
import unittest
import HtmlTestRunner
import os
import sys

path = 'C:\\Users\\HP\\Desktop\\GUDLFT\\'
os.chdir(path)
sys.path.insert(1, path)

from server import app, loadClubs, loadCompetitions

class TestUnittest(unittest.TestCase):
	
	def test_book_html_content(self):
		client = app.test_client()
		club = loadClubs()[0]
		competition = loadCompetitions()[0]
		endpoint = f"/book/{competition['name']}/{club['name']}"
		response = client.get(endpoint)
		self.assertIn(b'Booking for Spring Festival', response.data)

	def test_clubpoint_zero(self):
		client = app.test_client()
		club = loadClubs()[3]
		competition = loadCompetitions()[0]
		data = {
			'club': club['name'],
			'competition': competition['name'],
			'places': 10
		}
		response = client.post('/purchasePlaces', data=data)
		self.assertIn(b'sorry! you don&#39;t have enough points to make this order', response.data)

	def test_club_points_lte_placeRequired(self):
		client = app.test_client()
		club = loadClubs()[1]
		competition = loadCompetitions()[0]
		data = {
			"club": club['name'],
			"competition": competition['name'],
			"places": 10
		}
		response = client.post('/purchasePlaces', data=data)
		self.assertIn(b"sorry! you don&#39;t have enough points to make this order", response.data)

	def test_places_lte_placesRequired(self):
		client = app.test_client()
		club = loadClubs()[-1]
		competition = loadCompetitions()[-1]
		data = {
			"club": club['name'],
			"competition": competition['name'],
			"places": 8
		}
		response = client.post('/purchasePlaces', data=data)
		self.assertIn(b'Sorry there is not enough places for your order', response.data)

	def test_loadClubs_function(self):
		club = {
			"name":"Simply Lift",
			"email":"john@simplylift.co",
			"points":"13"
			}
		self.assertEqual(club, loadClubs()[0])

	def test_loadCompetitions_function(self):
		competition = {
			"name": "Spring Festival",
			"date": "2020-03-27 10:00:00",
			"numberOfPlaces": "25"
		}
		self.assertEqual(competition, loadCompetitions()[0])

	def test_index_html_content(self):
		client = app.test_client()
		response = client.get('/')
		b = b'Welcome to the GUDLFT Registration Portal!'
		self.assertIn(b, response.data)

	def test_places_zero(self):
		client = app.test_client()
		club = loadClubs()[0]
		competition = loadCompetitions()[0]
		data = {
			'club': club['name'],
			'competition': competition['name'],
			'places': 0
		}
		response = client.post('/purchasePlaces', data=data)
		self.assertIn(b'Sorry! select a number of places between 1 and 12', response.data)

	def test_places_negative(self):
		client = app.test_client()
		club = loadClubs()[0]
		competition = loadCompetitions()[0]
		data = {
			'club': club['name'],
			'competition': competition['name'],
			'places': -1
		}
		response = client.post('/purchasePlaces', data=data)
		self.assertIn(b'Sorry! select a number of places between 1 and 12', response.data)

	def test_places_greater_than_12(self):
		client = app.test_client()
		club = loadClubs()[0]
		competition = loadCompetitions()[0]
		data = {
			'club': club['name'],
			'competition': competition['name'],
			'places': 13
		}
		response = client.post('/purchasePlaces', data=data)
		self.assertIn(b'Sorry! select a number of places between 1 and 12', 
			response.data)

	def test_places_required_value_error(self):
		client = app.test_client()
		club = loadClubs()[0]
		competition = loadCompetitions()[0]
		data = {
			'club': club['name'],
			'competition': competition['name'],
			'places': "e"
		}
		response = client.post('/purchasePlaces', data=data)
		self.assertIn(b'Please enter a number', response.data)

	def test_purchase_places(self):
		client = app.test_client()
		club = loadClubs()[0]
		competition = loadCompetitions()[0]
		data = {
			'club': club['name'],
			'competition': competition['name'],
			'places': 10
		}
		response = client.post('/purchasePlaces', data=data)
		self.assertIn(b'Great-booking complete!', response.data)

	def test_showSummary_html_content(self):
		client = app.test_client()
		club = loadClubs()[0]
		response = client.post('/showSummary', data={'email': club['email']})
		content = f"Welcome, {club['email']}"
		self.assertIn(content, str(response.data))

	def test_totalClubPoints_html_content(self):
		client = app.test_client()
		response = client.get('/clubPoints')
		self.assertIn(b'Total points per club', response.data)


if __name__ == '__main__':
	unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='./testReportHtml'))

