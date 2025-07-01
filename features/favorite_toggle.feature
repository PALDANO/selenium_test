Feature: Toggle favorite game

  Scenario: Mark and unmark 'Live Blackjack' as favorite
    Given the user is logged in
    And the user is on the casino page
    When the user marks "Live Blackjack" as favorite
    And the user unmarks "Live Blackjack" as favorite
    Then the game should no longer be marked as favorite
