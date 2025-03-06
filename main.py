import praw
import configparser
import time

# starting up and grabbing my config stuff
print("Starting script and loading config...")
config = configparser.ConfigParser()
config.read('config.ini')

# pulling out my reddit keys and stuff
client_id = config['REDDIT']['client_id']
client_secret = config['REDDIT']['client_secret']
username = config['REDDIT']['username']
password = config['REDDIT']['password']
user_agent = config['REDDIT']['user_agent']
print("Config loaded—fingers crossed!")  # hope i got this right

# logging into reddit with all my info
print("Trying to log into Reddit...")
reddit = praw.Reddit(
    client_id=client_id,
    client_secret=client_secret,
    username=username,
    password=password,
    user_agent=user_agent
)
print(f"Logged in as: {reddit.user.me()}")  # cool, it shows my username!

# asking which subreddit to check
subreddit_name = input("Type the subreddit name here (like 'python' or 'test'): ")

# opening a file to save the posts
print("Setting up a file to save the posts...")
file = open("reddit_posts.txt", "w")  # making a new file, 'w' means write

# getting the 5 latest posts
print(f"Fetching 5 latest posts from r/{subreddit_name}...")
try:
    subreddit = reddit.subreddit(subreddit_name)  # picking the subreddit
    posts = subreddit.new(limit=5)  # grabbing just 5 new ones

    # showing each post and writing it to the file
    for post in posts:
        print(f"Title: {post.title}")
        print(f"Author: {post.author}")
        print(f"Upvotes: {post.score}")
        print("---")  # little line to keep it neat
        # writing to the file, \n means new line
        file.write(f"Title: {post.title}\n")
        file.write(f"Author: {post.author}\n")
        file.write(f"Upvotes: {post.score}\n")
        file.write("---\n")
    print("Got all 5 posts—yay!")  # woohoo it worked!
    file.write("Got all 5 posts—yay!\n")  # adding this to the file too

except praw.exceptions.PRAWException as e:
    print(f"Oops, Reddit didn’t like that: {e}")  # something went wrong
    file.write(f"Oops, Reddit didn’t like that: {e}\n")  # saving the error
    if "RATELIMIT" in str(e):
        print("Too many requests—rate limit hit!")  # ugh, too fast
        file.write("Too many requests—rate limit hit!\n")
        wait_time = 60  # waiting a minute, just guessing
        print(f"Chilling for {wait_time} seconds...")
        file.write(f"Chilling for {wait_time} seconds...\n")
        time.sleep(wait_time)
        print("Trying again...")
        file.write("Trying again...\n")
        posts = subreddit.new(limit=5)  # retrying
        for post in posts:
            print(f"Title: {post.title}")
            print(f"Author: {post.author}")
            print(f"Upvotes: {post.score}")
            print("---")
            file.write(f"Title: {post.title}\n")
            file.write(f"Author: {post.author}\n")
            file.write(f"Upvotes: {post.score}\n")
            file.write("---\n")
        print("Got em after waiting—phew!")
        file.write("Got em after waiting—phew!\n")
except Exception as e:
    print(f"Something weird broke: {e}")  # no idea what happened
    file.write(f"Something weird broke: {e}\n")  # saving this too

# closing the file so it saves
file.close()
print("Script’s all done and saved to reddit_posts.txt!")  # finished, hope it’s good!