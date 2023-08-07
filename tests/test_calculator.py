# test_calculator.py
import pytest
from hamcrest import assert_that, equal_to
from pytest_bdd import scenarios, given, when, then, parsers, scenario
from pages.calculator import CalculatorPage

feature_file_location = '../features/calculator.feature'
scenarios('../features/calculator.feature')

# Define fixture to set up and tear down the Calculator application before/after each scenario.

@pytest.fixture(scope='function')
def calculator():
    calculator_app = CalculatorPage()
    try:
        yield calculator_app
    finally:
        calculator_app.close()

# Mapped to Feature file to run the required tests

@scenario(feature_file_location, 'Add two numbers')
def test_add_two_numbers():
    pass

@scenario(feature_file_location, 'Subtract two numbers')
def test_subtract_two_numbers():
    pass

@scenario(feature_file_location, 'Multiply two numbers')
def test_multiply_two_numbers():
    pass

@scenario(feature_file_location, 'Divide two numbers')
def test_divide_two_numbers():
    pass

#---------------------------------------------- Step Implementation ---------------------------------------------------#

@given('the calculator is open')
def open_calculator(calculator):
    # Open Calculator application is already executed in the fixture and no implementation is needed.
    pass

@when(parsers.parse('I enter "{number1}" and "{operator}" and "{number2}"'))
def perform_calculation(calculator, number1, operator, number2):
    # Implementation of the code to enter numbers and operators in the Calculator.
    calculator.click_button(number1)
    calculator.click_button(operator)
    calculator.click_button(number2)
    calculator.click_button("Equals")

@then(parsers.parse('the result should be "{expectedResult}" on the display'))
def verify_result(calculator, expectedResult):
    # Implementation of the code to verify the result on the Calculator display.
    actualResult = calculator.get_result("CalculatorResults")
    assert_that(actualResult, equal_to(expectedResult), f'Expected:{expectedResult} but displayed {actualResult} result')