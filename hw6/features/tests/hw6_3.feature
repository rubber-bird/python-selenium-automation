Feature: Checking results for the word Table and emptying cart
  Scenario: Check if each element has the word Table in it's title
    Given Open Webpage
    When Search for stainless work table
    Then Check the search result ensuring every product item has the word Table its title
    And Add the last of found items to Cart
    Then Empty Cart