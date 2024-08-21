<p align="center">
  <img src="https://cdn-icons-png.flaticon.com/512/6295/6295417.png" width="100" />
</p>
<p align="center">
    <h1 align="center">GYM-MANAGEMENTS</h1>
</p>
<p align="center">
	<img src="https://img.shields.io/github/license/techdev59/gym-managements.git?style=flat&color=0080ff" alt="license">
	<img src="https://img.shields.io/github/last-commit/techdev59/gym-managements.git?style=flat&logo=git&logoColor=white&color=0080ff" alt="last-commit">
	<img src="https://img.shields.io/github/languages/top/techdev59/gym-managements.git?style=flat&color=0080ff" alt="repo-top-language">
	<img src="https://img.shields.io/github/languages/count/techdev59/gym-managements.git?style=flat&color=0080ff" alt="repo-language-count">
<p>
<p align="center">
		<em>Developed with the software and tools below.</em>
</p>
<p align="center">
	<img src="https://img.shields.io/badge/Python-3776AB.svg?style=flat&logo=Python&logoColor=white" alt="Python">
	<img src="https://img.shields.io/badge/Django-092E20.svg?style=flat&logo=Django&logoColor=white" alt="Django">
	<img src="https://img.shields.io/badge/PostgreSQL-4169E1.svg?style=flat&logo=PostgreSQL&logoColor=white" alt="PostgreSQL">
	<img src="https://img.shields.io/badge/Django%20REST%20Framework-092E20.svg?style=flat&logo=Django&logoColor=white" alt="Django REST Framework">
</p>
<hr>

##  Quick Links

