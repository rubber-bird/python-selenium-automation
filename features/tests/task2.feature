# Created by mturchyn at 2/5/20
Feature: Search for Cancelling an order
  # Enter feature description here

  Scenario: Find a cancel order on result page
    # Enter steps here
    Given Open Amazon page
    Then Click help button
    When Input Cancel Order into help search field
    Then Click on help search icon
    And Header check for Cancel Items or Orders


  Scenario: Check if shopping card is empty
    Given Open Amazon page
    Then Open shopping card
    And Check if shopping card is empty


   Scenario: Add Item and Delete it
    Given Open Amazon page
    When Input Yamaha Guitar into amazon search field
    And Click Amazon Search button
    Then Add second item to card
    And Click add to card
    And No Protection Plan
    Given Open Amazon page
    Then Open shopping card
    And Delete item
    And Check if shopping card is empty