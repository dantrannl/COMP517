# COMP517
Contains all the lab assignments about OOP I have done for my course this year

1. cache.py
Program Description:
This Python program simulates a simple memory management system using a cache mechanism. It processes user input to manage requests and determines whether each request is a "Hit" (already in cache) or a "Miss" (not in cache). The program uses an LRU (Least Recently Used) policy to evict old pages when the cache reaches its limit.

Skills:
List Operations: Demonstrates dynamic list management, including adding, removing, and checking elements.
Control Flow: Uses loops and conditional statements to handle input and process memory requests.
User Input Handling: Reads and processes input interactively, allowing the program to run continuously until the user quits.
Simulation of Algorithms: Implements an LRU-like caching strategy for memory management.

2. passport.py
Program Description:
This Python program models a Passport system with detailed functionality for tracking passport information, validating expiration dates, recording travel, and summarizing passport details. The program demonstrates object-oriented programming (OOP) concepts and uses Python's datetime module for date handling.

Skills:
Object-Oriented Programming (OOP):
Class Design: Passport class with attributes like first_name, dob, and methods for functionality.
Class Variables: Tracks the total number of passports issued.
Encapsulation: Methods like is_valid(), stamp(), and check_data() encapsulate specific functionality.
Date Handling: Converts and compares datetime.date objects to handle birth and expiration dates.
Dictionary Operations: Manages visited countries and visit counts using a dictionary.
Iterators and Generators: Provides iterable access to visited countries.
Custom Method Design: Includes methods for validation, travel history, and calculating the sum of squared visit counts.

Key Features:
Automatically generates unique passport numbers.
Validates passport expiration dates.
Tracks and summarizes travel history by stamping visited countries.
Compares input data with stored passport data for validation.
Calculates the sum of squares of visits to different countries.
