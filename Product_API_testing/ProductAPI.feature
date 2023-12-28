# Created by Tejaswini at 26/12/23
Feature: Add Products, update and delete using Product API
  # Enter feature description here
  Scenario: Verify User and product API functionality
    Given creating the user using API
    When user created
    Then check if user is created successfully

    Given create product for user
    When product POST API is called
    Then check if product is successfully added

    Given get the products created with productId
    When product get API is called
    Then check if product retrieved successfully

    Given update the products created with productId and userId
    When put API is called
    Then check if product is updated successfully
    # Enter steps here
