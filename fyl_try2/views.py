from django.http import HttpResponse
from django.template import loader
from django.core.mail import send_mail
from django.template.context import Context
from django.core.context_processors import request
from django.db import connection, transaction
from fyl_try2.forms import ContactForm
from django.http import HttpResponseRedirect
from django.shortcuts import render
import json


def index(request):
    cursor = connection.cursor()
    cursor.execute("SELECT tweet_text from tweets order by tweet_id  desc limit 5")
    row = cursor.fetchall()
    print row
    
    t = loader.get_template('index.html')
    c = Context({'row':row})
#    c = Context({})
    return HttpResponse(t.render(c))
    pass

def faq(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            send_mail(
                cd['name'],
                cd['message'],
                cd.get('email', 'noreply@fyl_faq.com'),
                ['info@followyourleaders.org'],
            )
            return HttpResponseRedirect('/faq')
    else:
        form = ContactForm() # An unbound form
        
    t = loader.get_template('faq.html')
    c = Context({'form': form,})
    return HttpResponse(t.render(c))
    pass

# ----  Not Implemented
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
    query='''
        SELECT created_at,name,tweet_text,image_url,screen_name,tweet_url FROM 
        (SELECT * from TwitterCollector_113thCongress.tweets order by tweet_id  desc limit 300) as tweets,
        TwitterCollector_113thCongress.user_info as user_info
        where 
        tweets.user_id= user_info.user_id
        and  user_info.user_id in (Select user_id from user_list )
        group by name
        order by tweet_id  desc limit 300;'''
    cursor.execute(query)
    #cursor.execute("SELECT tweet_text from tweets order by tweet_id  desc limit 5")
    row = cursor.fetchall()
    print type( row)

    t = loader.get_template('us-congress.html')
    c = Context({'row':row})
    return HttpResponse(t.render(c))



def get_latest_tweet(request):
    pass