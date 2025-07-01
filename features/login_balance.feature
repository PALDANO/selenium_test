Feature: Login and compare balance

  Scenario: UI balance should match API balance
    Given the user is logged in
    When the user checks the balance on the UI
    And the user checks the balance from the API
    Then both balances should match
