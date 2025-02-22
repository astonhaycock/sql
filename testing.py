import sqlite3
from queries import *
from datetime import datetime
from read_all import *
from tabulate import tabulate
import os

db = sqlite3.connect('social.db')

def pretty_print(data, column_names):
    print(tabulate(data, headers=column_names, tablefmt="fancy_grid"))


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
  print('12. Feed')
  print('13. Print All')
  print('14. Recommended Follow')
  print('15. Recommended Post')
  print('16. Exit')
  print('\n')
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
    data,column_name = create_post(db, username, message, posted_at)
    print('\nPost created successfully')
    pretty_print(data, column_name)

    

  if(choice == 4):
    post_id = input('Enter post id: ')
    delete_post(db, post_id)

  if(choice == 5):
    post_id = input('Enter post id: ')
    username = input('Enter username: ')
    message = input('Enter message: ')
    posted_at = datetime.now()
    create_comment(db, post_id, username, message, posted_at)

  if(choice == 6):
    post_id = input('Enter post id: ')
    comment_id = input('Enter comment id: ')
    message = input('Enter message: ')
    update_comment(db, post_id, message, comment_id)

  if(choice == 7):
    username = input('Enter username: ')
    post_id = input('Enter post id: ')
    create_like(db, username, post_id)

  if(choice == 8):
    username = input('Enter username: ')
    post_id = input('Enter post id: ')
    delete_like(db, username, post_id)

  if(choice == 9):
    follower = input('Enter follower: ')
    followee = input('Enter followee: ')
    create_follow(db, follower, followee)

  if(choice == 10):
    follower = input('Enter follower: ')
    followee = input('Enter followee: ')
    unfollow(db, follower, followee)

  if choice == 11:
    post_id = input('Enter post id: ')
    message = input('Enter message: ')
    update_post(db, post_id, message)

  if choice == 12:
    
    data,column_name = make_feed(db, input('Enter username: '))
    pretty_print(data, column_name)

  if choice == 13:
    get_all(db, ['accounts', 'users', 'posts', 'comments', 'likes', 'follows'])

  if choice == 14:
    data,column_name = recommended_follow(db, input('Enter username: '))
    pretty_print(data, column_name)

  if choice == 15:
    data,column_name = recommended_post(db, input('Enter username: '))
    pretty_print(data, column_name)
  
  if choice == 16:
    break

  