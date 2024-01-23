# APIToFront

APIToFront is a simple full-stack web application built with Flask (backend) and React (frontend). This project provides a basic example of how to create a basic API and load data from it using react hook and component.

## Features

- Backend API built with Flask
- Frontend UI built with React
- Dockerized both the frontend and backend
- Uses Docker Compose to orchestrate containers

## Prerequisites

Before you begin, ensure you have met the following requirements:

- [Docker](https://docs.docker.com/get-docker/) installed on your system.

## Getting Started

To get this project up and running, follow these steps:

1. Clone this repository to your local machine:

   ```bash
   git clone <repository_url>
   ```

2. Build and run the backend image:

   ```bash
   cd backend
   docker build -t backend-image .
   docker run -d -p 8080:8080 backend-image
   ```

3. Build and run the frontend image:

   ```bash
   cd frontend
   docker build -t frontend-image .
   docker run -d -p 3000:3000 frontend-image
   ```

4. Use Docker Compose to start both frontend and backend containers:

   ```bash
   docker-compose up
   ```

## Usage

- Access the frontend at `http://localhost:3000` in your web browser and backend at `http://localhost:8080`
- The frontend will interact with the Flask backend, and you can use the UI to fetch and manipulate data from the API.

## API Endpoints

- GET `/books`: Get a list of all books.
- GET `/books/:id`: Get a book by ID.
- POST `/books`: Create a new book.
- PUT `/books/:id`: Update a book by ID.
- DELETE `/books/:id`: Delete a book by ID.
