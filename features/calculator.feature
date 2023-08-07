# calculator.feature

Feature: Calculator Application

  Scenario: Add two numbers
    Given the calculator is open
    When I enter "One" and "Plus" and "Two"
    Then the result should be "Display is 3" on the display

  Scenario: Subtract two numbers
    Given the calculator is open
    When I enter "Five" and "Minus" and "Three"
    Then the result should be "Display is 2" on the display

  Scenario: Multiply two numbers
    Given the calculator is open
    When I enter "Four" and "Multiply by" and "Seven"
    Then the result should be "Display is 28" on the display

  Scenario: Divide two numbers
    Given the calculator is open
    When I enter "Eight" and "Divide by" and "Two"
    Then the result should be "Display is 4" on the display