Feature: Verify login functionality for OrangeHRM
#
#  Background:
#    Given Launch the browser
  Scenario Outline: Verify login for valid credentials
    Given I enter the url
    When I enter the username as "<username>" and password "<password>"
    And click on login button
    Then I should see the OrangeHRM logo
    Examples:
    | username | password |
    |   admin  | admin123 |
    |   admin  | admin1234 |