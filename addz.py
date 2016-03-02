from twython import Twython, TwythonError

app_key = "0s24wXPrr5Qe6enob5Xyn7VyZ"
app_secret = "jI0JY8RQMv7rylZnzdzIK6bLNcPGiPf8u4d7Fq0oz9PEAIdc92"
oauth_token = "704999209636864000-9kbaJ8hms0BdI0aF2vdA2JE24XXNOiv"
oauth_token_secret = "wjEqiZLI2ieu5b9ydWrNeiWKupJcrWxJ9n8jDYVvoUYpe"

naughty_words = [" -RT"]
good_words = ["vyvanse got me like", "adderall got me like"]
filter = " OR ".join(good_words)
blacklist = " -".join(naughty_words)
keywords = filter + blacklist

twitter = Twython(app_key, app_secret, oauth_token, oauth_token_secret)

search_results = twitter.search(q=keywords, count=10)
try:
    for tweet in search_results["statuses"]:
        try:
            twitter.retweet(id = tweet["id_str"])
        except TwythonError as e:
            print e
             time.sleep(7200)
except TwythonError as e:
    print e