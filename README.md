# Is It My Birthday?

This project is a simple Django web application inspired by [isitchristmas.com](https://isitchristmas.com/). It displays whether today is your birthday or not.

By default it takes the 2nd of September (my Birthday) as the input.

## Features

- Displays a simple message indicating if today is your birthday.
- Configurable birthday date.
- Minimalistic and clean design.

## Prerequisites

- Python 3.x
- Django 3.x or higher

## Configure Your Birthday
Open the settings.py file and add your birthday date:

```
settings.py

# Add your birthday date (Month, Day)
BIRTHDAY = (7, 15)  # Example: July 15
```

## Getting Started

1. Clone the Repository
2. Run the Development Server
Start the Django development server:

```
python birthday/manage.py runserver