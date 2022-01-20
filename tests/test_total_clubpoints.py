# -*- coding: utf-8 -*-
import unittest
import os
import sys

path = 'C:\\Users\\HP\\Desktop\\GUDLFT\\'
os.chdir(path)
sys.path.insert(1, path)

from server import app, loadClubs, loadCompetitions


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
    unittest.main()
