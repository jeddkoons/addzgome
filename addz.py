from twython import Twython, TwythonError

app_key = ""
app_secret = ""
oauth_token = ""
oauth_token_secret = ""

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
