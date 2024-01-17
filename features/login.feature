Feature: Check the login functionality

  Background:
    Given login: I am an user on the login page

  @smoke
   Scenario: Try to login with wrong credentials
    When login: I fill the username with value "username"
    When login: I fill the password with value "password"
    When login: I click the login button
    Then login: Error message is displayed with the message "Epic sadface: Username and password do not match any user in this service"

  @test
   Scenario: Try to login with different values
    When login: I click the login button
    Then login: Error message is displayed with the message "Epic sadface: Username is required"

  @outline_test
   Scenario Outline:Try to login with different values
     When login: I fill the username with value "<username>"
     When login: I fill the password with value "<password>"
     When login: I click the login button
     Then login: Error message is displayed with the message "<error>"

      Examples:
       | username     | password     | error |
       | username_123 |  wrong       | Epic sadface: Username and password do not match any user in this service |
       | wrong        |  pwd         | Epic sadface: Username and password do not match any user in this service |

   Scenario:Try to login without username,only password
     When login: I fill the password with value "password"
     When login: I click the login button
     Then login: Error message is displayed with the message "Epic sadface: Username is required"

   Scenario:Try to login without password,only username
     When login: I fill the username with value "username"
     When login: I click the login button
     Then login: Error message is displayed with the message "Epic sadface: Password is required"
  @login
   Scenario:Login with correct credentials
     When login: I fill the username with value "standard_user"
     When login: I fill the password with value "secret_sauce"
     When login: I click the login button
     Then inventory: The URL has changed
