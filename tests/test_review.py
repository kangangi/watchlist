import unittest
from app.models import Review

class ReviewTest(unittest.TestCase):
  '''
  Test Class to test the behaviour of the Movie class
  self.movie_id = movie_id
    self.title = title
    self.imageurl = imageurl
    self.review = review

  '''
  def setUp(self):
    '''
    Set up method that will run before every Test
    '''
    self.new_review = Review(1234,'Python Must Be Crazy','imageurl','A thrilling new Python Series',)

  def test_instance(self):
    self.assertTrue(isinstance(self.new_review,Review))


 

 
