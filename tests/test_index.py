# -*- coding: utf-8 -*-
import unittest
import os
import sys

path = 'C:\\Users\\HP\\Desktop\\GUDLFT\\'
os.chdir(path)
sys.path.insert(1, path)

from server import app, loadClubs, loadCompetitions


class TestIndex(unittest.TestCase):

	client = app.test_client()
	response = client.get('/')

	def test_status(self):
		statuscode = self.response.status_code
		self.assertEqual(statuscode, 200)

	def test_html_content(self):
		b = b'Welcome to the GUDLFT Registration Portal!'
		self.assertIn(b, self.response.data)


if __name__ == '__main__':
    unittest.main()
