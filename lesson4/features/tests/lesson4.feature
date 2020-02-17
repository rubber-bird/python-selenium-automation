# Created by mturchyn at 2/12/20
Feature: Check menu items
  # Enter feature description here

  Scenario: User will get Fire Tablets items
    # Enter steps here
    Given Open Amazon main page
    When Click hamburger menu
    And Click Fire Tablets
    Then Menu will have 16 items