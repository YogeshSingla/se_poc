__author__ = 'the-kid89, kirito'
"""
A sample program for with hardcoded quiz questions and answers
that are parsed using intent tones based on given samples into
positive, negative and neutral.
"""

import json
import sys
from adapt.entity_tagger import EntityTagger
from adapt.tools.text.tokenizer import EnglishTokenizer
from adapt.tools.text.trie import Trie
from adapt.intent import IntentBuilder
from adapt.parser import Parser
from adapt.engine import DomainIntentDeterminationEngine


tokenizer = EnglishTokenizer()
trie = Trie()
tagger = EntityTagger(trie, tokenizer)
parser = Parser(tokenizer, tagger)

engine = DomainIntentDeterminationEngine()

# engine.register_domain('Domain1')
# engine.register_domain('Domain2')
#
# # define vocabulary
# weather_keyword = [
#     "weather"
# ]
#
# for wk in weather_keyword:
#     engine.register_entity(wk, "WeatherKeyword", domain='Domain1')
#
# weather_types = [
#     "snow",
#     "rain",
#     "wind",
#     "sleet",
#     "sun"
# ]
#
# for wt in weather_types:
#     engine.register_entity(wt, "WeatherType", domain='Domain1')
#
# locations = [
#     "Seattle",
#     "San Francisco",
#     "Tokyo"
# ]
#
# for l in locations:
#     engine.register_entity(l, "Location", domain='Domain1')
#
# # structure intent
# weather_intent = IntentBuilder("WeatherIntent")\
#     .require("WeatherKeyword")\
#     .optionally("WeatherType")\
#     .require("Location")\
#     .build()
#
#
# # define music vocabulary
# artists = [
#     "third eye blind",
#     "the who",
#     "the clash",
#     "john mayer",
#     "kings of leon",
#     "adelle"
# ]
#
# for a in artists:
#     engine.register_entity(a, "Artist", domain='Domain2')
#
# music_verbs = [
#     "listen",
#     "hear",
#     "play"
# ]
#
# for mv in music_verbs:
#     engine.register_entity(mv, "MusicVerb", domain='Domain2')
#
# music_keywords = [
#     "songs",
#     "music"
# ]
#
# for mk in music_keywords:
#     engine.register_entity(mk, "MusicKeyword", domain='Domain2')
#
# music_intent = IntentBuilder("MusicIntent")\
#     .require("MusicVerb")\
#     .optionally("MusicKeyword")\
#     .optionally("Artist")\
#     .build()
#
# engine.register_intent_parser(weather_intent, domain='Domain1')
# engine.register_intent_parser(music_intent, domain='Domain2')
#
#
# #create a default reply
# engine.register_domain('DefaultDomain')
# default_reply = [ "I do not understand", "Sorry! I didn't get that", "I think I am not programmed for that yet", "Still in beta"]
# for sample in default_reply:
#     engine.register_entity(sample,"DefaultReply", domain='DefaultDomain')
# default_intent = IntentBuilder("DefaultIntent").require("MusicVerb").build()
# engine.register_intent_parser(default_intent, domain='DefaultDomain')

#positive reply intent
positive_reply = [
    "yes",
    "very often",
    "many",
    "yeah",
    "ya",
    "often"
]
for sample in positive_reply:
    engine.register_entity(sample,"PositiveReplySamples")
positive_intent = IntentBuilder("PositiveIntent").require("PositiveReplySamples").build()
engine.register_intent_parser(positive_intent)


#negative reply intent
negative_reply = [
    "no",
    "hardly",
    "never",
    "don't recall",
    "dont recall",
    "rarely",
    "seldom",
    "not often",
    "few",
    "very few",
    "nah",
    "na",
    "nope"
]
for sample in negative_reply:
    engine.register_entity(sample,"NegativeReplySamples")
negative_intent = IntentBuilder("NegativeIntent").require("NegativeReplySamples").build()
engine.register_intent_parser(negative_intent)


#neutral reply intent
neutral_reply = [
    "sometimes",
    "a few",
    "probably",
    "maybe",
    "ok"
]
for sample in neutral_reply:
    engine.register_entity(sample,"NeutralReplySamples")
neutral_intent = IntentBuilder("NeutralIntent").require("NeutralReplySamples").build()
engine.register_intent_parser(neutral_intent)

time_span = [
    "minutes",
    "hours",
    "days",
    "weeks",
    "months",
    "years"
]
engine.register_regex_entity("(?P<frequency>[0-9]+)")
for sample in time_span:
    engine.register_entity(sample,"TimeSpan")
quantitative_intent = IntentBuilder("QuantitativeIntent").require("frequency").optionally("TimeSpan").build()
engine.register_intent_parser(quantitative_intent)

#questions
quiz_questions = [
    "Do you find work interesting and challenging?",
    "Do you look forward to coming to work everyday?",
    "Do you have friends in office?",
    "How frequently do you think about leaving your current job?",
    "Did you learn something in the last 5 days?",
    "How frequently did you get opportunity to do something different (through a new role or a new assignment within the same role) ?",
    "Were your goals set in the beginning of the year?",
    "How frequently do you visit the learning portal?"
]

if __name__ == "__main__":

    #for intents in engine.determine_intent(' '.join(sys.argv[1:])):
    #    print(intents)
    score = 0
    for question in quiz_questions:
        answer = str(raw_input(question))
        for intent in engine.determine_intent(answer):
            print(intent)
            if(intent.get('intent_type') == 'PositiveIntent'):
                score = score + 5
            elif(intent.get('intent_type') == 'NeutralIntent'):
                score = score + 3
            elif(intent.get('intent_type') == 'NegativeIntent'):
                score = score + 1
            #added for ease of teseting. Ideally score NOT to be printed during the quiz.
            print("[DEBUG] score: ",score)
    if(score>30):
        risk_level = "low"
    elif(score>15):
        risk_level = "moderate"
    else:
        risk_level = "high"
    print("Risk: " + risk_level)
