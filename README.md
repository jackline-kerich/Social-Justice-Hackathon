Finsavvy - Financial Literacy App
Overview
Finsavvy is a financial literacy app that empowers users to manage their personal finances by offering essential tools and lessons in budgeting, saving, investing, and debt management. Built using Python (Django) for the backend, HTML, CSS, and JavaScript for the frontend, this app provides interactive learning modules, real-time financial tips, personalized budget tracking, and quizzes to test financial knowledge.

Features
Learning Modules:

Structured lessons on essential financial skills including:
Budgeting Basics
Debt Management
Smart Saving Strategies
Investment Fundamentals
Retirement Savings
Financial Planning & Goal Setting
Managing Financial Risks
Tax Planning
Building Wealth Over Time
Emergency Fund Creation
Interactive Quizzes:

Sector-specific quizzes to reinforce lessons and engage users with real-life scenarios.
Personalized Budget Planner:

Users can categorize expenses, set budgets, and track progress.
Goal Setting & Tracking:

Set and track financial goals such as emergency savings, investments, or retirement.
Real-Time Financial Tips:

Notifications triggered by user financial activity, providing tips for better financial management.
Installation
Prerequisites
Python
Django
Git
Clone the Repository
Clone this repository to your local machine:

bash
Copy code
git clone https://github.com/jackline-kerich/Social-Justice-Hackathon.git
Install Dependencies
Navigate to your project directory and install the necessary dependencies:

bash
Copy code
cd financialliteracy
pip install -r requirements.txt
Database Setup
Make migrations:
bash
Copy code
python manage.py makemigrations
Migrate the database:
bash
Copy code
python manage.py migrate
Run the Development Server
Once the setup is complete, you can start the Django development server:

bash
Copy code
python manage.py runserver
Visit http://127.0.0.1:8000/ in your browser to interact with the app.

Frontend Structure
HTML: Handles the structure of the app’s pages.
CSS: Provides styling for the user interface.
JavaScript: Enhances interactivity, including the quizzes and real-time financial tips.
Usage
Sign Up/Login: New users can create an account or log in to access the dashboard.
Dashboard: From the dashboard, users can access learning modules, set goals, and track budgets.
Quizzes: Users can take quizzes after completing lessons to test their understanding.
Deployment
Netlify for Frontend (Optional)
You can deploy the static frontend on Netlify. For instructions, check the Netlify Docs.

Django Deployment
Deploy your Django app using services like:

Heroku
PythonAnywhere
AWS or DigitalOcean
Testing
Unit Testing
Django provides built-in testing tools. To test your app, run:

bash
Copy code
python manage.py test
Cross-Browser Testing
Test your app in different browsers (Chrome, Firefox, Safari, etc.) using built-in Developer Tools to ensure compatibility and responsiveness.

Technologies Used
Backend: Python (Django)
Frontend: HTML5, CSS3, JavaScript
Database: SQLite (default) 
Contributing
We welcome contributions to make Finsavvy even better. Here’s how you can contribute:

Fork the repository.
Create your feature branch: git checkout -b feature-name
Commit your changes: git commit -m 'Add new feature'
Push to the branch: git push origin feature-name
Open a pull request.
License
This project is licensed under the MIT License. See the LICENSE file for details.

Contact
For any inquiries or feedback, contact:

GitHub: jackline-kerich
