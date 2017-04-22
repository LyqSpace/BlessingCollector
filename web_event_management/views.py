from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.template import loader
from django.views.decorators.csrf import ensure_csrf_cookie
from utility import UserAuth, EventManagement


@ensure_csrf_cookie
def index(request):

    user_auth = UserAuth.UserAuth()
    permission = user_auth.user_auth(request.COOKIES, module='SUPER_ADMIN')
    if permission is False:
        return HttpResponseRedirect('/login/')

    add_birthday_unit = EventManagement.add_birthday_unit()
    add_event_unit = EventManagement.add_event_unit()
    event_list_unit = EventManagement.event_list_unit()

    template = loader.get_template('web_event_management/index.html')

    context = {
        'add_birthday_unit': add_birthday_unit,
        'add_event_unit': add_event_unit,
        'event_list_unit': event_list_unit
    }
    return HttpResponse(template.render(context))


@ensure_csrf_cookie
def add_birthday(request):

    user_auth = UserAuth.UserAuth()
    permission = user_auth.user_auth(request.COOKIES, module='SUPER_ADMIN')
    if permission is False:
        return HttpResponseRedirect('/login/')

    status, message = EventManagement.add_birthday(request)
    content = EventManagement.event_list_unit()

    context = {
        'status': status,
        'message': message,
        'content': content
    }

    return JsonResponse(context)


@ensure_csrf_cookie
def add_event(request):
    user_auth = UserAuth.UserAuth()
    permission = user_auth.user_auth(request.COOKIES, module='SUPER_ADMIN')
    if permission is False:
        return HttpResponseRedirect('/login/')

    status, message = EventManagement.add_event(request)
    content = EventManagement.event_list_unit()

    context = {
        'status': status,
        'message': message,
        'content': content
    }

    return JsonResponse(context)


@ensure_csrf_cookie
def delete_event(request):
    user_auth = UserAuth.UserAuth()
    permission = user_auth.user_auth(request.COOKIES, module='SUPER_ADMIN')
    if permission is False:
        return HttpResponseRedirect('/login/')

    status, message = EventManagement.delete_event(request)
    content = EventManagement.event_list_unit()

    context = {
        'status': status,
        'message': message,
        'content': content
    }

    return JsonResponse(context)


def arrange_blessings(request):
    user_auth = UserAuth.UserAuth()
    permission = user_auth.user_auth(request.COOKIES, module='SUPER_ADMIN')
    if permission is False:
        return HttpResponseRedirect('/login/')

    blessings_page = EventManagement.arrange_blessings(request)

    return HttpResponse(blessings_page)