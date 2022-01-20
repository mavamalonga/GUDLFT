# -*- coding: utf-8 -*-
import unittest
import os
import sys

path = 'C:\\Users\\HP\\Desktop\\GUDLFT\\'
os.chdir(path)
sys.path.insert(1, path)

from server import app, loadClubs, loadCompetitions


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


if __name__ == '__main__':
    unittest.main()