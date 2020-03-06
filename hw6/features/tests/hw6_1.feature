Feature: Open and close pages and add the product, check card
  Scenario: User can open and close pages, cart items would be saved in memory
    Given Open Amazon page
    When Store original windows
    And Click to blog link
    And Switch to the window 1
    And Switch to the window 0
    And Switch to the window 1
    Then User can close new window and switch back to original
    Then Open product page
    And Add item to card
    Then Refresh the page
    And Verify that card has 1 item