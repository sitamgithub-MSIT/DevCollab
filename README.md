# DevCollab

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

## Features

## Installation

### Prerequisites

- Git
- Python (v3.10 or any other compatible version)
- pip (latest version)
- PostgreSQL (or any other preferred database if you want to use a different one other than the default)

### Steps

1. Clone the repository: `git clone https://github.com/yourusername/DevCollab.git`
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

- `DJANGO_SECRET_KEY`: The secret key for the Django project
- `DEBUG`: Set to `True` for development, `False` for production

If you are using a different database, you will also need to set the following variables:

- `DB_HOST`: The hostname of the database server
- `DB_USER`: The username for the database connection
- `DB_PASSWORD`: The password for the database connection
- `DB_NAME`: The name of the database to use

## Usage

To start the development server, run `python manage.py runserver`. Access the application by navigating to `http://localhost:8000` in your web browser.

## Running Tests

## Deployment

For deployment options, you can use vercel as a serverless deployment platform. You can deploy the Django project using the Vercel Serverless Functions. The project is already set up to work with Vercel, so you can deploy it directly from the repository.

Files reponsible for the deployment are:

- `vercel.json`: This file contains the configuration for the Vercel deployment. It specifies the routes and the serverless functions to use for the deployment.
- `build_files.sh`: This script is used to build the project before deployment. It installs the dependencies and runs the collectstatic command to collect the static files.

Please refer to the Vercel documentation for more information on how to deploy a Django project using Vercel.

## Contributing

Contributions are welcome! If you would like to contribute to this project, please raise an issue to discuss the changes you would like to make. Once the changes are approved, you can create a pull request.

## License

DevCollab is released under the [MIT License](LICENSE). See `LICENSE` for more details.

## Contact

If you have any questions or suggestions regarding the project, feel free to reach out to me on my GitHub profile.

Happy coding! 🚀
