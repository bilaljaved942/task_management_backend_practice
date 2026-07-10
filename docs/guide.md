# Task Manager API
## Production-Grade Backend Learning Project

---

# Project Overview

This project is not just a Task Manager API. It is a complete backend engineering project built from scratch using modern software engineering principles.

The goal is to learn how production-grade backend applications are designed, developed, tested, containerized, and deployed.

Instead of only making APIs work, every component is built while understanding:

- Why it exists
- How it works internally
- Industry best practices
- Common interview questions
- Real-world software architecture

---

# Technology Stack

Backend
- FastAPI

Programming Language
- Python

Database
- PostgreSQL

ORM
- SQLAlchemy

Database Migrations
- Alembic

Authentication
- JWT
- bcrypt

Validation
- Pydantic v2

Containerization
- Docker

Testing
- Pytest

CI/CD
- GitHub Actions

Deployment
- Docker
- Kubernetes (Later)

---

# Project Architecture

Client
│
▼
FastAPI Router
│
▼
Service Layer
│
▼
Repository Layer
│
▼
SQLAlchemy ORM
│
▼
PostgreSQL

---

# Layer Responsibilities

## Router

Responsible for:

- Receiving HTTP requests
- Validating request data
- Calling services
- Returning responses

Router contains NO business logic.

---

## Service

Contains business logic.

Examples:

- Register User
- Login User
- Hash Password
- Generate JWT
- Validate business rules

Service never directly writes SQL.

---

## Repository

Responsible only for database operations.

Examples:

- Create User
- Find User by Email
- Update User
- Delete User

Repository knows SQLAlchemy.

Service does not.

---

## Database

Stores persistent data.

Tables:

- Users
- Tasks
- Alembic Version

---

# Project Folder Structure

app/

    api/
        routes/

    core/

    database/

    models/

    repositories/

    schemas/

    services/

    utils/

alembic/

tests/

docs/

---

# Development Roadmap

Phase 1
Project Setup

Phase 2
Authentication

Phase 3
Task CRUD

Phase 4
Testing

Phase 5
Docker

Phase 6
CI/CD

Phase 7
Production Deployment

---

# Phase 1
Project Setup

Completed

---

## Virtual Environment

Created project virtual environment.

Purpose

- Dependency isolation
- Reproducible builds

---

## FastAPI

Configured FastAPI application.

Created

- main.py

Added

Health endpoint

Purpose

Verify application is running.

---

## PostgreSQL

Pulled PostgreSQL Docker image.

Created Docker container.

Configured

- username
- password
- database

Learned

Container networking

Port Mapping

Docker volumes

---

## Docker Networking

Learned why

Host Port

↓

Container Port

Example

5432:5432

Host applications communicate through the mapped host port.

---

## SQLAlchemy

Configured

Engine

SessionLocal

Declarative Base

Purpose

Acts as bridge between Python objects and SQL.

---

## Alembic

Configured migration system.

Learned

Why migrations exist.

Difference between:

Model

↓

Migration

↓

Database

Alembic compares:

Base.metadata

with

Current Database

Then generates migration scripts.

---

## User Model

Created

User table

Fields

- id
- name
- email
- hashed_password
- created_at

Learned

Primary Keys

Unique Constraints

Indexes

Server Defaults

---

## First Migration

Generated

create users table

Applied

alembic upgrade head

Verified

- users table
- alembic_version table

Learned

upgrade()

downgrade()

Migration History

Revision IDs

---

## PostgreSQL Verification

Connected directly into PostgreSQL container.

Verified

\dt

Listed tables

Verified

\d users

Checked schema.

Verified

SELECT * FROM alembic_version;

Purpose

Never trust tools blindly.

Always verify database state.

---

# Authentication Phase

Currently In Progress

---

## Authentication Flow

Register

↓

Validate Request

↓

Hash Password

↓

Save User

↓

Return Success

---

Login

↓

Find User

↓

Verify Password

↓

Generate JWT

↓

Return Token

---

Protected Route

↓

Validate JWT

↓

Extract User ID

↓

Return Current User

---

# Schemas

Completed

Created

UserCreate

Purpose

Incoming registration request.

---

UserLogin

Purpose

Incoming login request.

---

UserResponse

Purpose

Outgoing response.

Never expose

hashed_password

---

Learned

Why database models should not be used as API responses.

---

# Security Layer

Started

Will include

Password Hashing

JWT Tokens

Password Verification

Access Tokens

Token Expiration

---

Current Issue

Python 3.14 compatibility.

passlib currently has compatibility issues with

bcrypt

Recommendation

Use Python 3.13 for long-term project stability.

---

# Upcoming Work

Repository Layer

Create

- create_user()
- get_user_by_email()
- get_user_by_id()

---

Service Layer

Business logic

Registration

Login

Password Validation

JWT Creation

---

Router

Create endpoints

POST /register

POST /login

GET /me

---

Task Module

Create Task Model

Relationships

Foreign Keys

Cascade Delete

Task CRUD

---

Testing

Unit Tests

Integration Tests

End-to-End Tests

---

Docker

Dockerfile

Docker Compose

---

CI/CD Pipeline

Developer Push

↓

Build

↓

Unit Tests

↓

Integration Tests

↓

Security Scan

↓

Code Quality

↓

Docker Image

↓

Deploy to Staging

↓

End-to-End Tests

↓

Deploy to Production

---

Production Topics

Logging

Monitoring

Health Checks

Environment Variables

Error Handling

Rate Limiting

Security Headers

---

Concepts Learned

SQLAlchemy ORM

Alembic

Database Migrations

Docker

PostgreSQL

Container Networking

Port Mapping

Pydantic Schemas

Layered Architecture

Repository Pattern

Service Layer

Router Layer

Database Verification

Migration Lifecycle

---

Project Goal

By the end of this project I should understand not only how to build a backend application, but also why every architectural decision is made.

The objective is to be able to confidently design, build, test, deploy, and explain a production-grade backend system during software engineering interviews and in real-world development.