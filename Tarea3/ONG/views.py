from django.shortcuts import render


def onghome(request):
    return render(request, 'ong.html', {})
