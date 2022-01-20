# -*- coding: utf-8 -*-
import unittest
import os
import sys

path = 'C:\\Users\\HP\\Desktop\\GUDLFT\\'
os.chdir(path)
sys.path.insert(1, path)

from server import app, loadClubs, loadCompetitions


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


if __name__ == '__main__':
    unittest.main()
