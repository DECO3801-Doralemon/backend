from django.test import TestCase
from profile_feature.models import Customer
from django.contrib.auth.models import User
from rest_framework_simplejwt.tokens import RefreshToken


class ProfileUnitTest(TestCase):
    customer = None
    accessToken = None
    user = None
    def setUp(self):
        self.user = User.objects.create_user(
        username = 'gibran',
        password = 'gibran',
        email = 'gibran@gibran.gibran',
        first_name = 'Gibran',
        last_name = 'Gibran'
        )
        self.accessToken = RefreshToken.for_user(self.user).access_token
        self.customer = Customer.objects.create(user=self.user, bio = 'Test', photo = 'profilePic/GDR.PNG')

    def testGet(self):
        response = self.client.get("/api/v1/profile/", header = {
        'Authorization': 'Bearer '+str(self.accessToken)
        })
        print("Access Token: "+str(self.accessToken))

        self.assertEqual(response.data, {
        'First Name': 'Gibran',
        'Last Name': 'Gibran',
        'Username': 'gibran',
        'Email' : 'gibran@gibran.gibran',
        'Biography': 'Test',
        'Photo': 'profilePic/GDR.PNG',
        })

    def testPost(self):
        response = self.client.post("/api/v1/profile/", header = {
        'Authorization': 'Bearer '+str(self.accessToken),
        }, data = {
        'Username' : 'gibran',
        'Email' : 'gibran@gibran.gibran',
        'First Name' : 'Gibran',
        'Last Name' : 'Gibran',
        'Biography' : 'Test',
        'Photo' : 'profilePic/GDR.PNG',
        })

        self.assertEqual(response.status_code, 200)
