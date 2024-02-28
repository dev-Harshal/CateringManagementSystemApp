from django.shortcuts import redirect




def login_required_custom(view_func):
    def wrapped_view(request, *args, **kwargs):
        if not request.user.is_authenticated:
            print(request.META.get('HTTP_REFERER'),"Request QRL")
            next_url = f'/signup/?from={request.META.get("HTTP_REFERER")}'
            return redirect(next_url)
        return view_func(request, *args, **kwargs)
    return wrapped_view