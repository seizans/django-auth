from django.shortcuts import render_to_response


def page1(request):
    if hasattr(request.user, 'profile'):
        print request.user.profile.height
    else:
        print 'does not have profile'
    return render_to_response('app1/page1.html')
