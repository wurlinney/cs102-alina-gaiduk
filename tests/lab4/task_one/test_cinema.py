import os
from  src.lab4.task_one.cinema import Recommendation
import unittest


class TestRecommended(unittest.TestCase):

    def test_recommend(self):
        current_dir = os.path.dirname(__file__)
        list_of_films = os.path.join(current_dir, 'films.txt')
        history_file = os.path.join(current_dir, 'history.txt')
        recommendation_system = Recommendation(list_of_films, history_file)
        input_data = [2, 4]
        expected_result = 'Дюна'
        actual_result = recommendation_system.recommend(input_data)
        self.assertEqual(actual_result, expected_result)


    def test_history_list(self):
        current_dir = os.path.dirname(__file__)
        list_of_films = os.path.join(current_dir, 'films.txt')
        history_file = os.path.join(current_dir, 'history.txt')
        recommendation_service = Recommendation(list_of_films, history_file)
        expected_history_sets = [
            {2, 1, 3},
            {1, 4, 3},
            {2, 2, 2, 2, 2, 3}
        ]

        result = recommendation_service.history_list(history_file)
        for i, user in enumerate(result[:3]):
            self.assertEqual(user.watched_films, expected_history_sets[i])


if __name__ == '__main__':
        unittest.main()


