# DevCollab

Demo: [DevCollab](/)

**Note**: After running the project on deployment for a few months, I decided to take it down. You can still run the project locally by following the instructions below.

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Installation](#installation)
- [Configuration](#configuration)
- [Usage](#usage)
- [Running Tests](#running-tests)
- [Deployment](#deployment)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

## Introduction

DevCollab is a forum-like web application that enables developers to collaborate, share ideas, and learn from each other. It allows beginners to learn from experienced developers and experienced ones to help others and share their knowledge.

## Features

- _User Authentication_: Users can sign up, log in, and log out of the application using their email address and password. It uses Django's built-in session-based authentication system for user authentication.
- _User Profile_: Users can create a profile with their name, email address, bio, and profile picture. They can update their profile information and change their profile picture.
- _Topics_: Users can create topics to discuss specific subjects, ask questions, and share information with other users. They can view topics created by other users and participate in discussions.
- _Categories_: Topics are organized into categories to help users find topics related to specific subjects. Users can create categories and assign topics to them.
- _Comments_: Users can comment on topics to share their thoughts, ask questions, and provide feedback. They can view comments made by other users and reply to them.
- _Activity Feed_: Users can view an activity feed that displays recent topics, comments, and replies made by other users. They can see updates from other users and stay informed about the latest discussions.
- _Search_: Users can search for topics, categories, and users using the search bar. They can enter keywords to find relevant content and filter the search results based on different criteria.
- _Responsive Design_: The application is designed to be responsive and mobile-friendly, allowing users to access it on different devices and screen sizes. It uses CSS media queries to adjust the layout and styling based on the device's screen size.
- _Admin Panel_: Administrators can manage users, topics, categories, and comments using the Django admin panel. They can view, create, update, and delete content to maintain the application and ensure its smooth operation.
- _Serverless Deployment_: The application can be deployed using serverless functions on platforms such as Vercel. It uses serverless functions to handle requests and responses, making it scalable and cost-effective for hosting the application.

## Technologies

### Tech Stack

- Backend: Python, Django
- Frontend: HTML, CSS, JavaScript

### Libraries and Dependencies

- PyCharm/VS Code: IDE for writing code
- Required Module Are In The requiements.txt

**Note**: All the dependencies are pushed along with code to run the project smoothly

## Installation

### Prerequisites

- Git
- Python (v3.10 or any other compatible version)
- pip (latest version)
- PostgreSQL (or any other preferred database if you want to use a different one other than the default)

### Steps

1. Clone the repository: `git clone https://github.com/sitamgithub-MSIT/DevCollab.git`
2. Change into the project directory: `cd DevCollab`
3. Create a virtual environment: `python -m venv env`
4. Activate the virtual environment:
   - On Windows: `env\Scripts\activate`
   - On macOS/Linux: `source env/bin/activate`
5. Install dependencies: `pip install -r requirements.txt`

If you want to use a different database other than the default SQLite database, follow these additional steps:

6. Set up the database:
   - Create a PostgreSQL database
   - Update the database settings in `settings.py`
7. Run initial migrations: `python manage.py migrate`

## Configuration

Set up your environment variables as described in `env.example`. You can create a `.env` file in the root directory of the project and add the required variables. Make sure to replace the placeholder values with your own. Here are some of the key variables you need to configure:

- `SECRET_KEY`: The secret key for the Django project
- `DEBUG`: Set to `True` for development, `False` for production

If you are using a different database, you will also need to set the following variables:

- `DB_NAME`: The name of the database to use
- `DB_USER`: The username for the database connection
- `DB_PASSWORD`: The password for the database connection
- `DB_NAME`: The name of the database to use
- `DB_HOST`: The hostname of the database server
- `DB_PORT`: The port number of the database server

You can also configure other Django settings in the `settings.py` file. Refer to the [Django documentation](https://docs.djangoproject.com/en/3.2/ref/settings/) for more information on the available settings.

## Usage

To start the development server, run `python manage.py runserver`. Access the application by navigating to `http://localhost:8000` in your web browser.

## Running Tests

## Deployment

For deployment options, you can use Vercel as a serverless deployment platform. You can deploy the Django project using the Vercel Serverless Functions. The project is already set up to work with Vercel, so you can deploy it directly from the repository.

The files responsible for the deployment are:

- `vercel.json`: This file contains the configuration for the Vercel deployment. It specifies the routes and serverless functions to use for the deployment.
- `build_files.sh`: This script is used to build the project before deployment. It installs the dependencies and runs the collectstatic command to collect the static files.

Please refer to the Vercel documentation for more information on how to deploy a Django project using Vercel.

## Contributing

Contributions are welcome! If you would like to contribute to this project, please raise an issue to discuss the changes you would like to make. Once the changes are approved, you can create a pull request.

## License

DevCollab is released under the [MIT License](LICENSE). See `LICENSE` for more details.

## Contact

If you have any questions or suggestions regarding the project, feel free to reach out to me on my GitHub profile.

Happy coding! 🚀
