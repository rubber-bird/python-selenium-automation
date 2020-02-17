# Created by mturchyn at 2/9/20
Feature: Book counter
  # Enter feature description here

  Scenario: Counting history books
    # Enter steps here
    Given Open amazon main page
    When Search input fill history book
    And Click Search button