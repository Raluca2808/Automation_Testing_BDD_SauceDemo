Feature: Check inventory funtionality
  Background:
    Given login: I am an user on the login page
    When login: I fill the username with value "standard_user"
    When login: I fill the password with value "secret_sauce"
    When login: I click the login button
    Then inventory: I am on inventory page
@test1
    Scenario:Inventory click settings button
      When inventory: I click the settings button
      Then inventory: Settings list is displayed
  @test2
    Scenario: Check the logo is displayed
      Then inventory: logo is displayed
    Scenario: Click the cart icon
      When inventory: I click on the cart icon
      Then cart: Thr URL has changed
