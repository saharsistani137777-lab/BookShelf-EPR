 BookShelf-EPR
 A simple student project to practice EPR, versioning, and basic software engineering concepts
 Overview

BookShelf-EPR is a practice project for my software development course.
The idea is inspired by digital book platforms (like Taaghche), but this project is only for learning purposes and does not copy any real code or commercial features.

The main goal is to understand how software projects are structured and how developers deal with things like versions, bugs, and documentation

Goals of the Project
Learn how to write a basic EPR (Engineering Process Report)
Practice versioning and see why sometimes old versions can be more stable
Understand how bugs are tracked and fixed
Learn about library responsibility (who made which library and why it matters)
Use a simple backend + frontend structure
Work with open-source licenses and see how they protect developers

Libraries and Dependencies
| Library  | Why I used it          | Author                |
| -------- | ---------------------- | --------------------- |
| FastAPI  | To create a simple API | Sebastián Ramírez     |
| Uvicorn  | To run the API server  | Encode / Tom Christie |
| Pydantic | For data validation    | Samuel Colvin         |
| Pytest   | For simple testing     | Community project     |


Frontend
HTML
CSS
JavaScript
(all standard W3C technologies)

EPR (Short Summary)
The EPR file in the project includes:
what the project is supposed to do
how I planned the structure
steps of development
what bugs I found
what I fixed
small release notes for each version
This helps me practice writing documentation in a simple way

Versioning
I followed a very basic versioning style:
v0.1 → first try, simple API, not stable
v0.2 → fixed small bugs, cleaner structure
v1.0 → more stable version
This is to show what we discussed in class:
Sometimes older versions become more stable because their bugs are already found.

Testing
I added a very small test file in the tests/ folder using pytest just to check that the API works.

License
This project uses the Apache License 2.0.
This license makes it clear who the developer is and protects me from legal responsibility in case someone misuses the project.

Developer: Sahar Sistani






