import praw
import re
import datetime

reddit = praw.Reddit(user_agent='AssBot v0.1',
                     client_id='client_id',
                     client_secret='client_secret',
                     username='username',
                     password='password')

subreddit = reddit.subreddit('all')

comments = subreddit.stream.comments()

regex = re.compile('(\w+)-ass (\w+)?')

for comment in comments:
    text = comment.body
    match = regex.match(text)
    if match:
        print({datetime.datetime.now().isoformat()})
        print('match found: ')
        print(match.group())
        print('{match.group(1) ass-{match.group(2)}}')
