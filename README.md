# sat_results_app.py

SAT Results Management System
This repository contains an application for managing SAT results. The application allows users to perform various operations such as inserting data, viewing all data, getting ranks, updating scores, and deleting records. The data is stored in memory and can be accessed through a simple command-line interface.

Features
Insert Data: Allows the user to input SAT result data, including the candidate's name, address, city, country, pincode, and SAT score. The "Passed" field is automatically calculated based on the SAT score.
View All Data: Displays all the SAT result data stored in memory in JSON format.
Get Rank: Takes a candidate's name as input and returns their rank based on their SAT score.
Update Score: Enables the user to update the SAT score for a candidate by their name.
Delete Record: Deletes a record from the SAT result data by the candidate's name.

Usage
To run the application, execute the main.py file in a Python environment. The application will present a menu with numbered options. Simply enter the corresponding number to select an operation.

