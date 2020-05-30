from django.test import TestCase, SimpleTestCase
from django.shortcuts import reverse



class HomePageTests(SimpleTestCase):
    

    def test_home_status_code(self):
      response = self.client.get('/')
      self.assertEquals(response.status_code,200)

    def test_signIn_status_code(self):
      response = self.client.get('/accounts/signIn')
      self.assertEquals(response.status_code,200)

    def test_register_status_code(self):
      response = self.client.get('/accounts/register')
      self.assertEquals(response.status_code,200) 

    def test_admin_status_code(self):
        response = self.client.get('/admin/')
        self.assertEquals(response.status_code, 200)

    def test_signIn_url_name(self):
      response = self.client.get(reverse('signIn'))
      self.assertEquals(response.status_code, 200)

    def test_register_url_name(self):
      response = self.client.get(reverse('register'))
      self.assertEquals(response.status_code, 200)

    def test_home_url_name(self):
      response = self.client.get(reverse('home'))
      self.assertEquals(response.status_code, 200)

    def test_correct_template_signIn(self):
      response = self.client.get(reverse('signIn'))
      self.assertEquals(response.status_code, 200)
      self.assertTemplateUsed(response, 'signIn.html')

    def test_correct_template_register(self):
      response = self.client.get(reverse('register'))
      self.assertEquals(response.status_code, 200)
      self.assertTemplateUsed(response, 'register.html')

    def test_correct_template_home(self):
      response = self.client.get(reverse('home'))
      self.assertEquals(response.status_code, 200)
      self.assertTemplateUsed(response, 'index.html')