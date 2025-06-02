 # Project Brief: Mini Issue Tracker App

# Overview:
The Mini Issue Tracker App is a simple backend application built using FastAPI that allows users to create, view, update, and delete issue reports — similar to a lightweight bug-tracking or task management system.

The goal is to simulate the type of software typically developed and maintained in an Application Development & Maintenance (ADM) role — where both new functionality and ongoing support are crucial.

# Purpose:
Showcase full lifecycle thinking — from design and build to test and maintain.

Demonstrate core ADM skills: CRUD operations, clean code, version control, and documentation.

Practice building modular, maintainable Python applications using FastAPI and pytest.


# MVP (Minimum Viable Product)
The MVP for this Mini Issue Tracker App is a simple but functional web-based API that allows users to:

Create new issues with a title and description.

Read a list of all submitted issues or view a single issue by ID.

Update an existing issue’s title, description, or status (e.g. Open, In Progress, Closed).

Delete an issue by ID.

# Features:
POST /issues: Create a new issue (e.g., "Bug in login form")

GET /issues: Retrieve a list of all issues

GET /issues/{id}: Retrieve a single issue by ID

PUT /issues/{id}: Update an issue's status or description

DELETE /issues/{id}: Remove a resolved or invalid issue

# Tech Stack:
FastAPI – for API routing and documentation

Uvicorn – for local development server

Python standard library – for JSON-based in-memory storage (or SQLite for extra depth)

pytest – for writing unit tests

pydantic – for input validation and data models

# Testing:
Unit tests for all endpoints using pytest

Edge case coverage (e.g., invalid ID, missing data)

Clearly separated app.py, models.py, and test_app.py for readability

# Example Use Case:
Imagine this tracker being used internally by a small IT support team to:

Log new bugs from users

Track current issue statuses (Open, In Progress, Resolved)

Delete issues once resolved or marked as duplicate

