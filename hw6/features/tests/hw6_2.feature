Feature: Looping the tab menu with comparing the tab menu text with header name
  Scenario: Compare each tab menu and header
    Given Open Amazon Best Sellers page
    When Get elements from tab menu
    Then Check each value with header
