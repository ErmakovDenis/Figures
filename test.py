# test_app.py

import unittest
from fastapi.testclient import TestClient

from main import *


class TestFastAPI(unittest.TestCase):

    def setUp(self):
        self.client = TestClient(app)

    def test_get_model_pyramid(self):
        response = self.client.get("/pyramid")
        self.assertEqual(response.status_code, 200)
        self.assertIn("figure", response.context)
        self.assertEqual(response.context["figure"], ModelName.PYRAMID.value)

    def test_get_model_cube(self):
        response = self.client.get("/cube")
        self.assertEqual(response.status_code, 200)
        self.assertIn("figure", response.context)
        self.assertEqual(response.context["figure"], ModelName.CUBE.value)

    def test_get_model_star(self):
        response = self.client.get("/star")
        self.assertEqual(response.status_code, 200)
        self.assertIn("figure", response.context)
        self.assertEqual(response.context["figure"], ModelName.STAR.value)

    def test_get_model_sphere(self):
        response = self.client.get("/sphere")
        self.assertEqual(response.status_code, 200)
        self.assertIn("figure", response.context)
        self.assertEqual(response.context["figure"], ModelName.SPHERE.value)

    def test_get_model_invalid(self):
        response = self.client.get("/invalid")
        self.assertEqual(response.status_code, 422)  # Unprocessable Entity

if __name__ == '__main__':
    unittest.main()