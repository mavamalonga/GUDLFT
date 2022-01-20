# -*- coding: utf-8 -*-
import unittest
import os
import sys

path = 'C:\\Users\\HP\\Desktop\\GUDLFT\\'
os.chdir(path)
sys.path.insert(1, path)

from server import app, loadClubs, loadCompetitions


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


if __name__ == '__main__':
    unittest.main()
