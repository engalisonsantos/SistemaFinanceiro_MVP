from django.http import HttpResponseForbidden

def master_required(view_func):
    def _wrapped(request, *args, **kwargs):
        if not request.user.is_authenticated:
            return view_func(request, *args, **kwargs)
        if getattr(request.user, "role", None) != "MASTER":
            return HttpResponseForbidden("Acesso restrito ao usuário Master.")
        return view_func(request, *args, **kwargs)
    return _wrapped
