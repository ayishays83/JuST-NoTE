Demo-Vedio
[Click to view Demo](https://clipchamp.com/watch/9JDKI36AJwe)

# Note-App
The "JuST NoTE "Web Application is built using Python-Django as the backend framework and utilizes CSS, HTML, and JavaScript for the frontend. This application allows users to create, view, and delete notes securely.

# README File for Note Application

This document provides information on how to create, view, and delete notes using Python-Django, CSS, HTML, and JavaScript.

## Table of Contents

1. Introduction
2. Installation
3. Usage
4. Features
5. Security
6. Contributions

## 1. Introduction

The Secure Web Application is built using Python-Django as the backend framework and utilizes CSS, HTML, and JavaScript for the frontend. 
This application allows users to create, view, and delete notes securely.

## 2. Installation

To run the Secure Web Application, follow these steps:

1. Clone the repository from [Clone](https://github.com/ayishays83/JuST-NoTE.git).
2. Install Python and Django on your system.

3. Create a virtual environment using the following command:

       python -m venv myenv

4. Activate the virtual environment:

   - For Windows:

     		myenv\Scripts\activate

   - For macOS and Linux:

     		source myenv/bin/activate

5. Navigate to the project directory and install the required dependencies:

   		pip install -r requirements.txt

6. Run the migration command to set up the database

  
    	python manage.py migrate

7. Start the development server:

  		 python manage.py runserver

8. Open your web browser and access the application at[Local-Host]( `http://localhost:8000`.)

## 3. Usage

Once the JuST NoTE Web Application is running, follow these steps to create, view, and delete notes:

- Create a Note:

  - Click on the "Add Notes" button.

  - Enter the title and content of the note.

  - Click on the "Save" button to create the note.

- View Notes:

- All existing notes will be displayed on the page.only after adding new nodes

- Edited Notes:

- The user can modify the existing notes by clicking on the edit button. 

After making the changes, the user can save the notes. 

The modified notes will be updated automatically on the page.

- Delete a Note:

  - To delete a note, click on the "Delete" button next to the note you want to remove.

  - Confirm deletion when prompted.

## 4. Features

- Secure user authentication and authorization.

- Create, view, and delete notes.

- User-friendly interface with a responsive design.

- Validation checks for input fields.

## 5. Security

- User authentication to ensure only authorized users can access the application.

- Password hashing to protect user passwords in the database.

- CSRF protection to prevent cross-site request forgery attacks.

- Input validation to prevent malicious code injection.

- HTTPS encryption for secure data transmission.

## 6. Contributions

Contributions to the 'Just Note' Web Application are welcome. 

If you find any issues or have suggestions for improvement, please submit a pull request to the [Git-Hub](https://github.com/ayishays83/JuST-NoTE.git.)

