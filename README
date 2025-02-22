# Social Media Database

## Overview

This project implements a **social media database** that allows users to create accounts, follow other users, post messages, like posts, and leave comments. It also provides functions to recommend users to follow, generate personalized feeds, and manage interactions.

## Database Schema

### **1. Users Table**

```sql
CREATE TABLE users (
    email              TEXT,
    first_name        TEXT NOT NULL,
    last_name         TEXT NOT NULL,
    PRIMARY KEY (email)
);
```

- Stores **user profile information**.
- `email` is the **primary key**.

### **2. Accounts Table**

```sql
CREATE TABLE accounts (
    username        TEXT,
    email           TEXT NOT NULL,
    PRIMARY KEY (username),
    FOREIGN KEY (email) REFERENCES users (email)
);
```

- Each user has an **account** with a unique `username`.
- Links to `users` via `email`.

### **3. Follows Table**

```sql
CREATE TABLE follows (
    follower        TEXT NOT NULL,
    followee        TEXT NOT NULL,
    PRIMARY KEY (follower, followee),
    FOREIGN KEY (follower) REFERENCES accounts (username),
    FOREIGN KEY (followee) REFERENCES accounts (username)
);
```

- Represents **who follows whom**.
- Uses a **composite primary key** (`follower`, `followee`).

### **4. Posts Table**

```sql
CREATE TABLE posts (
    id              INTEGER PRIMARY KEY AUTOINCREMENT,
    username        TEXT NOT NULL,
    message         TEXT NOT NULL,
    posted_at       DATETIME NOT NULL,
    FOREIGN KEY (username) REFERENCES accounts (username)
);
```

- Stores **posts made by users**.
- `id` is an **auto-incrementing primary key**.

### **5. Likes Table**

```sql
CREATE TABLE likes (
    username        TEXT NOT NULL,
    post_id         INTEGER NOT NULL,
    PRIMARY KEY (username, post_id),
    FOREIGN KEY (username) REFERENCES accounts (username),
    FOREIGN KEY (post_id) REFERENCES posts (id)
);
```

- Stores **which user liked which post**.
- Uses a **composite primary key** (`username`, `post_id`).

### **6. Comments Table**

```sql
CREATE TABLE comments (
    id              INTEGER PRIMARY KEY AUTOINCREMENT,
    post_id         INTEGER NOT NULL,
    username        TEXT NOT NULL,
    message         TEXT NOT NULL,
    posted_at       DATETIME NOT NULL,
    FOREIGN KEY (username) REFERENCES accounts (username),
    FOREIGN KEY (post_id) REFERENCES posts (id)
);
```

- Stores **comments on posts**.
- `id` is an **auto-incrementing primary key**.

## Functions and Queries

### **User & Account Management**

```python
def create_user(db, email, first_name, last_name):
    db.execute("INSERT INTO users (email, first_name, last_name) VALUES (?,?,?)", (email, first_name, last_name))

def add_account(db, username, email):
    db.execute("INSERT INTO accounts (username, email) VALUES (?,?)", (username, email))
```

- Adds users and their accounts.

### **Posts & Comments**

```python
def create_post(db, username, message, posted_at):
    db.execute("INSERT INTO posts (username, message, posted_at) VALUES (?,?,?)", (username, message, posted_at))

def create_comment(db, post_id, username, message, posted_at):
    db.execute("INSERT INTO comments (post_id, username, message, posted_at) VALUES (?,?,?,?)", (post_id, username, message, posted_at))
```

- Adds new posts and comments.

### **Likes & Follows**

```python
def create_like(db, username, post_id):
    db.execute("INSERT INTO likes (username, post_id) VALUES (?,?)", (username, post_id))

def create_follow(db, follower, followee):
    db.execute("INSERT INTO follows (follower, followee) VALUES (?,?)", (follower, followee))
```

- Allows users to **like posts** and **follow others**.

### **Fetching Data**

```python
def make_feed(db, username):
    query = """
    SELECT p1.username, p1.message, p1.posted_at
    FROM follows f1
    JOIN posts p1 ON f1.followee = p1.username
    WHERE f1.follower = ?
    ORDER BY p1.posted_at DESC;
    """
    result = db.execute(query, (username,))
    return result.fetchall()
```

- Generates a **personalized feed** based on followed users' posts.

### **Deleting Data**

```python
def delete_post(db, post_id):
    try:
        db.execute("DELETE FROM likes WHERE post_id = ?", (post_id,))
        db.execute("DELETE FROM comments WHERE post_id = ?", (post_id,))
        db.execute("DELETE FROM posts WHERE id = ?", (post_id,))
        db.commit()
        return True
    except Exception as e:
        print(f"Error deleting post: {e}")
        return False
```

- Deletes a post **along with its likes and comments**.

### **Unfollowing a User**

```python
def unfollow(db, follower, followee):
    try:
        db.execute("DELETE FROM follows WHERE follower = ? AND followee = ?", (follower, followee))
        db.commit()
        return True
    except Exception as e:
        print(f"Error when unfollowing: {e}")
        return False
```

- Allows users to **unfollow** others.

### **Updating Posts & Comments**

```python
def update_post(db, post_id, message):
    try:
        result = db.execute("UPDATE posts SET message = ? WHERE id = ?", (message, post_id))
        db.commit()
        return result.rowcount > 0
    except Exception as e:
        print(f"Error updating post: {e}")
        return False

def update_comment(db, comment_id, post_id, message):
    try:
        result = db.execute("UPDATE comments SET message = ? WHERE id = ? AND post_id = ?", (message, comment_id, post_id))
        db.commit()
        return result.rowcount > 0
    except Exception as e:
        print(f"Error updating comment: {e}")
        return False
```

- Updates **posts and comments** based on `id`.

### **Finding Recommended Users & Posts**

```python
def recommended_follow(db, username):
    query = """
    SELECT DISTINCT f2.followee
    FROM follows f1
    JOIN follows f2 ON f1.followee = f2.follower
    WHERE f1.follower = ?
    """
    return db.execute(query, (username,)).fetchall()
```

- Suggests **new people to follow** based on mutual connections.

---

## Summary

This **social media database** supports:
 User accounts & profiles
 Posting, commenting, and liking
 Following & unfollowing
 Generating personalized feeds
 Discovering recommended users & posts
 Full CRUD operations on posts & comments

 **Future Improvements:**

- Implementing **hashtags & search functionality**
- Adding **notifications for likes & follows**
- Optimizing queries for better performance

---

### **Author**

Developed by **Austin Espinoza and Aston Haycock**
