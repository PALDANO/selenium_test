Feature: Basic login and balance presence

  Scenario: User logs in and sees positive balance
    Given the user is logged in
    When the user checks the balance on the UI
    Then the balance should be greater than zero
