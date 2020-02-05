# Created by mturchyn at 2/5/20
Feature: Lego Search
  # Enter feature description here

  Scenario: Find header on good
    Given Open amazon main page
    When Search input fill Lego
    And Click Search button
    Then Assert Lego header on the page
