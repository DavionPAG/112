from django.urls import reverse
from django.test import SimpleTestCase

# Create your tests here.
class SimpleTests(SimpleTestCase):

# ________________ROUTES TEST____________________
  def test_home_status_code(self):
    res = self.client.get('/')
    self.assertEqual(res.status_code, 200)

  def test_about_status_code(self):
    res = self.client.get('/about/')
    self.assertEqual(res.status_code, 200)

# ___________________HOME_PAGE TESTS_________________

  def test_home_page_uses_correct_template(self):
    res = self.client.get('/')
    self.assertTemplateUsed(res, 'index.html')
  
  def test_home_page_extends_base_template(self):
    res = self.client.get('/')
    self.assertTemplateUsed(res, 'base.html')

  def test_home_page_content(self):
    res = self.client.get('/')
    self.assertContains(res, 'Jinja')

  def test_home_page_content(self):
    res = self.client.get(reverse('home'))
    self.assertEqual(res.status_code, 200)
    self.assertTemplateUsed(res, 'index.html')

# ______________ABOUT_PAGE TESTS_________________________

  def test_about_page_uses_correct_template(self):
    res = self.client.get('/about/')
    self.assertTemplateUsed(res, 'about.html')
  
  def test_about_page_extends_base_template(self):
    res = self.client.get('/about/')
    self.assertTemplateUsed(res, 'base.html')

  def test_about_page_content(self):
    res = self.client.get('/about/')
    self.assertContains(res, 'Davion')

  def test_about_page_content(self):
    res = self.client.get(reverse('about'))
    self.assertEqual(res.status_code, 200)
    self.assertTemplateUsed(res, 'about.html')