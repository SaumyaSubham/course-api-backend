# course-api-backend

### Overview

This repository contains the backend of the Course Management System, built using Django and Django REST Framework. The API allows for managing courses and course instances, including creating, viewing, and deleting courses.

### Features

- **Course Management**: Create, retrieve, update, and delete courses.
- **Course Instances**: Manage course instances for specific semesters and years.
- **REST API**: Exposes endpoints to interact with the application programmatically.

### Technologies Used

- **Django**: The main web framework.
- **Django REST Framework**: For building the RESTful API.
- **PostgreSQL**: Relational database to store course information.
- **Docker**: Containerization of the application for consistent deployment.

### Prerequisites

- Docker and Docker Compose installed on your local machine.
- PostgreSQL for database management.

### Getting Started

### 1. Clone the Repository
```
git clone https://github.com/your-username/course-api-backend.git
cd course-api-backend 
```
### 2. Set Up Environment Variables
Create a .env file in the root of the project to define environment-specific variables.
```
DEBUG=True
SECRET_KEY=your-secret-key
DATABASE_URL=postgres://username:password@host:port/database_name
```
### 3. Build and Run with Docker
```
docker-compose up -d --build
```
### 4. Access the Application
The backend API will be running on http://localhost:8001.

### 5. API Endpoints
GET /api/courses: List all courses.
<br /> POST /api/courses: Create a new course.
<br /> GET /api/courses/<int:pk>: Retrieve course details.
<br /> DELETE /api/courses/<int:pk>: Delete a course.
<br /> GET /api/instances: List course instances.
<br /> More detailed API documentation is available within the code.

### Testing
To run tests:
```
docker-compose exec backend python manage.py test
```
### CI/CD Workflow
This repository uses GitHub Actions for CI/CD. Docker images are automatically built and pushed to DockerHub upon merging changes to the main branch.

### GitHub Actions Workflow
The .github/workflows/docker-image.yml file is set up to automate the building and pushing of Docker images. Here's what it does:

**Build the Docker Image:** The image is built based on the Dockerfile in the repository.
<br /> **Push to DockerHub:** The image is then pushed to your DockerHub repository.

### Contributing
Feel free to fork this repository and submit pull requests. All contributions are welcome!
