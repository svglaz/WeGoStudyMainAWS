import unittest
import wegostudy_locators as locators
import wegostudy_methods as methods


class WeGoStudyPositiveTestCases(unittest.TestCase):

    @staticmethod
    def test_WeGoStudy():
        methods.setUp()
        #methods.negative_login_test()
        methods.log_in()
        methods.create_new_student()
        methods.view_details_of_student()
        methods.log_out()
        methods.tearDown()

