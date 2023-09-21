# Statement of Purpose (SOP) Generator

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Usage](#usage)
  - [User Signup](#user-signup)
  - [User Login](#user-login)
  - [Generating SOP](#generating-sop)
- [Contributing](#contributing)
- [License](#license)

## Introduction

The Statement of Purpose (SOP) Generator is a tool designed to assist students in creating compelling SOPs for university applications. It offers a user-friendly interface for generating well-structured SOPs that can be tailored to individual experiences and goals.

## Features

- User authentication (Signup and Login)
- User-friendly input forms for SOP content
- Word limit validation for each SOP section
- Random OTP generation for user registration
- Integration with a MongoDB database for user data storage

## Getting Started

### Prerequisites

- Python 3.x
- MongoDB (for user data storage)
- Required Python packages (see [requirements.txt](requirements.txt))

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/sop-generator.git
   cd sop-generator
   ```
2. install the required Python packages:
    ```
    pip install -r requirements.txt

    ```
3. Set up MongoDB and configure the connection URL

### Usage
#### User-Signup
- Launch the application by running sop.py.
- Access the application in your web browser.
- Click on the "Signup" button.
- Fill in the required information, including your name, email, and mobile number.
- Complete the SOP-related sections with your content.
- Click the "Signup" button to register.
- An OTP will be sent to your mobile number for verification.

#### User-Login
- Access the application in your web browser.
- Click on the "Login" button.
- Enter your mobile number and OTP.
- Click the "Login" button to access the SOP Generator.

#### Generating-SOP
- After logging in, you will be able to fill in the SOP sections.
- Each section has word limit validation to ensure your SOP meets the requirements.
- Click the "Generate SOP" button to create your Statement of Purpose.

#### Contributing
Contributions are welcome! 

#### License
This project is licensed under the MIT License.