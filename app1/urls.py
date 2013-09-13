from django.conf.urls import patterns, url
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView

from app1 import views
from .views import MyView, MySignupView
from allauth.account.views import login, confirm_email
from allauth.account import views as account
from allauth.socialaccount import views as social
from allauth.socialaccount.providers.facebook import views as fb


urlpatterns = patterns(
    '',
    url(r'^login$', login, name='account_login'),
    url(r'^confirm_email/(?P<key>\w+)/$', confirm_email,
        name='account_confirm_email'),
    url(r'^account/logout/$', account.logout, name='account_logout'),
    url(r'^account/password/reset/$', account.password_reset,
        name='account_reset_password'),

    url(r'^social/login/cancelled/$', social.login_cancelled,
        name='socialaccount_login_cancelled'),
    url(r'^social/login/error/$', social.login_error,
        name='socialaccount_login_error'),
    url(r'^social/signup/$', views.SocialSignupView.as_view(),
        name='socialaccount_signup'),

    url(r'^facebook/login/$', fb.oauth2_login, name='facebook_login'),
    url(r'^facebook/callback/$', fb.oauth2_callback, name='facebook_callback'),
    url(r'^facebook/login/token/$', fb.login_by_token,
        name='facebook_login_by_token'),
    url(r'^facebook/channel/$', fb.channel, name='facebook_channel'),

    url(r'^twitter/login/$', login, name='twitter_login'),

    url(r'^sign$', MyView.as_view()),
    url(r'^signup$', MySignupView.as_view(), name='account_signup'),
    url(r'^page1$', views.page1),
    url(r'^log$', login_required(
        TemplateView.as_view(template_name='app1/page1.html'))),
    url(r'^tweet$', views.tweet),
    url(r'^tweet_media$', views.tweet_media),
    url(r'^face$', views.face),
    url(r'^facepost$', views.facepost),
    url(r'^face_image$', views.face_image),
)
