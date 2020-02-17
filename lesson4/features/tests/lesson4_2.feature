# Created by mturchyn at 2/13/20
Feature: Close popup
  # Enter feature description here

  Scenario: If we have popup, we will close it
    # Enter steps here
    Given Open Heritage site
    When See popup
    Then Close popup