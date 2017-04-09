from django.http import HttpResponse, JsonResponse
from django.template import loader
from utility import UserAuth


def index(request):

    template = loader.get_template('web_login/index.html')
    context = {
    }
    return HttpResponse(template.render(context))


def user_login(request):

    try:
        email = request.POST['email']
        token = request.POST['token']
    except KeyError:
        context = {
            'status': 'FAIL',
            'message': '缺少参数，登录失败！'
        }
        return JsonResponse(context)

    user_auth = UserAuth.UserAuth()
    login_state, message, full_name = user_auth.login(email, token)

    context = {
        'status': login_state,
        'message': message,
        'fullname': full_name,
    }

    return JsonResponse(context)