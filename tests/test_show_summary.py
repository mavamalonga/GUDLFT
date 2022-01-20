# -*- coding: utf-8 -*-
import unittest
import os
import sys

path = 'C:\\Users\\HP\\Desktop\\GUDLFT\\'
os.chdir(path)
sys.path.insert(1, path)

from server import app, loadClubs, loadCompetitions


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


if __name__ == '__main__':
    unittest.main()
