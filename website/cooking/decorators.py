from django.http import HttpResponse
from django.shortcuts import redirect

def unauthenticatedUser(viewFunc):
    def wrapperFunc(request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('index')
        else:
            return viewFunc(request, *args, **kwargs)
    return wrapperFunc

def allowedUsers(allowedRoles=[]):
    def decorator(viewFunc):
        def wrapperFunc(request, *args, **kwargs):
            group = None
            if request.user.groups.exists():
                group = request.user.groups.all()[0].name
            if group in allowedRoles:
                return viewFunc(request, *args, **kwargs)
            else:
                return HttpResponse("You are not authorized to view this page")
            return viewFunc(request, *args, **kwargs)
        return wrapperFunc
    return decorator