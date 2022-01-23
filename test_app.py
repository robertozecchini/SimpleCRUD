import unittest

from app import app, Profile, db

class AppTestCase(unittest.TestCase):
    def setUp(self):
        self.ctx = app.app_context()
        self.ctx.push()
        self.client = app.test_client()

    def tearDown(self):
        self.ctx.pop()

    def test_home(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)
    
    def test_lookup(self):
        p = Profile(first_name='Paolino', last_name='Paperino', age=30)
        db.session.add(p)
        db.session.commit()
        profiles = Profile.query.all()
        self.assertIn(p, profiles)

if __name__ == "__main__":
    unittest.main()
