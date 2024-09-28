# International Student Visa Facilitator POC

## Description
The International Student Visa Facilitator is a Proof of Concept (POC) developed to manage student visa records effectively. This program implements CRUD (Create, Read, Update, Delete) operations for visa records, assists international students in obtaining or renewing their visas, and monitors visa processing times. Built using object-oriented programming (OOP) principles in Python, this system aims to streamline the visa management process for educational institutions and students.

## Features
- **CRUD Operations**: Manage student visa records, including adding, viewing, updating, and deleting records.
- **Visa Assistance**: Provide support to international students during the visa application and renewal process.
- **Processing Time Monitoring**: Track and report the durations of visa processing.

## Entity Definition
### Classes
- **Student**: Represents a student, containing attributes such as student ID and name.
- **VisaRecord**: Manages visa-related information such as type, status, and processing ID.
- **VisaFacilitator**: Facilitates CRUD operations and provides assistance with visa processes.

## Data Structures
- **List**: Used to store collections of `VisaRecord` instances for easy management.
- **Dictionary**: Enables quick access to visa records based on student IDs.

## Installation
1. Clone the repository:
   ```bash
   git clone <repository-url>
