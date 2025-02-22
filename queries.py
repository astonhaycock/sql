def add_account(db, username, email):
    existing_user = db.execute("SELECT 1 FROM users WHERE email = ?", (email,)).fetchone()
    if not existing_user:
        print("No user found with that email, cannot create account.")
        return
    db.execute("INSERT INTO accounts (username, email) VALUES (?,?)", (username, email))
    db.commit()
    print("account created successfully")

def create_user(db, email, first_name, last_name):
    db.execute("INSERT INTO users (email, first_name, last_name) VALUES (?,?,?)", 
              (email, first_name, last_name))
    db.commit()

def delete_like(db, username, post_id):
    db.execute("DELETE FROM likes WHERE username = ? AND post_id = ?", (username, post_id))
    db.commit()
    

def get_all(db, tables):
        for table in tables:
            res = db.execute(f"Select * From {table}")
            data = res.fetchall()
            column_names = [description[0] for description in res.description]
            print(tabulate(data, headers=column_names, tablefmt="fancy_grid"))


    
def create_post(db, username, message, posted_at):
    cursor = db.execute(
        "INSERT INTO posts (username, message, posted_at) VALUES (?,?,?)",
        (username, message, posted_at)
    )
    new_post_id = cursor.lastrowid
    db.commit()

    post = db.execute(
        "SELECT * FROM posts WHERE id = ?",
        (new_post_id,)
    )
    return (post, [description[0] for description in post.description])



def create_comment(db, post_id, username, message, posted_at):
    cursor = db.execute("INSERT INTO comments (post_id, username, message, posted_at) VALUES (?,?,?,?)",
                (post_id, username, message, posted_at))
    
    new_post_id = cursor.lastrowid
    db.commit()
    print(new_post_id)

def create_like(db, username, post_id):
    db.execute("INSERT INTO likes (username, post_id) VALUES (?,?)",
                (username, post_id))
    db.commit()
    

    
def create_follow(db, follower, followee):
    db.execute("INSERT INTO follows (follower, followee) VALUES (?,?)",
                (follower, followee))
    db.commit()

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

def make_feed(db, username):
    query = """
    SELECT  p1.username, p1.message, p1.posted_at
    FROM follows f1
    JOIN posts p1 ON f1.followee = p1.username
    WHERE f1.follower = ?
    ORDER BY p1.posted_at DESC;
    """
    result = db.execute(query, (username,))
    column_name = [description[0] for description in result.description]
    return result.fetchall(),  column_name

def delete_post(db,post_id):
    try:
        db.execute("DELETE FROM likes WHERE post_id = ?", (post_id,))

        db.execute("DELETE FROM comments WHERE post_id = ?", (post_id,))

        db.execute("DELETE FROM posts WHERE id = ?", (post_id,))

        db.commit()
        return True
    
    except Exception as e :
        print(f"Error during deleting post: {e}")
        return False

def unfollow(db, follower, followee):
    try:
        db.execute("DELETE FROM follows WHERE follower = ? AND followee = ?", (follower, followee))
        db.commit()
        return True
    except Exception as e :
        print(f"Error when unfollowing: {e}")
        return False


def update_post(db, post_id, message):
    try:
        result = db.execute(
            "UPDATE posts SET message = ? WHERE id = ?", 
            (message, post_id)
        )
        db.commit()  
        
        if result.rowcount == 0: 
            print("No post found with that ID.")
            return False
        
        return True  
    except Exception as e:
        print(f"Error updating post: {e}")
        return False

def update_comment(db, post_id, message,comment_id):
    try:
        result = db.execute("UPDATE comments SET message = ? WHERE id = ? AND post_id = ?", (message,comment_id, post_id,))
        db.commit()

        if result.rowcount == 0:
            print("No comment found with that id")
            return False
        
        return True
    except Exception as e :
        print(f"Error updating comment {e}")
        return False