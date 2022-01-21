from django.test import TestCase
from .models import Posts
from django.contrib.auth.models import User

class PostsTest(TestCase):
    txt='123456'
    title='new title'
    un='new user'
    pw='123'
    email=''
    def setUp(self):
        Posts.objects.create(title=self.title,
                             author=User.objects.create_user(
                                 username=self.un,
                                 email=self.email,
                                 password=self.pw,),
                             text=self.txt
                             )
    def test_posts_by_user(self):
        post=Posts.objects.get(id=1)
        user=User.objects.get_by_natural_key(self.un)
        self.assertEqual(post.author,user)

# Create your tests here.
