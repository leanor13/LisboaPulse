# Lisboa Pulse

Lisboa Pulse is a microservices-based application designed to track and display events happening in the city of Lisbon. It allows users to view upcoming events such as concerts, exhibitions, and more. Admins can manage event listings manually or via automated scraping of event websites. The project is built to practice microservices architecture using Django, FastAPI, RabbitMQ, PostgreSQL, Celery, and more, with future deployment on AWS.

## Architecture Overview

Lisboa Pulse is built using the microservices approach to ensure scalability and modularity. Each microservice is responsible for a specific domain of the application, and they communicate asynchronously using RabbitMQ as the message broker.

### Core Technologies

- **Python**
- **Django** for user management, admin interface, and core event management.
- **FastAPI** for the scraper service.
- **PostgreSQL** as the primary database.
- **RabbitMQ** for message brokering between services.
- **Celery** for managing asynchronous tasks like scraping and background jobs.
- **Poetry** for dependency management.
- **Telegram Bot API** for user interaction through a bot.
- **AWS** for deployment (future goal).

---

## Microservice Structure

### High-Level Microservices Overview

1. **User Management Service (Django)**: Handles authentication, user roles (admin and regular users), and manages admin tasks via the Django admin panel.
2. **Event Management Service (Django)**: Stores and serves event data, providing API endpoints to retrieve and filter events based on various parameters.
3. **Scraper Service (FastAPI)**: Automates the process of scraping external event pages to gather new events into the system.
4. **Background Task Service (Celery + RabbitMQ)**: Manages asynchronous background tasks such as periodic scraping, event database cleanup, and more.
5. **Telegram Bot Service**: Acts as a front-end for user interaction, allowing both users and admins to interact with the system via Telegram.

---

### Detailed Service Description

#### 1. User Management Service (Django)
- **Responsibilities**:
  - Authentication and user management (admins and regular users).
  - Provides access control (admins can manage events, regular users can only view them).
  - Django Admin interface for manual event management.
- **Technologies**:
  - **Django** + **Django REST Framework** for the API.
  - **PostgreSQL** for user data storage.
  - **Celery** for background tasks (e.g., user activity tracking).
  - **Poetry** for dependency management.

#### 2. Event Management Service (Django)
- **Responsibilities**:
  - Store event data such as title, date, price, description, tags, and comments.
  - Serve event data via REST API endpoints.
  - Provide filtering options based on parameters like date, price, and tags.
  - Handle event creation, updating, and deletion.
  - Clean up old events from the database.
- **Technologies**:
  - **Django** + **Django REST Framework**.
  - **PostgreSQL** for storing event information.
  - **Celery** for periodic database cleanup.
  - **RabbitMQ** to receive tasks for new event creation and updates.
  - **Poetry** for dependency management.

#### 3. Scraper Service (FastAPI)
- **Responsibilities**:
  - Scrapes external websites (defined by admin) for new events.
  - Uses ChatGPT API to parse and extract event details from pages.
  - Sends data to Event Management Service to add new events.
- **Technologies**:
  - **FastAPI** for the scraping logic.
  - **Celery** to schedule and execute scraping tasks.
  - **RabbitMQ** as the message broker between scraping jobs and the event service.
  - **PostgreSQL** (optional) for temporary storage of raw data before processing.
  - **Poetry** for dependency management.

#### 4. Background Task Service (Celery + RabbitMQ)
- **Responsibilities**:
  - Manage background tasks such as scraping events weekly, cleaning up old events, and sending notifications.
  - Ensures scalability and asynchronous processing across services.
- **Technologies**:
  - **Celery** for asynchronous job execution.
  - **RabbitMQ** as the broker for communication between services.
  - **Poetry** for dependency management.

#### 5. Telegram Bot Service
- **Responsibilities**:
  - Allows users to interact with the event system via Telegram.
  - Regular users can query for upcoming events based on filters.
  - Admins can receive notifications, add URLs for scraping, and manage events through the bot.
- **Technologies**:
  - **Telegram Bot API**.
  - **FastAPI** to handle the bot logic and route interactions.
  - **RabbitMQ** to communicate with other services.
  - **Poetry** for dependency management.

---

## Future Enhancements

- **Favorite Events**: Allow users to bookmark favorite events and get notifications about them.
- **Google/Apple Calendar Integration**: Add events directly to users’ calendars.
- **Social Media Parsing**: Add scraping capabilities for Facebook, Instagram, and Telegram channels.
- **Multilingual Support**: Implement support for multiple languages (starting with English).
- **AWS Deployment**: Scale the system using AWS services like EC2, RDS (PostgreSQL), and SQS (for message brokering).

---

## Getting Started

### Prerequisites

- Python 3.8+
- Docker (for RabbitMQ and PostgreSQL)
- Poetry (for dependency management)

