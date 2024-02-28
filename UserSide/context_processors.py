from UserSide.views import users_cart

def message_processor(request):
    return {'cart_no': len(users_cart)}



    