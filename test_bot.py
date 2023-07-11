from instagrapi import Client
import pandas as pd
import numpy as np
import matplotlib as mp
import time
import pprint

cl = Client()
cl.login("username", "password")

find_value = 20

while True:
    # List of Hashtags To Fetch
    hashtag_list = ["barbie", "oppenheimer", "bariemovie", "barbiepink", "pinkbarbie", "oppenheimermovie"]

    for hashtag in hashtag_list:
        # Finding Top Hashtags Based on "find_value"
        top_posts = cl.hashtag_medias_top(hashtag, find_value)

        for i in range(0, len(top_posts)):
            # Fetching the CSV File Used to store the Post Links
            commented_posts = pd.read_csv('Commented_List.csv')

            # Itertating through the Results
            first_comment = top_posts[i].dict()

            post_id = first_comment['id']
            pprint.pprint(post_id)

            post_code = first_comment['code']
            pprint.pprint(post_code)

            post_url = "https://instagram.com/reel/" + post_code
            print(post_url)

            # Checking if Already Commented on the Post
            is_present = post_id in commented_posts['post_id'].values

            if  is_present == False:
                print("New Post Found, Commenting..... \n")
                # Using try and except beacuse certain posts have comment limit
                try:
                    comment = cl.media_comment(post_id, "Your comment goes here")
                except Exception as error:
                    print(error)

                # Storing the Values in Commented_List.csv File
                values = [hashtag, post_id, post_code, post_url]
                print(values)

                commented_posts.loc[len(commented_posts)] = values

                commented_posts.to_csv("Commented_List.csv", index=False, encoding='utf-8')
            else:
                print("Post Already Found \n")

    # Increase the time inorder to not get temporary ban
    print("Checking For New Posts in 5 Seconds....")
    time.sleep(5)



