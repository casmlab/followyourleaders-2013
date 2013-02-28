from django.http import HttpResponse
from django.template import loader
from django.template.context import Context
from django.core.context_processors import request
from django.db import connection, transaction
import json


def index(request):
    t = loader.get_template('index.html')
    c = Context({})
    return HttpResponse(t.render(c))
    pass

def faq(request):
    t = loader.get_template('faq.html')
    c = Context({})
    return HttpResponse(t.render(c))
    pass

def contact(request):
    t = loader.get_template('contact.html')
    c = Context({})
    return HttpResponse(t.render(c))
    pass

def about(request):
    t = loader.get_template('about.html')
    c = Context({})
    return HttpResponse(t.render(c))
    pass

def get_recent_tweet():
    cursor = connection.cursor()
    cursor.execute("SELECT tweet_text from tweets order by tweet_id  desc limit 1")
    row = cursor.fetchone()
    print "Row is: " +row
    return HttpResponse (json.dumps(row), mimetype="application/json")
    
def get_us_congress(request): 
    cursor = connection.cursor()
    cursor.execute("SELECT tweet_text from tweets order by tweet_id  desc limit 5")
    row = cursor.fetchall()
    print row

    t = loader.get_template('us-congress.html')
    c = Context({'row':row})
    return HttpResponse(t.render(c))
    pass

def get_latest_tweet(request):
    pass