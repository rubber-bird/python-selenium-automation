Feature: Dress color

  Scenario: Check every dress color name
    Given Open Amazon dress page
    When Get all dress colors
    Then Check every color has description