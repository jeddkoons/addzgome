# Importing the module
from twython import Twython

#Setting these as variables will make them easier for future edits
app_key = "0s24wXPrr5Qe6enob5Xyn7VyZ"
app_secret = "jI0JY8RQMv7rylZnzdzIK6bLNcPGiPf8u4d7Fq0oz9PEAIdc92"
oauth_token = "704999209636864000-9kbaJ8hms0BdI0aF2vdA2JE24XXNOiv"
oauth_token_secret = "wjEqiZLI2ieu5b9ydWrNeiWKupJcrWxJ9n8jDYVvoUYpe"

#Prepare your twitter, you will need it for everything
twitter = Twython(app_key, app_secret, oauth_token, oauth_token_secret)
#The above should just be a single line, without the break

#The obligatory first status update to test
twitter.update_status(status="Hello world.")