#Email Login
This is a simple OTP login project that demonstrates how to create a secure login process using One-Time Passwords (OTP).

**Features**
1. Request OTP via email
2. Verify OTP
3. OTP expire in 30 seconds
4. Request another OTP if the previous OTP is invalid

**Requirements**
- Django 3.1
- Python 3.8

**Installation**
- Clone the repository

`git clone https://github.com/[username]/otp-login.git`

- Run the development server

`python manage.py runserver`

**Usage**
- Open the application in your browser at http://127.0.0.1:8000/
- Enter your email address in the Email field and click on Request OTP
- Check your email for the OTP and enter it in the OTP field
- Click on Verify OTP
- If the OTP is valid, you will be logged in. If the OTP is invalid, you can request another OTP by clicking on the Request another OTP button.

**Contributing**
- Fork the repository
- Create your feature branch (git checkout -b feature/new-feature)
- Commit your changes (git commit -am 'Add new feature')
- Push to the branch (git push origin feature/new-feature)
- Create a new Pull Request
