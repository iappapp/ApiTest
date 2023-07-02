from robot.api.deco import keyword


class ApiTestOne(object):
    def __init__(self):
        pass

    # @keyword('test_one')
    def test_one(self):
        print('hello')

    def test_my_case(self):
        pass


