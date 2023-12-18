
Mecanico App
The Mecanico App is a simple Python application designed for managing motorcycle data. This application features a graphical user interface (GUI) built using the ttkbootstrap library for styling. Users can input motorcycle information, which is then stored in a MySQL database. The app also includes a table view for displaying and managing the entered data.


To run the Mecanico App, you need to install the required dependencies. Open a terminal and run the following command:


pip install ttkbootstrap mysql-connector-python

To use the Mecanico App, execute the following Python script:


python app.py
Replace app.py with the actual filename if it differs

Features
Data Input: Users can input motorcycle details such as Name, Patente, Modelo, Descripcion, and Monto.

Data Validation: Regular expressions are employed to validate the input data.

Database Interaction: The application connects to a MySQL database using the mysql-connector library. Submitted data is saved to the database.

Table View: A table displays the entered data, providing pagination and search functionality for ease of use.

Toast Notifications: Users receive toast notifications for errors during the data submission process.
