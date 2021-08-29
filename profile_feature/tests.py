from rest_framework.test import APITestCase
from profile_feature.models import Customer
from django.contrib.auth.models import User
from rest_framework_simplejwt.tokens import RefreshToken
from django.core.files.uploadedfile import SimpleUploadedFile
from django.conf import settings


class ProfileUnitTest(APITestCase):
    customer = None
    accessToken = None
    user = None

    def setUp(self):
        self.user = User.objects.create_user(
            username='gibran',
            password='gibran',
            email='gibran@gibran.gibran',
            first_name='Gibran',
            last_name='Gibran'
        )
        self.accessToken = RefreshToken.for_user(self.user).access_token

        self.customer = Customer.objects.create(
            user=self.user, bio='Test')

    def test_profile_get(self):
        self.client.credentials(
            HTTP_AUTHORIZATION='Bearer ' + str(self.accessToken))
        response = self.client.get("/api/v1/profile/")

        self.assertEqual(response.content.decode(
            "UTF-8"),
            '{"First Name": "Gibran", "Last Name": "Gibran", "Username": "gibran", "Email": "gibran@gibran.gibran", "Biography": "Test", "Photo": "/profile_photo/GDR.PNG"}')

    def test_profile_post(self):
        photo = SimpleUploadedFile(name='test_photo.png',
                                   content=open(settings.BASE_DIR / 'test_media/1.png', 'rb').read())

        self.client.credentials(
            HTTP_AUTHORIZATION='Bearer ' + str(self.accessToken))
        response = self.client.post("/api/v1/profile/", data={
            'first_name': 'Gibran',
            'last_name': 'Gibran',
            'email': 'gibran@gibran.gibran',
            'bio': 'Test',
            'photo': photo,
        })

        self.assertEqual(response.status_code, 200)
