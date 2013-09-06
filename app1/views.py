# encoding=utf-8
from django.shortcuts import render_to_response
import twitter
import allauth.socialaccount.models as m


def page1(request):
    if hasattr(request.user, 'profile'):
        print request.user.profile.height
    else:
        print 'does not have profile'
    return render_to_response('app1/page1.html')


def tweet(request):
    account = request.user.socialaccount_set.get()
    app = m.SocialApp.objects.get(provider='twitter')
    token = m.SocialToken.objects.get(app=app, account=account)
    api = twitter.Api(
        consumer_key=app.client_id,
        consumer_secret=app.secret,
        access_token_key=token.token,
        access_token_secret=token.token_secret,
    )
    status = api.GetUserTimeline(user_id=account.uid)
    for s in status:
        print s.text
    return render_to_response('app1/page1.html')
