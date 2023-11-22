# Django Blog API

Welcome to the Django Blog API, a powerful API for managing and interacting with blog posts.

## Table of Contents

- [Prerequisites](#Prerequisites)
- [Getting Started](#getting-started)
- [Introduction](#introduction)
- [Endpoints](#endpoints)
- [Technologies](#technologies)
- [Usage](#usage)

## Prerequisites

Before you begin, ensure you have met the following requirements:

- [Python](https://www.python.org/)
- [Pipenv](https://pipenv.pypa.io/)
- [PostgreSQL](https://www.postgresql.org/)

Make sure to install the required Python packages in Virtualenironment using 
```
pipenv install
```

## Getting-started

- Install and set up PostgreSQL.
- Create a database for the project.
- Add the database configurations to db_config.py in the project's root:
``` python
DB_NAME = 'DATABASE NAME'
DB_USER = 'DATABASE USERNAME'
DB_PASSWORD = 'DATABASE PASSWORD'
```
- Apply migrations to the database:
``` bash
python3 manage.py makemigrations
```
``` bash
python3 manage.py migrate
```
- Enable two-step verification on your Google account.
- Generate an App Password on [Google App Password](https://myaccount.google.com/apppasswords).
- Add the app configurations to email_config.py in the project's root:
``` python
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'Email@gmail.com'
#password of the app
EMAIL_HOST_PASSWORD = 'XXXX XXXX XXXX XXXX'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
```
Load Initial Data
To load initial data for testing the API, run:
``` bash
python3 manage.py loaddata mysite_data.json
```
Note: Ensure you have migrated the database before running this command.

## Introduction

The Django Blog API is a versatile API designed for a blogging application. It provides handles various functionalities, including fetching blog posts, viewing single posts with similar recommendations, adding comments, sharing posts via email, generating an RSS feed, and performing full-text searches.

## Endpoints

1. **Blog (GET /blog/):**
   - Returns a paginated list of all blog posts.

2. **Single Post (GET /blog/\<int:year\>/\<int:month\>/\<int:day\>/\<slug:post_slug\>/):**
   - Retrieves a specific post and its comments.
   - Provides a list of similar posts using the Taggit package for tags.

3. **Comment (POST /blog/comment):**
   - Allows users to add comments to a specific post.<br>
   **NOTE**: require post(post_id), name, email, body(the comment)

4. **Share Post (POST /blog/share):**
   - Shares a post by sending an email to the specified recipient using Google SMTP.<br>
   **NOTE**: require name, recipent_email, post(post_id),comments(optinial comment to the recipent)

5. **Feed (GET /api/feed):**
   - Generates an RSS feed for the blog.

6. **Search (GET /api/search):**
   - Performs a full-text search on post titles and bodies for a given query.<br>
   **NOTE**: require query

## Technologies

- Python
- Django
- Django Rest Framework
- PostgreSQL

## Usage

Start the app by running:
``` bash
python3 manage.py runserver
```
Explore the API using the provided endpoints. You can use tools like [Insomnia](https://insomnia.rest/) or [curl](https://curl.se/) to interact with the API.