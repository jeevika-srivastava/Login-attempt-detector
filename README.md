# Login-attempt-detector

## Project Overview
This is a basic Python cybersecurity project that simulates a login system with limited password attempts.

The program allows a user to enter a password and blocks access after multiple failed login attempts.

## Features
- User password input
- Maximum 3 login attempts
- Access granted on correct password
- Access blocked after repeated failed attempts

## Concepts Used
- Python loops
- Conditional statements (if-else)
- Counter variables
- Basic authentication logic

## How to Run It
Run the script directly through your terminal or command prompt:

```bash
python login_attempt_detector.py
```

## Example Output

Enter password: test123  
Wrong password  

Enter password: admin123  
Login successful

OR

Enter password: wrong  
Wrong password  

(After 3 wrong attempts)

Too many failed attempts. Access blocked.

## Language Used
Python

## Purpose
This project demonstrates a simple authentication mechanism used in cybersecurity systems to prevent unauthorized access.