*** Settings ***
Test Setup           setup_api_test_one
Test Teardown        teardown_api_test_one
Library         ApiTestLib

*** Test Cases ***
01-01-01-test_one
    [tags]  L_1
    test_one
