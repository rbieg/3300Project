from django.middleware import BaseMiddleware

class SaveFormInputMiddleware(BaseMiddleware):
    def process_request(self, request):
        if request.method == 'POST' and 'appliance-form' in request.POST:
            # Assuming 'appliance-form' is the form identifier
            request.session['name'] = request.POST.get('name', '')
            request.session['description'] = request.POST.get('description', '')
            request.session['heat_setting'] = request.POST.get('heat_setting', '')
        elif request.method == 'GET':
            # Populate the form with session data
            request.session.setdefault('name', '')
            request.session.setdefault('description', '')
            request.session.setdefault('heat_setting', '')
