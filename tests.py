import unittest
from server import app, loadClubs, loadCompetitions


class TestDataFunctions(unittest.TestCase):

	def test_loadClubs(self):
		first_club = {
			"name":"Simply Lift",
			"email":"john@simplylift.co",
			"points":"13"
			}
		self.assertEqual(first_club, loadClubs()[0])

	def test_loadCompetitions(self):
		first_comp = {
			"name": "Spring Festival",
			"date": "2020-03-27 10:00:00",
			"numberOfPlaces": "25"
		}
		self.assertEqual(first_comp, loadCompetitions()[0])


class TestIndexFunction(unittest.TestCase):

	client = app.test_client()
	response = client.get('/')

	def test_index_status(self):
		statuscode = self.response.status_code
		self.assertEqual(statuscode, 200)

	def test_index_html_content(self):
		b = b'Welcome to the GUDLFT Registration Portal!'
		self.assertIn(b, self.response.data)



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