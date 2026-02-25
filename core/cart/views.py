from django.views.generic import View
from django.http import JsonResponse
from .context_processors import CartSession



class SessionAddProduct(View):
    
    def post(self, request, *args, **kwargs):
        cart = CartSession(request.session)

        return JsonResponse({"cart":cart})
    
    