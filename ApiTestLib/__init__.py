import importlib
import os
import sys
from types import MethodType, FunctionType

SCRIPT_DIR = 'scripts'
CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))


class ApiTestLib(object):
    ROBOT_GLOBAL_LIBRARY = 'GLOBAL'

    def __init__(self):
        self.keyword_method_dict = self.walk_through_script_dir()

    def __getattr__(self, item):
        if item.startswith('test') or item.startswith('setup') or item.startswith('teardown'):
            attr = self.keyword_method_dict.get(item)
            return attr

    def get_keyword_names(self):
        return self.keyword_method_dict.keys()

    def walk_through_script_dir(self):
        scripts_dir = os.path.join(CURRENT_DIR, SCRIPT_DIR)
        keyword_method_list = []
        for root, dirs, files in os.walk(scripts_dir, topdown=True):
            for file in files:
                if file == '__init__.py':
                    continue
                if file.endswith('.pyc'):
                    continue
                # print(root, dirs, file)
                module_name = self.get_module_name(root, file)
                keyword_method_list += self.scan_keyword_method(module_name)
        return self.kws_to_keyword_method_dict(keyword_method_list)

    def scan_keyword_method(self, module_name):
        kws = []
        import_package = importlib.import_module(module_name)
        for item in dir(import_package):
            if item.startswith('__'):
                continue

            attr = getattr(import_package, item)

            if isinstance(attr, (MethodType, FunctionType)):
                continue

            if isinstance(attr, type):
                kws = self.scan_keyword_method_to_kws(kws, attr)

        return kws

    def scan_keyword_method_to_kws(self, kws, attr):
        class_obj = attr()
        for item in dir(class_obj):
            if item.startswith('__'):
                continue
            if item.startswith('test') or item.startswith('setup') or item.startswith('teardown'):
                kws.append(getattr(class_obj, item))
        return kws

    def get_module_name(self, root, file):
        module_name_list = root.split(os.sep)
        module_name_list.append(os.path.splitext(file)[0])
        module_name_list = module_name_list[module_name_list.index('ApiTestLib'):]

        return '.'.join(module_name_list)

    def kws_to_keyword_method_dict(self, kws):
        keyword_method_dict = {}
        for item in kws:
            name = item.__name__
            keyword_method_dict[name] = item
        return keyword_method_dict


if __name__ == '__main__':
    test = ApiTestLib()
    print('\n'.join(test.get_keyword_names()))
    getattr(test, 'test_one')

    for item in dir(test):
        print(item)