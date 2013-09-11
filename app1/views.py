# encoding=utf-8
from django.shortcuts import render_to_response
from django.views.generic.edit import CreateView

import facebook
import allauth.socialaccount.models as m

import app1.twitter as twitter
from .forms import MyForm

from allauth.account.views import SignupView
from .forms import SignupForm
from django.template import RequestContext


class MySignupView(SignupView):
    form_class = SignupForm
    success_url = '/admin/'


class MyView(CreateView):
    template_name = 'signup.html'
    form_class = MyForm
    success_url = '/app1/sign'


def page1(request):
    if hasattr(request.user, 'profile'):
        print request.user.profile.height
    else:
        print 'does not have profile'
    return render_to_response(
        'app1/page1.html',
        context_instance=RequestContext(request)
    )


def tweet(request):
    account = request.user.socialaccount_set.get()
    api = twitter_api(account)
    status = api.GetUserTimeline(user_id=account.uid)
    for s in status:
        print s.text
    message = 'twitter post test'
    poststatus = api.PostUpdate(message)
    print poststatus
    return render_to_response('app1/page1.html')


def tweet_media(request):
    account = request.user.socialaccount_set.get()
    api = twitter_api(account)
    message = 'media post test'
    media = '/Users/seizans/Downloads/picture.jpg'
    status = api.PostMedia(message, media)
    print status
    return render_to_response('app1/page1.html')


def twitter_api(account):
    app = m.SocialApp.objects.get(provider='twitter')
    token = m.SocialToken.objects.get(app=app, account=account)
    api = twitter.Api(
        consumer_key=app.client_id,
        consumer_secret=app.secret,
        access_token_key=token.token,
        access_token_secret=token.token_secret,
    )
    return api


def face(request):
    graph = facebook_graph(request.user)
    profile = graph.get_object('me')
    print profile
    return render_to_response('app1/page1.html')


def facepost(request):
    graph = facebook_graph(request.user)
    message = 'From facepost \n\n url \n hoge'
    link = 'http://docs.python.jp/2/library/index.html'
    graph.put_object('me', 'feed', message=message, link=link)
    return render_to_response('app1/page1.html')


def facebook_graph(user):
    account = user.socialaccount_set.get()
    app = m.SocialApp.objects.get(provider='facebook')
    token = m.SocialToken.objects.get(app=app, account=account)
    graph = facebook.GraphAPI(token.token)
    return graph


def face_image(request):
    graph = facebook_graph(request.user)
    with open('/Users/seizans/Downloads/picture.jpg') as image:
        message = 'message with image to facebook'
        graph.put_photo(image, message)
    return render_to_response('app1/page1.html')
