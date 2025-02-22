import sqlite3
from queries import *
from datetime import datetime
from read_all import *
from tabulate import tabulate
import os

db = sqlite3.connect('social.db')

def Options():
  print('\n')
  print('1. Create User')
  print('2. Create Account')
  print('3. Post')
  print('4. Delete Post')
  print('5. comment')
  print('6. update comment')
  print('7. Like')
  print('8. dislike')
  print('9. Follow')
  print('10. Unfollow')
  print('11. update post')
  print('12. Quit')
  return input('Enter your choice: ')



while True:
  choice = int(Options())


  if(choice == 1):
    email = input('Enter email: ')
    first_name = input('Enter first name: ')
    last_name = input('Enter last name: ')
    create_user(db, email, first_name, last_name)
  
  if(choice == 2):
    username = input('Enter username: ')
    email = input('Enter email: ')
    add_account(db, username, email)
  
  if(choice == 3):
    username = input('Enter username: ')
    message = input('Enter message: ')
    posted_at = datetime.now()
    create_post(db, username, message, posted_at)

  if(choice == 4):
    pass
    post_id = input('Enter post id: ')
    # delete_post(db, post_id)  

  if(choice == 5):
    post_id = input('Enter post id: ')
    username = input('Enter username: ')
    message = input('Enter message: ')
    posted_at = datetime.now()
    create_comment(db, post_id, username, message, posted_at)

  if(choice == 6):
    pass
    # comment_id = input('Enter comment id: ')
    # delete_comment(db, comment_id)

  if(choice == 7):
    username = input('Enter username: ')
    post_id = input('Enter post id: ')
    create_like(db, username, post_id)

  if(choice == 8):
    pass
    # username = input('Enter username: ')
    # post_id = input('Enter post id: ')
    # delete_like(db, username, post_id)

  if(choice == 9):
    follower = input('Enter follower: ')
    followee = input('Enter followee: ')
    create_follow(db, follower, followee)

  if(choice == 10):
    pass
    # follower = input('Enter follower: ')
    # followee = input('Enter followee: ')
    # delete_follow(db, follower, followee)

  if choice == 11:
    post_id = input('Enter post id: ')
    message = input('Enter message: ')
    update_post(db, post_id, message)

  if choice == 12:
    break