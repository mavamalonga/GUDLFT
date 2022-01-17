import unittest
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


class TestIndex(unittest.TestCase):

	client = app.test_client()
	response = client.get('/')

	def test_status(self):
		statuscode = self.response.status_code
		self.assertEqual(statuscode, 200)

	def test_html_content(self):
		b = b'Welcome to the GUDLFT Registration Portal!'
		self.assertIn(b, self.response.data)


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








""""
	def test_upper(self):
		self.assertEqual('foo'.upper(), 'FOO')
		client = app.test_client()
		#rv = c.get('/?tequila=42')
		#assert request.args['tequila'] == '42'
		response = client.get('/showSummary')
		statuscode = response.status_code
		print(f"status_code : {statuscode}")
		res = b'Welcome' in response.data
		print(res)
		print(response.data)
		self.assertEqual(statuscode, 405)
"""

if __name__ == '__main__':
    unittest.main()