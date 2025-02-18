import sqlite3
from queries import *
from datetime import datetime

def main():
    db = sqlite3.connect('social.db')
    with db:
        setup_database(db)

def setup_database(db):
    # Create sample users
    create_user(db, "sally@email.com", "Sally", "Smith")
    create_user(db, "john@email.com", "John", "Doe")
    
    # Create accounts
    add_account(db, "sally123", "sally@email.com")
    add_account(db, "johndoe", "john@email.com")
    
    # Create some posts
    create_post(db, 1, "Hello world!", datetime.now().isoformat())
    create_post(db, 2, "My first post!", datetime.now().isoformat())
    
    # Create comments
    create_comment(db, 2, 1, "Welcome!", datetime.now().isoformat())
    
    # Create likes
    create_like(db, 2, 1)  # John likes Sally's post
    
    # Create followers
    create_follow(db, 2, 1)  # John follows Sally

if __name__ == "__main__":
    main()
