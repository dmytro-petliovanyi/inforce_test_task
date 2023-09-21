# inforce_test_task

### For using docker enter to terminal this command: docker compose up
#### Access the API at http://localhost:8001/api/

### To run server use: cd lunch_decision && python manage.py runserver
#### Access the API at http://localhost:8000/api/

## Features

- CRUD operations for managing restaurants.
- CRUD operations for managing menus for each restaurant.
- Voting for menus of the day.
- Managing employees and their positions.
- Retrieving the menu with the most votes for the current day.
- Retrieving all votes made for the current day.

### Prerequisites

- [Docker](https://docs.docker.com/get-docker/)
- [Docker Compose](https://docs.docker.com/compose/install/)



## API Endpoints:

- GET /api/restaurants: Retrieve a list of restaurants.
- POST /api/restaurants: Create a new restaurant.
- GET /api/menus: Retrieve a list of menus.
- POST /api/menus: Create a new menu.
- GET /api/votes: Retrieve a list of votes.
- POST /api/votes: Create a new vote.
- GET /api/employees: Retrieve a list of employees.
- POST /api/employees: Create a new employee.
- GET /api/current-day-menu: Retrieve the menu with the most votes for today.
- GET /api/current-day-results: Retrieve all votes made for today.
- POST /api/token: Obtain an authentication token.
- POST /api/token/refresh: Refresh an authentication token.
