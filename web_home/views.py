from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.template import loader
from django.views.decorators.csrf import ensure_csrf_cookie
from utility import UserAuth, Home


@ensure_csrf_cookie
def index(request):

    user_auth = UserAuth.UserAuth()
    permission = user_auth.user_auth(request.COOKIES)
    if permission is False:
        return HttpResponseRedirect('/login/')

    event_list_unit = Home.event_list_unit(request)
    template = loader.get_template('web_home/index.html')

    context = {
        'SUPER_ADMIN': user_auth.user_auth(request.COOKIES, module='SUPER_ADMIN'),
        'event_list_unit': event_list_unit
    }
    return HttpResponse(template.render(context))


@ensure_csrf_cookie
def save_blessing(request):
    user_auth = UserAuth.UserAuth()
    permission = user_auth.user_auth(request.COOKIES)
    if permission is False:
        return HttpResponseRedirect('/login/')

    status, message = Home.save_blessing(request)

    context = {
        'status': status,
        'message': message
    }

    return JsonResponse(context)