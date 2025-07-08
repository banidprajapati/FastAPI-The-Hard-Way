Done using the tutorial:
https://www.fastapitutorial.com/blog/fastapi-course/

# FastAPI Blog Project

A blog application built with FastAPI, SQLAlchemy, and PostgreSQL.

## Features
- User authentication with JWT
- Blog CRUD operations
- Database models with relationships
- Pydantic schemas for validation

## Setup
1. Install dependencies: `pip install -r requirements.txt`
2. Set up database
3. Run: `uvicorn main:app --reload`

## API Endpoints
- POST /token - Login
- POST /blogs - Create blog
- GET /blogs - List blogs
- GET /blogs/{id} - Get blog by ID
