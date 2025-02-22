CREATE TABLE users (
    email              TEXT,
    first_name      TEXT NOT NULL,
    last_name       TEXT NOT NULL,

    PRIMARY KEY (email)
);

CREATE TABLE accounts (
    username        TEXT,
    email           TEXT NOT NULL,

    PRIMARY KEY (username),
    FOREIGN KEY (email) REFERENCES users (email)
);

CREATE TABLE follows (
    follower        TEXT NOT NULL,
    followee        TEXT NOT NULL,

    PRIMARY KEY (follower, followee),
    FOREIGN KEY (follower) REFERENCES accounts (username),
    FOREIGN KEY (followee) REFERENCES accounts (username)
);

CREATE TABLE posts (
    id              INTEGER PRIMARY KEY AUTOINCREMENT,
    username        TEXT NOT NULL,
    message         TEXT NOT NULL,
    posted_at       DATETIME NOT NULL,

    FOREIGN KEY (username) REFERENCES accounts (username)
);

CREATE TABLE likes (
    username        TEXT NOT NULL,
    post_id         INTEGER NOT NULL,

    PRIMARY KEY (username, post_id),
    FOREIGN KEY (username) REFERENCES accounts (username),
    FOREIGN KEY (post_id) REFERENCES posts (id)
);

CREATE TABLE comments (
    id      INTEGER PRIMARY KEY AUTOINCREMENT,
    post_id         INTEGER NOT NULL,
    username        TEXT NOT NULL,
    message         TEXT NOT NULL,
    posted_at       DATETIME NOT NULL,

    FOREIGN KEY (username) REFERENCES accounts (username),
    FOREIGN KEY (post_id) REFERENCES posts (id)
);




