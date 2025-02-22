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
    

def get_all(db, tables):
        for table in tables:
            res = db.execute(f"Select * From {table}")
            data = res.fetchall()
            column_names = [description[0] for description in res.description]
            print(tabulate(data, headers=column_names, tablefmt="fancy_grid"))

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
    

def recommended_follow(db, username):
    query = """
    SELECT DISTINCT f2.followee
    FROM follows f1
    JOIN follows f2 ON f1.followee = f2.follower
    WHERE f1.follower = ?
    AND f2.followee NOT IN (
        SELECT followee 
        FROM follows 
        WHERE follower = ?
    )
    AND f2.followee != ?
    """
    res = db.execute(query, (username, username, username))
    column_names = [description[0] for description in res.description]
    return res.fetchall(), column_names

def recommended_post(db, username):
    query = """
    SELECT * 
    FROM posts 
    WHERE (username IN (
        SELECT DISTINCT f2.followee
        FROM follows f1
        JOIN follows f2 ON f1.followee = f2.follower
        WHERE f1.follower = ?
        AND f2.followee NOT IN (
        SELECT followee 
        FROM follows 
        WHERE follower = ?
        )
        AND f2.followee != ?
    )
    OR username IN (
        SELECT followee
        FROM follows
        WHERE follower = ?
    ))
    AND id NOT IN (
        SELECT post_id
        FROM likes
        WHERE username = ?
    )
    """
    res = db.execute(query, (username, username, username, username, username))
    column_names = [description[0] for description in res.description]
    return res.fetchall(), column_names