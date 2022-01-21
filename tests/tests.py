# -*- coding: utf-8 -*-
import unittest
import HtmlTestRunner
import os
import sys

from server import app, loadClubs, loadCompetitions

path = 'C:\\Users\\HP\\Desktop\\GUDLFT\\'
os.chdir(path)
sys.path.insert(1, path)


class TestBook(unittest.TestCase):

	client = app.test_client()
	club = loadClubs()[0]
	competition = loadCompetitions()[0]
	endpoint = f"/book/{competition['name']}/{club['name']}"
	response = client.get(endpoint)

	def test_status(self):
		statuscode = self.response.status_code
		self.assertEqual(statuscode, 200)
	
	def test_html_content(self):
		self.assertIn(b'Booking for Spring Festival', self.response.data)
		self.assertIn(b'Places available: 25', self.response.data)


class TestClubPoints(unittest.TestCase):

	def test_club_point_zero(self):
		client = app.test_client()
		club = loadClubs()[3]
		competition = loadCompetitions()[0]
		data = {
			'club': club['name'],
			'competition': competition['name'],
			'places': 10
		}
		response = client.post('/purchasePlaces', data=data)
		self.assertEqual(response.status_code, 200)
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
		self.assertEqual(response.status_code, 200)
		self.assertIn(b"sorry! you don&#39;t have enough points to make this order", response.data)


class TestCompetitionPlaces(unittest.TestCase):

	client = app.test_client()

	def test_places_lte_placesRequired(self):
		club = loadClubs()[-1]
		competition = loadCompetitions()[-1]
		data = {
			"club": club['name'],
			"competition": competition['name'],
			"places": 8
		}
		response = self.client.post('/purchasePlaces', data=data)
		self.assertEqual(response.status_code, 200)
		self.assertIn(b'Sorry there is not enough places for your order', response.data)


class TestDataJson(unittest.TestCase):

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


class TestIndex(unittest.TestCase):

	client = app.test_client()
	response = client.get('/')

	def test_status(self):
		statuscode = self.response.status_code
		self.assertEqual(statuscode, 200)

	def test_html_content(self):
		b = b'Welcome to the GUDLFT Registration Portal!'
		self.assertIn(b, self.response.data)


class TestPlacesRequired(unittest.TestCase):

	client = app.test_client()
	club = loadClubs()[0]
	competition = loadCompetitions()[0]

	def test_places_zero(self):
		data = {
			'club': self.club['name'],
			'competition': self.competition['name'],
			'places': 0
		}
		response = self.client.post('/purchasePlaces', data=data)
		self.assertEqual(response.status_code, 200)
		self.assertIn(b'Sorry! select a number of places between 1 and 12', response.data)

	def test_places_negative(self):
		data = {
			'club': self.club['name'],
			'competition': self.competition['name'],
			'places': -1
		}
		response = self.client.post('/purchasePlaces', data=data)
		self.assertEqual(response.status_code, 200)
		self.assertIn(b'Sorry! select a number of places between 1 and 12', response.data)

	def test_places_greater_than_12(self):
		data = {
			'club': self.club['name'],
			'competition': self.competition['name'],
			'places': 13
		}
		response = self.client.post('/purchasePlaces', data=data)
		self.assertEqual(response.status_code, 200)
		self.assertIn(b'Sorry! select a number of places between 1 and 12', 
			response.data)

	def test_purchase_places(self):
		data = {
			'club': self.club['name'],
			'competition': self.competition['name'],
			'places': 10
		}
		response = self.client.post('/purchasePlaces', data=data)
		self.assertEqual(response.status_code, 200)
		self.assertIn(b'Great-booking complete!', response.data)


class TestShowSummary(unittest.TestCase):

	client = app.test_client()
	club = loadClubs()[0]
	response = client.post('/showSummary', data={'email': club['email']})

	def test_status(self):
		statuscode = self.response.status_code
		self.assertEqual(statuscode, 200)

	def test_html_content(self):
		content = f"Welcome, {self.club['email']}"
		self.assertIn(content, str(self.response.data))


class TestTotalClubsPoints(unittest.TestCase):

	client = app.test_client()
	response = client.get('/clubPoints')

	def test_status(self):
		statuscode = self.response.status_code
		self.assertEqual(statuscode, 200)

	def test_html_content(self):
		self.assertIn(b'Total points per club', self.response.data)
		self.assertIn(b'Simply Lift', self.response.data)
		self.assertIn(b'Iron Temple', self.response.data)


if __name__ == '__main__':
	unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='./testReportHtml'))

