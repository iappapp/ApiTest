from setuptools import setup, find_packages

setup(
    name = "ApiTestLib",
    version = "0.0.1",
    packages = find_packages('ApiTestLib'), package_dir= {'':'ApiTestLib'},
    description = "ApiTest lib",
    author = "iapp",
    author_email = "iapp@live.cn",

    license = "GPL",
    keyword = ("api test", "api", "robotframework"),
    platform = "Independent",
    url = ""
)