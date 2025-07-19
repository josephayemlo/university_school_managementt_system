# Exit on error
set -o errexit

# Install dependencies (already handled by Render normally, but just in case)
pip install -r requirements.txt

# Run Django management commands
python manage.py migrate
python manage.py collectstatic --noinput
