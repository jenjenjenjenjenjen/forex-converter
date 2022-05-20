from app import app
from unittest import TestCase

class AppTestCase(TestCase):
    def test_redirect_to_result(self):
        with app.test_client() as client:
            response = client.post('/convert', data={"converting-from": "USD", "converting-to": "USD", "amount": "1"})

            self.assertEqual(response.status_code, 302)
            self.assertEqual(response.location, "http://localhost/")

    def test_redirection_followed(self):
        with app.test_client() as client:
            response = client.post('/convert', 
                                    data={"converting-from": "USD", "converting-to": "USD", "amount": "1"}, 
                                    follow_redirects=True)
            html = response.get_data(as_text=True)

            self.assertEqual(response.status_code, 200)
            self.assertIn("<li>The result is 1.0.</li>", html)

    


