Feature: Find how many best sellers on a result page
  Scenario: Looking for best sellers
    Given Open Amazon main page
    When Input fantasy books into amazon search field
    And Click Search button
    Then Count Best sellers