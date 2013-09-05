from django.shortcuts import render_to_response


def page1(request):
    return render_to_response('app1/page1.html')
