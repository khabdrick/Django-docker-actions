from django.urls import reverse, resolve
class TestUrls:
  
   def test_post_content_url(self):
       path = reverse('content', kwargs={'pk':1})
       assert resolve(path).view_name == "content"  # here you are checking if the "path"'s view name is content