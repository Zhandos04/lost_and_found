def generate_readme():
    return """# Lost and Found Web Application

## Setup Instructions

### Prerequisites
- Python 3.11+
- SQLite
- Django
- Git

### Installation
1. Clone the repository:
   ```sh
   git clone <repo_url>
   cd lost_and_found
   ```
2. Create and activate a virtual environment:
   ```sh
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```
3. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```
4. Apply migrations:
   ```sh
   python manage.py migrate
   ```
5. Create a superuser:
   ```sh
   python manage.py createsuperuser
   ```
6. Start the development server:
   ```sh
   python manage.py runserver
   ```

### Workflow
- Development is done in the `dev` branch.
- Code is reviewed before merging into `main`.
- Pull requests must be approved before merging.
- On presentation, if an issue is found, the reviewer loses 10% of their grade.
- If the project passes without issues, the reviewer gains 10%.

### Testing
Run tests with:
```sh
python manage.py test
```"""

readme_content = generate_readme()
with open('README.md', 'w') as readme_file:
    readme_file.write(readme_content)
