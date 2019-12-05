import praw

# bot = praw.Reddit(user_agent='MySimpleBot v0.1',
#                   client_id='abcdefGHIJKLO123--',
#                   client_secret='12345678901abcdefgh-_',
#                   username='demo_user',
#                   password='demo_password')


bot.read_only = True
print(bot.auth.scopes())

subreddit = bot.subreddit("AbortionDebate")

submission = bot.submission(url='https://www.reddit.com/r/funny/comments/3g1jfi/buttons/')

# for top_level_comment in submission.comments:
#     try:
#         print(top_level_comment.body)
#     except AttributeError:
#         print('no body - first level')
#     for second_level_comment in submission.comments:
#         try:
#             print('\t', second_level_comment.body)
#         except AttributeError:
#             print('\tno body - second level')
#
submission.comments.replace_more(limit=None)
comment_queue = submission.comments[:]  # Seed with top-level
for comment in comment_queue:
    print(comment.body)
    for replies in comment.replies:
        print('\t', replies.body)

#
# submission.comments.replace_more(limit=None)
# for comment in submission.comments.list():
#     print(comment.body)

# comments = subreddit.stream.comments()
#
# #comments = subreddit.get_comments(limit=None)
#
# for comment in comments:
#     text = comment.body # Fetch body
#     author = comment.author # Fetch author
#     if 'man' in text.lower():
#         # Generate a message
#         message = "Message - /{1}, u/{0} ?".format(author, len(text))
#
#         print(message) # Send message