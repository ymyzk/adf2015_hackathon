# -*- coding: utf-8 -*-

from __future__ import unicode_literals
import json

from bottle import response, route, run
import twitter


api = twitter.Api(consumer_key="uQ644CuFtyY1L9Q4eGQbFNx5B",
        consumer_secret="sCkTpWUZ42myubNOjJLaAs1lkIGWym4rg5rqqFZFBVU1d7i5GE",
        access_token_key="2338692848-nhxkktgVNGZycQhfdobwmMeceaCeJerwb4KhcIF",
        access_token_secret="S5j63eT3eiUaVsv9WezxdTzaDa3hVf6CRQEDnoQqyhMef")


@route('/search')
def search():
    term = "adf2015"
    tweets = map(lambda t: t.AsDict(), api.GetSearch(term=term))
    return tweets


run(host='0.0.0.0', port=8081, reloader=True)
