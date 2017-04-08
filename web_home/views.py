from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.views.decorators.csrf import ensure_csrf_cookie
from utility import UserAuth


@ensure_csrf_cookie
def index(request):

    user_auth = UserAuth.UserAuth()
    permission = user_auth.user_auth(request.COOKIES)
    if permission is False:
        return HttpResponseRedirect('/login/')

    template = loader.get_template('web_home/index.html')

    context = {
        'admin_permission': user_auth.user_auth(request.COOKIES, module='SUPER_ADMIN')
    }
    return HttpResponse(template.render(context))