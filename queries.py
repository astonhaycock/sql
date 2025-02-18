def add_account(db, username, email):
    db.execute("INSERT INTO accounts (username, email) VALUES (?,?)", (username, email))

def create_user(db, email, first_name, last_name):
    db.execute("INSERT INTO users (email, first_name, last_name) VALUES (?,?,?)", 
              (email, first_name, last_name))

def create_post(db, username, message, posted_at):
    db.execute("INSERT INTO posts (username, message, posted_at) VALUES (?,?,?)",
              (username, message, posted_at))

def create_comment(db, post_id, username, message, posted_at):
    db.execute("INSERT INTO comments (post_id, username, message, posted_at) VALUES (?,?,?,?)",
              (post_id, username, message, posted_at))

def create_like(db, username, post_id):
    db.execute("INSERT INTO likes (username, post_id) VALUES (?,?)",
              (username, post_id))

def create_follow(db, follower, followee):
    db.execute("INSERT INTO follows (follower, followee) VALUES (?,?)",
              (follower, followee))