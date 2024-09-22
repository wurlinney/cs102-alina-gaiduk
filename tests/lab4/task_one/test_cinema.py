import unittest
from  src.lab4.task_one.cinema import User, Recommendation
class TestUser(unittest.TestCase):
        def test_same_views(self):
                user1 =  User([1, 2, 3])
                user2 = User([1, 3, 4])
                user3 = User([2, 5, 7])
                user4 = User([4, 8, 10, 3, 5])
                self.assertEqual(user4.same_views(user2), 2/5)
                self.assertEqual(user1.same_views(user3), 1/3)
                self.assertEqual(user1.same_views(user2), 2/3)
class TestRecommendation(unittest.TestCase):
        def


