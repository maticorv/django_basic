from datetime import datetime
from django.http import HttpResponse, JsonResponse


def hola(request):
    return HttpResponse('La fecha es: {}'.format(datetime.now().strftime("%b %dth, /%Y - %H:%M ")))


def sort_integers(request):
    numbers = [int(x) for x in request.GET.get('numbers').split(',')]
    numbers.sort()
    return JsonResponse(numbers, safe=False)
   # return HttpResponse(json.dumps(numbers), content_type='application/json')


def say_hi(request, name, age):
    if age < 12:
        message = 'Sorry {}, you are not allowed here'.format(name)
    else:
        message = 'Hello {}, you are Welcome'.format(name)
    return HttpResponse(message)
