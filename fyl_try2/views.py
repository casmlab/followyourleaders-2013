from django.http import HttpResponse
from django.template import loader
from django.core.mail import send_mail
from django.template.context import Context
from django.core.context_processors import request
from django.db import connection, transaction
from fyl_try2.forms import ContactForm
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.core.serializers.json import DjangoJSONEncoder
import json



def index(request):
    return get_us_congress(request)
#    cursor = connection.cursor()
#    cursor.execute("SELECT tweet_text from tweets order by tweet_id  desc limit 5")
#    row = cursor.fetchall()
#    print row
#    
#    t = loader.get_template('index.html')
#    c = Context({'row':row})
##    c = Context({})
#    return HttpResponse(t.render(c))
#    pass

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
        SELECT created_at,name,tweet_text,image_url,screen_name,tweet_url,location, geo_lat, geo_long  FROM 
        (SELECT * from TwitterCollector_113thCongress.tweets order by tweet_id  desc limit 500) as tweets,
        TwitterCollector_113thCongress.user_info as user_info
        where 
        tweets.user_id= user_info.user_id
        and  user_info.user_id in (Select user_id from user_list )
        group by name
        order by tweet_id  desc limit 500;'''
    cursor.execute(query)
    #cursor.execute("SELECT tweet_text from tweets order by tweet_id  desc limit 5")
    row = cursor.fetchall()

    t = loader.get_template('us-congress.html')
    c = Context({'row':row,})
    return HttpResponse(t.render(c))

def us_congress_pltcl_map(request):
    cursor = connection.cursor()
    query='''
        SELECT created_at,name,tweet_text,image_url,screen_name,tweet_url,location, geo_lat, geo_long  FROM 
        (SELECT * from TwitterCollector_113thCongress.tweets order by tweet_id  desc limit 500) as tweets,
        TwitterCollector_113thCongress.user_info as user_info
        where 
        tweets.user_id= user_info.user_id
        and tweets.geo_lat != 0
        group by name
        order by tweet_id  desc limit 500;'''
    cursor.execute(query)
    congressTweets = cursor.fetchall()
    congressTArray = list(congressTweets) #convert to Array from tuple
    for i in range(0,len(congressTArray)):
        congressTArray[i]=list(congressTArray[i])
        congressTArray[i][0]=str(congressTArray[i][0]) #date time format fixes
    congressArray = json.dumps(congressTArray, cls=DjangoJSONEncoder);
    print congressArray
#    print type( congressTweets)

    t = loader.get_template('political-map.html')
    c = Context({'congressArray':congressArray,})
    return HttpResponse(t.render(c))
	
def us_congress_trends(request):
    if request.method == 'POST':    
        if request.POST['trend']:
            trendValue = request.POST['trend']
        else:
            errors = "<span style='color:red;'>Please input a correct trend. </span> <br>"
	cursor = connection.cursor()
    query='''
			SELECT name,count(name),tweet_text  FROM 
			(SELECT * from TwitterCollector_113thCongress.tweets where  tweets.tweet_text like '%{trendValue}%' order by tweet_id  ) as tweets,
			TwitterCollector_113thCongress.user_info as user_info
			where 
			tweets.user_id= user_info.user_id
			group by name
			order by tweet_id  desc limit 30000;'''
    cursor.execute(query)
	trendsArray=convert_tuple_array(cursor.fetchall())
    t = loader.get_template('trends.html')
    c = Context({'trendsArray':trendsArray,})
    return HttpResponse(t.render(c)) 

def get_latest_tweet(request):
    pass

	
#util functions --to be moved into seperate class

	
def convert_tuple_array(tuple):
    tupleArray = list(tuple) #convert to Array from tuple
    for i in range(0,len(tupleArray)):
        tupleArray[i]=list(tupleArray[i])
        tupleArray[i][0]=str(tupleArray[i][0]) #date time format fixes
    tupleArray = json.dumps(tupleArray, cls=DjangoJSONEncoder);
	return tupleArray;