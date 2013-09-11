from django.conf.urls import patterns, url
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView

from app1 import views
from .views import MyConfirmEmailView, MyView, MySignupView


urlpatterns = patterns(
    '',
    url(r'^confirm_email/(?P<key>\w+)/$', MyConfirmEmailView.as_view(),
        name='my_account_confirm_email'),
    url(r'^sign$', MyView.as_view()),
    url(r'^signup$', MySignupView.as_view()),
    url(r'^page1$', views.page1),
    url(r'^log$', login_required(
        TemplateView.as_view(template_name='app1/page1.html'))),
    url(r'^tweet$', views.tweet),
    url(r'^tweet_media$', views.tweet_media),
    url(r'^face$', views.face),
    url(r'^facepost$', views.facepost),
    url(r'^face_image$', views.face_image),
)
