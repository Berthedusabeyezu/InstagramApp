from django.test import TestCase
from .models import Profile,Image
import datetime as dt

class ProfileTestClass(TestCase):

    # Set up method
    def setUp(self):
        self.name = Profile(bio = 'text', image ='photo', pub_date ='26.3.2018')

    # Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.name,Profile))

     # Testing Save Method
    def test_save_method(self):
        self.name.save_profile()
        profiles = Profile.objects.all()
        self.assertTrue(len(profiles) > 0)
class ImageTestClass(TestCase):

    # Set up method
    def setUp(self):
        self.name = Image(bio = 'text', image ='photo', pub_date ='26.3.2018')


    # Creating a new tag and saving it
        self.new_image = images(name = 'testing')
        self.new_image.save()

        self.new_image= Image(title = 'Test Image',post = 'This is a random test Post',profile = self.name)
        self.new_image.save()

        self.new_image.images.add(self.new_image)

    def tearDown(self):
        Profile.objects.all().delete()
        images.objects.all().delete()
        Image.objects.all().delete()

# def test_get_instagram_by_date(self):
#         test_date = '2017-03-17'
#         date = dt.datetime.strptime(test_date, '%Y-%m-%d').date()
#         instagram_by_date = Article.days_instagram(date)
#         self.assertTrue(len(instagram_by_date) == 0)