from __future__ import absolute_import, print_function

from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import json

# Go to http://apps.twitter.com and create an app.
# The consumer key and secret will be generated for you after
consumer_key="jEU5IU9iPWlTd2Zupb9tNuExY"
consumer_secret="dDZspvAKBUbrpo7PiNPoBC8FB9B0XGkRacUGDgTuJKSMsTTCu0"

# After the step above, you will be redirected to your app's page.
# Create an access token under the the "Your access token" section

access_token="963178560436490242-e4zs5HPRhSftditvZUUSsb5NrfwzJVg"
access_token_secret="rSgTVfRtXdi8GX8TJPqTDAfQHvcXYD2YRuR0QnkpcyGrg"

class StdOutListener(StreamListener):
    """ A listener handles tweets that are received from the stream.
    This is a basic listener that just prints received tweets to stdout.
    """
    
    def on_data(self, data):
        try:
            with open('data10.json', 'a') as outfile:
                json.dump(data,outfile)
            with open('data20.json','a') as outputj:
                outputj.write(data)
            with open('tweetsdata.txt', 'a') as tweets:
                tweets.write(data)
                tweets.write('\n')
            outfile.close()
            tweets.close()
            outputj.close()
        except BaseException as e:
            print('problem collecting tweet',str(e))
        return True

    def on_error(self, status):
        print(status)

if __name__ == '__main__':
    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    stream = Stream(auth, l)
    stream.filter(track=['WalkingDead_AMC','BachelorABC','netflix','powertv','cw_dynasty','HouseofCards','Suits_USA','usa','got','PPLTVSeries','prisonbreak','GameOfThrones','ScorpionCBS','sherlock','benedictcumberbatch','SleepintheGardn','lucyhale','shaymitch','sashapieterse27','AshBenzo','Pizza Hut','RareDiseaseDay','TurnOffThePhoneWhen','WednesdayWisdom','COYS','FACup','911onFOX','Line_of_duty','EmpireFOX','SalvationCBS'])
