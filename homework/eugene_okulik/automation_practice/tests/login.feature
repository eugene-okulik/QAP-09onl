Feature: Login page

    Scenario: login field exists
    Given I am on home page
    When I click login button
    And I click login field
    Then I see login field

    Scenario: password field exists
    Given I am on home page
    When I click login button
    Then I see password field