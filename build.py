import sqlite3
from queries import *
from datetime import datetime
from read_all import *
from tabulate import tabulate
import os
def main():
    os.system('rm -f social.db')
    os.system('sqlite3 social.db < schema.sql')

    db = sqlite3.connect('social.db')
    with db:
        setup_database(db)

def setup_database(db):
    lis = ["users", "accounts", "follows", "posts", "likes", "comments"]
    get_all(db, lis)

    users = [
        ("dave@email.com", "Dave", "Martin"),
        ("emma@email.com", "Emma", "Clark"),
        ("frank@email.com", "Frank", "Harris"),
        ("grace@email.com", "Grace", "Walker"),
        ("henry@email.com", "Henry", "Lopez"),
        ("ivy@email.com", "Ivy", "Taylor"),
        ("jack@email.com", "Jack", "Miller"),
        ("karen@email.com", "Karen", "Wilson"),
        ("luke@email.com", "Luke", "Davis"),
        ("mona@email.com", "Mona", "Smith")
    ]
    
    for email, first_name, last_name in users:
        create_user(db, email, first_name, last_name)
    
    # Create accounts with distinct usernames
    accounts = [
        ("dave987", "dave@email.com"),
        ("emma456", "emma@email.com"),
        ("frank123", "frank@email.com"),
        ("grace789", "grace@email.com"),
        ("henry654", "henry@email.com"),
        ("ivy101", "ivy@email.com"),
        ("jack007", "jack@email.com"),
        ("karen202", "karen@email.com"),
        ("luke333", "luke@email.com"),
        ("mona444", "mona@email.com"),
    ]
    
    for username, email in accounts:
        add_account(db, username, email)
    
    # Create a large number of posts
    posts = [
        ("dave987", "Feeling great today! Dave here."),
        ("emma456", "Excited to start this new journey!"),
        ("frank123", "Just got back from a workout. Feeling strong!"),
        ("grace789", "Can't wait for the weekend!"),
        ("henry654", "Henry checking in. All is well!"),
        ("ivy101", "Exploring the city today, it's a beautiful day!"),
        ("jack007", "Just finished reading an interesting book!"),
        ("karen202", "Had an amazing lunch at a new place."),
        ("luke333", "Busy day at work, but feeling productive."),
        ("mona444", "Looking forward to the weekend getaway.")
    ]
    
    for username, message in posts:
        create_post(db, username, message, datetime.now().isoformat())
    
    # Get post IDs
    posts = db.execute("SELECT * FROM posts").fetchall()
    
    # Create comments (make sure they're unique)
    comments = [
        (posts[0][0], "frank123", "Nice post, Dave!"),
        (posts[1][0], "grace789", "I can relate, Emma!"),
        (posts[2][0], "ivy101", "Great job, Frank!"),
        (posts[3][0], "henry654", "Weekend vibes, Grace!"),
        (posts[4][0], "jack007", "Keep it up, Henry!"),
        (posts[5][0], "karen202", "Love your energy, Ivy!"),
        (posts[6][0], "luke333", "Interesting book, Jack!"),
        (posts[7][0], "mona444", "Lunch sounds amazing, Karen!"),
        (posts[8][0], "dave987", "Productivity is key, Luke!"),
        (posts[9][0], "emma456", "Weekend getaway sounds fun, Mona!")
    ]
    
    for post_id, username, message in comments:
        create_comment(db, post_id, username, message, datetime.now().isoformat())
    
    # Create likes (distinct users liking posts)
    likes = [
        ("frank123", posts[0][0]),
        ("frank123", posts[3][0]),
        ("grace789", posts[1][0]),
        ("ivy101", posts[2][0]),
        ("jack007", posts[3][0]),
        ("henry654", posts[4][0]),
        ("karen202", posts[5][0]),
        ("luke333", posts[6][0]),
        ("mona444", posts[7][0]),
        ("dave987", posts[8][0]),
        ("emma456", posts[9][0])

    ]
    
    for username, post_id in likes:
        create_like(db, username, post_id)
    
    # Create follows (distinct user follow relationships)
    follows = [
        ("frank123", "dave987"),
        ("grace789", "emma456"),
        ("ivy101", "frank123"),
        ("jack007", "grace789"),
        ("henry654", "ivy101"),
        ("karen202", "jack007"),
        ("luke333", "henry654"),
        ("mona444", "karen202"),
        ("dave987", "luke333"),
        ("emma456", "mona444"),
        ("frank123", "grace789"),
        ("grace789", "ivy101"),
        ("ivy101", "jack007"),
        ("jack007", "henry654"),
        ("henry654", "karen202"),
        ("karen202", "luke333"),
        ("luke333", "mona444"),
        ("mona444", "dave987"),
        ("dave987", "emma456")
    ]
    
    for follower, followee in follows:
        create_follow(db, follower, followee)




db = sqlite3.connect('social.db')

def pretty_print(data, column_names):
    print(tabulate(data, headers=column_names, tablefmt="fancy_grid"))

data,column_name = recommended_post(db, "frank123")

pretty_print(data, column_name)


if __name__ == "__main__":
    # main()
    pass
