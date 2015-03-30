# -*- coding: utf-8 -*-

from __future__ import unicode_literals
import json

from bottle import request, response, route, run
import twitter


api = twitter.Api(
        consumer_key="",
        consumer_secret="",
        access_token_key="",
        access_token_secret="")


@route("/")
def index():
    return {"message": "API Server Running"}


@route('/search')
def search():
    term = request.query.q
    if term == "":
        term = "#adf2015"

    tweets = api.GetSearch(
        term=term,
        result_type="recent",
        count=15)
    dict_tweets = map(lambda t: t.AsDict(), tweets)

    result = {
        "query": {
            "term": term
        },
        "results": dict_tweets
    }

    response.content_type = "application/json"

    return json.dumps(result, ensure_ascii=False)


if __name__ == "__main__":
    run(host='0.0.0.0', port=8000, reloader=True)
