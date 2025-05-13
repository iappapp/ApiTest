from robot.api.deco import keyword


class ApiTestOne(object):
    def __init__(self):
        pass

    def setup_api_test_one(self):
        print('setup this test case')
        pass

    def teardown_api_test_one(self):
        print('teardown this test case')
        pass

    # @keyword('test_one')
    def test_one(self):
        print('hello')
        print("i run the test unit")

    def test_my_case(self):
        pass


