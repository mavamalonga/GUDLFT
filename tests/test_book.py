# -*- coding: utf-8 -*-
import unittest
import os
import sys

path = 'C:\\Users\\HP\\Desktop\\GUDLFT\\'
os.chdir(path)
sys.path.insert(1, path)

from server import app, loadClubs, loadCompetitions


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


if __name__ == '__main__':
    unittest.main()
