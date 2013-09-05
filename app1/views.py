from django.shortcuts import render_to_response


def page1(request):
    if request.user.get_profile():
        print request.user.get_profile()
    else:
        print 'does not have profile'
    return render_to_response('app1/page1.html')
