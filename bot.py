import praw
import re
import datetime

reddit = praw.Reddit(user_agent='AssBot v0.1',
                     client_id='client_id',
                     client_secret='client_secret',
                     username='username',
                     password='password')

subreddit = reddit.subreddit('all')

regex = re.compile('(\w+)-ass (\w+)?')

for submission in subreddit.stream.submissions():
    comments = submission.comments.list()
    for comment in comments:
        match = regex.match(comment.body)
        if match:
            comment.reply('What about a %s ass-%s?' % (match.group(1), match.group(2)))
