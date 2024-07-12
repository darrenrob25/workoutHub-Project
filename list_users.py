# list_users.py

from workouthub import app, db
from workouthub.models import User  # Import the User model, not Users

# Initialize the Flask app context
with app.app_context():
    # Fetch all users from the database
    users = User.query.all()
    
    # Check if there are users and print them
    if users:
        print(f"{'Username':<20} {'ID':<5}")
        print("-" * 25)
        for user in users:
            print(f"{user.username:<20} {user.id:<5}")
    else:
        print("No users found")