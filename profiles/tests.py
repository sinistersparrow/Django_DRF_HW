import json
from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework.authtoken.models import Token
from rest_framework.test import APITestCase, APIClient
from rest_framework import status
from profiles.models import Profile
from profiles.api.serializers import ProfileSerializer


class RegistrationTestCase(APITestCase):

    client = APIClient()

    def test_registration(self):
        data = {"username": "testuser1", "email": "test@localhost.app", "password1": "A41&14all", "password2": "A41@14all"}
        response = self.client.post("/api/rest-auth/registration/", data)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

