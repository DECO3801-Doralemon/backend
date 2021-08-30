from rest_framework.test import APITestCase
from profile_feature.models import Customer
from django.contrib.auth.models import User


class AuthUnitTest(APITestCase):

    def test_register(self):
        response = self.client.post("/api/v1/auth/register", data={
            'username': 'gibran',
            'password': 'gibrannn',
            'email': 'gibran@email.com',
            'first_name': 'Gibran',
            'last_name': 'Gibran',
        })

        self.assertEqual(response.status_code, 201)

        count = Customer.objects.all().count()
        self.assertEqual(count, 1)