> - [ Overview](#-overview)
> - [ Features](#-features)
> - [ Repository Structure](#-repository-structure)
> - [ Getting Started](#-getting-started)
>   - [ Environment Variables](#environment-variables)
>   - [ Installation](#-installation)
>   - [ Running gym-managements](#-running-gym-managements)
> - [ Project Roadmap](#-project-roadmap)
> - [ Contributing](#-contributing)
> - [ License](#-license)
> - [ Acknowledgments](#-acknowledgments)

---

##  Overview


## Overview

The **Gym Management System** is a comprehensive web-based platform designed to streamline the management of gym operations, including member registration, class scheduling, trainer assignments, and payment processing. Built using Django and Django Rest Framework (DRF), the system supports dynamic databases for each gym branch, ensuring that each branch's data is managed independently while providing a unified interface for administrators. The system is designed with scalability in mind, making it suitable for gyms of all sizes.

## Features

- **Dynamic Database Routing**: 
  - Each gym branch has its own database, allowing for separate management of members, trainers, classes, and payments.
  - The system dynamically routes database operations based on the `db_name` query parameter, ensuring data separation and security.

- **Member Management**: 
  - Add, update, retrieve, and delete member information.
  - Track member entry and exit times to monitor gym usage.

- **Trainer Management**: 
  - Add and manage gym trainers with their specialties and contact details.
  - Assign trainers to gym classes for better class management.

- **Gym Class Scheduling**: 
  - Create and manage gym classes, assign trainers, and enroll members.
  - Manage class timings and attendance records efficiently.

- **Payment Tracking**:
  - Record and manage member payments, including support for multiple payment methods (online and cash).
  - Track payment history and generate financial reports.

- **RESTful API**: 
  - A robust REST API built with Django Rest Framework (DRF) enables seamless integration with frontend applications.
  - The API supports full CRUD operations for all models, making it easy to interact with the system programmatically.

- **Authentication and Security**: 
  - Integrated user authentication using Django’s built-in authentication system.
  - Permission-based access control ensures that only authorized users can access and modify data.

- **Scalable Architecture**: 
  - The system’s architecture is designed for scalability, making it easy to add more gym branches or integrate new features as your business grows.

- **Flexible Data Model**: 
  - The data model supports various types of gym operations, including member subscriptions, class scheduling, trainer management, and payment processing.
  - Customizable to meet the specific needs of different gym environments.

---


##  Repository Structure

```sh
└── gym-managements/
    ├── README.md
    ├── accounts
    │   ├── __init__.py
    │   ├── admin.py
    │   ├── apps.py
    │   ├── management
    │   │   ├── __init__.py
    │   │   └── commands
    │   │       ├── __init__.py
    │   │       └── init_gym.py
    │   ├── models.py
    │   ├── tests.py
    │   └── views.py
    ├── gym
    │   ├── __init__.py
    │   ├── asgi.py
    │   ├── db_routers.py
    │   ├── settings.py
    │   ├── urls.py
    │   └── wsgi.py
    ├── manage.py
    ├── management
    │   ├── __init__.py
    │   ├── admin.py
    │   ├── apps.py
    │   ├── models.py
    │   ├── serializers.py
    │   ├── tests.py
    │   ├── urls.py
    │   └── views.py
    └── requirements.txt
```



##  Getting Started

***Requirements***

Ensure you have the following dependencies installed on your system:

* **Python**: `version 3.12`

### Environment Variables

To configure the database and other project settings, you need to set up a `.env` file in the root of your project. Below is an example of the required environment variables:

### Example `.env` File

```bash
# General Settings
DEBUG=True
SECRET_KEY=your_secret_key_here

# Database Configuration for PostgreSQL
DB_ENGINE=django.db.backends.postgresql
DB_NAME=your_database_name_here
DB_USER=your_database_user_here
DB_PASSWORD=your_database_password_here
DB_HOST=your_database_host_here
DB_PORT=5432  # Default PostgreSQL port


```

###  Installation

1. Clone the salon-management repository:

```sh
git clone https://github.com/techdev59/salon-management.git
```

2. Change to the project directory:

```sh
cd salon-management
```

3. Create virtual environment:

```sh
python -m venv venv
```

3. Activate virtual environment:

for wundows
```sh
venv\Scripts\activate
```
for linux
```sh
Source venv/bin/activate
```


4. Install the dependencies:

```sh
pip install -r requirements.txt
```

###  Running salon-management

Use the following command to run salon-management:

```sh
python manage.py runserver
```


## To apply migrations 

first use this command

```sh
python manage.py makemigrations
```
then apply all the migrations
```sh
python manage.py migrate
```

##  Contributing

Contributions are welcome! Here are several ways you can contribute:

- **[Submit Pull Requests](https://github.com/techdev59/gym-managements.git/blob/main/CONTRIBUTING.md)**: Review open PRs, and submit your own PRs.
- **[Join the Discussions](https://github.com/techdev59/gym-managements.git/discussions)**: Share your insights, provide feedback, or ask questions.
- **[Report Issues](https://github.com/techdev59/gym-managements.git/issues)**: Submit bugs found or log feature requests for Gym-managements.

<details closed>
    <summary>Contributing Guidelines</summary>

1. **Fork the Repository**: Start by forking the project repository to your GitHub account.
2. **Clone Locally**: Clone the forked repository to your local machine using a Git client.
   ```sh
   git clone https://github.com/techdev59/gym-managements.git
   ```
3. **Create a New Branch**: Always work on a new branch, giving it a descriptive name.
   ```sh
   git checkout -b new-feature-x
   ```
4. **Make Your Changes**: Develop and test your changes locally.
5. **Commit Your Changes**: Commit with a clear message describing your updates.
   ```sh
   git commit -m 'Implemented new feature x.'
   ```
6. **Push to GitHub**: Push the changes to your forked repository.
   ```sh
   git push origin new-feature-x
   ```
7. **Submit a Pull Request**: Create a PR against the original project repository. Clearly describe the changes and their motivations.

Once your PR is reviewed and approved, it will be merged into the main branch.

</details>

---

##  License

This project is protected under the [SELECT-A-LICENSE](https://choosealicense.com/licenses) License. For more details, refer to the [LICENSE](https://choosealicense.com/licenses/) file.

---

## Acknowledgments


We would like to express our gratitude to the following communities and individuals:

- **Django Community**: For providing a powerful, flexible, and well-documented web framework that makes developing complex applications manageable and enjoyable.
- **Django Rest Framework (DRF)**: For enabling the creation of robust and flexible RESTful APIs, making integration with frontend applications seamless.
- **Open Source Contributors**: To all the developers and maintainers of the open-source packages that this project relies on. Your contributions make the software ecosystem thrive.
- **Stack Overflow and Online Communities**: For offering a wealth of knowledge, troubleshooting tips, and support that make overcoming development challenges easier.
- **Gym Owners and Trainers**: For providing valuable insights into gym operations and helping shape the features of this management system.
- **Contributors to This Project**: To everyone who has contributed their time and skills to improve this project, from developers to testers and designers. Your contributions are invaluable.
  

[**Return**](#-quick-links)

---
