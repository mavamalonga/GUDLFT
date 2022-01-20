# -*- coding: utf-8 -*-
import unittest
import os
import sys

path = 'C:\\Users\\HP\\Desktop\\GUDLFT\\'
os.chdir(path)
sys.path.insert(1, path)

from server import app, loadClubs, loadCompetitions


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


if __name__ == '__main__':
    unittest.main()
