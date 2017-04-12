from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.template import loader
from django.views.decorators.csrf import ensure_csrf_cookie
from utility import UserAuth, UserManagement


@ensure_csrf_cookie
def index(request):

    user_auth = UserAuth.UserAuth()
    permission = user_auth.user_auth(request.COOKIES, module='SUPER_ADMIN')
    if permission is False:
        return HttpResponseRedirect('/login/')

    new_user_unit = UserManagement.new_user_unit()
    update_old_user_unit = UserManagement.update_old_user_unit()

    template = loader.get_template('web_user_management/index.html')

    context = {
        'new_user_unit': new_user_unit,
        'update_old_user_unit': update_old_user_unit
    }
    return HttpResponse(template.render(context))


@ensure_csrf_cookie
def create_new_user(request):
    user_auth = UserAuth.UserAuth()
    permission = user_auth.user_auth(request.COOKIES, module='SUPER_ADMIN')
    if permission is False:
        context = {
            'status': 'AUTH_FAIL'
        }
        return JsonResponse(context)

    status, message = UserManagement.create_new_user(request)
    update_old_user_unit = UserManagement.update_old_user_unit()

    context = {
        'status': status,
        'message': message,
        'update_old_user_unit': update_old_user_unit
    }

    return JsonResponse(context)


@ensure_csrf_cookie
def select_old_user(request):
    user_auth = UserAuth.UserAuth()
    permission = user_auth.user_auth(request.COOKIES, module='SUPER_ADMIN')
    if permission is False:
        context = {
            'status': 'AUTH_FAIL'
        }
        return JsonResponse(context)

    status, message, user_profile = UserManagement.select_old_user(request)
    context = {
        'status': status,
        'message': message,
        'user_profile': user_profile
    }

    return JsonResponse(context)


@ensure_csrf_cookie
def update_user_info(request):
    user_auth = UserAuth.UserAuth()
    permission = user_auth.user_auth(request.COOKIES, module='SUPER_ADMIN')
    if permission is False:
        context = {
            'status': 'AUTH_FAIL'
        }
        return JsonResponse(context)

    status, message = UserManagement.update_user_info(request)
    context = {
        'status': status,
        'message': message
    }

    return JsonResponse(context)