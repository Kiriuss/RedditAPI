Hey there! Here’s my Reddit API task submission for TheSoul Publishing!

What’s this:
- My Reddit script! It logs into Reddit, asks for a subreddit, grabs the 5 latest posts, shows their title/author/upvotes, and saves them to a file (reddit_posts.txt). It handles errors too—all with fun print messages!

What you need to run it (Dependencies):
- Python 3 (I used 3.10, but prolly works with others too).
- One extra thing I installed with pip:
  - praw: Makes Reddit stuff super easy. Install it with: pip install praw
- Plus a Reddit account and an app (you make it at reddit.com/prefs/apps, pick “script”).

How to run it (Walkthrough):
1. Get your Reddit keys:
   - Go to reddit.com/prefs/apps, log in, and click “create app” or “create another app.”
   - Pick “script,” name it whatever (I did “MyRedditScript”), and leave redirect URI as http://localhost:8080.
   - After you hit create, copy the client_id (it’s right under the app name) and client_secret (next to “secret”).
   - You’ll also need your Reddit username, password, and a user_agent.
   - Put all that in a file called config.ini like this:
     [REDDIT]
     client_id = your_client_id
     client_secret = your_client_secret
     username = your_reddit_username
     password = your_reddit_password
     user_agent = MyRedditScript by u/yourusername
   - Save it in the same folder as the script.

2. Run the script:
   - Open a terminal or wherever you run Python stuff (I use PyCharm’s terminal).
   - Run: python main.py
   - It’ll ask “Type the subreddit name here (like 'python' or 'test'): ”—type something like “test” or “python” and hit Enter.
   - Watch it print the 5 latest posts with titles, authors, and upvotes—it’ll also save them to reddit_posts.txt in the same folder!

What it does:
- Logs into Reddit with OAuth 2.0 (fancy login stuff!).
- Fetches the 5 newest posts from whatever subreddit you pick.
- Prints and saves each post’s title, author, and upvote count to reddit_posts.txt.
- If something messes up (like rate limits or login fails), it tells you and tries to fix it.

Sample output (my run with r/test):
Starting script and loading config...
Config loaded—fingers crossed!
Trying to log into Reddit...
Logged in as: KirilAngjelkos1
Type the subreddit name here (like 'python' or 'test'): test
Setting up a file to save the posts...
Fetching 5 latest posts from r/test...
Title: Testing 123
Author: SomeUser
Upvotes: 5
---
Title: Hi there
Author: AnotherUser
Upvotes: 2
---
[3 more posts...]
Got all 5 posts—yay!
Script’s all done and saved to reddit_posts.txt!

(And reddit_posts.txt has the same stuff—check it out!)

Let me know if you need help running it—I’m new to coding, but I’ll do my best to help!