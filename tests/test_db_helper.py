from unittest import TestCase, mock
from unittest.mock import patch
from src.db_helper import DbHelper

class Test_Db_Helper(TestCase):
    @patch('src.db_helper')
    def test_max_salary_is_greater_than_min_salary(self, MockHelper):
        db = MockHelper()
        db.get_maximum_salary.return_value = 20000
        db.get_minimum_salary.return_value = 15000
        maxsalary = db.get_maximum_salary()
        minsalary = db.get_minimum_salary()
        self.assertGreater(maxsalary, minsalary)