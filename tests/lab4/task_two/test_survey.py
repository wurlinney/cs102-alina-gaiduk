import unittest
from src.lab4.task_two.survey import Respondent, Group, MakeGroups

class TestRespondent(unittest.TestCase):
    def test_lt(self):
        respondent1 = Respondent('Владимирова Анна', 30)
        respondent2 = Respondent('Остахов Владимир', 40)
        respondent3 = Respondent('Гайдук Алина', 19)
        respondent4 = Respondent('Семенова Алиса', 19)
        self.assertTrue(respondent2 < respondent1)
        self.assertTrue(respondent3 < respondent4)

class TestGroup(unittest.TestCase):

    def test_add_respondent(self):
        test_group = Group('19-25', 19, 25)
        respondent = Respondent('Гайдук Алина', 19)
        test_group.add_respondent(respondent)
        self.assertEqual(len(test_group.respondents), 1)
        self.assertEqual(test_group.respondents[0], respondent)

    def  test_str(self):
        test_group = Group('19 - 25', 19, 25)
        respondent1 = Respondent('Гайдук Алина', 19)
        respondent2 = Respondent('Семенова Алиса', 19)
        test_group.add_respondent(respondent1)
        test_group.add_respondent(respondent2)
        self.assertEqual(str(test_group), '19 - 25: Гайдук Алина (19), Семенова Алиса (19)')

class TestMakeGroups(unittest.TestCase):

    def test_read_personal_data(self):
        borders = [18, 25, 35, 45, 60, 80, 100]
        age_group = MakeGroups(borders)
        file_path = 'personal_data.txt'
        age_group.read_personal_data(file_path)
        expected_group_info = [
            "101+: Кошельков Захар Брониславович (105)",
            "81-100: Дьячков Нисон Иринеевич (88), Иванов Варлам Якунович (88)",
            "46-60: Старостин Ростислав Ермолаевич (50)",
            "26-35: Ярилова Розалия Трофимовна (29)",
            "0-18: Соколов Андрей Сергеевич (15), Егоров Алан Петрович (7)"
        ]

        self.assertEqual(age_group.get_age_groups_info(), expected_group_info)

if __name__ == '__main__':
    unittest.main()



