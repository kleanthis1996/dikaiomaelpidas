# Django Project Setup Guide

This guide provides instructions on how to set up and run this Django project locally.

## Prerequisites
- Python 3.8+
- pip
- virtualenv (optional but recommended)

## Installation

### 1. Clone the Repository
```bash
git clone <repository-url>
cd <project-name>
```

### 2. Create a Virtual Environment
```bash
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Configure Environment Variables
Create a `.env` file in the root directory and add the necessary environment variables:
```
SECRET_KEY=your_secret_key
DEBUG=True
DATABASE_URL=sqlite:///db.sqlite3  # Change if using PostgreSQL or MySQL
```

### 5. Apply Migrations
```bash
python manage.py migrate
```

### 6. Create a Superuser (Optional)
```bash
python manage.py createsuperuser
```
Follow the prompts to create an admin user.

### 7. Run the Development Server
```bash
python manage.py runserver
```
The project should now be accessible at `http://127.0.0.1:8000/`.

## Additional Commands

### Running the Shell
```bash
python manage.py shell
```

### Collect Static Files
```bash
python manage.py collectstatic
```

## Contributing
- Fork the repository
- Create a new branch (`git checkout -b feature-branch`)
- Commit your changes (`git commit -m "Added new feature"`)
- Push to the branch (`git push origin feature-branch`)
- Create a pull request

## License
This project is licensed under the MIT License. See `LICENSE` for more details.

