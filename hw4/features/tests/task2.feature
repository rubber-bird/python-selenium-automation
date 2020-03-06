Feature: Make a request and count the results in page
  Scenario: Counting Results
    Given Open Amazon main page
    When Input History Books into amazon search field
    And Click Search button
    Then Count Results
    And If price of fist element more than 10 dollards add to card
