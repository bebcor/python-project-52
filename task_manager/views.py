import logging

import rollbar
from django.http import HttpResponse
from django.views import View

logger = logging.getLogger(__name__)


class RollbarTestView(View):
    def get(self, request):
        try:
            _ = 1 / 0
            
        except ZeroDivisionError:
            logger.error("Test Rollbar error: Division by zero", exc_info=True)
            
            rollbar.report_exc_info(
                request=request,
                extra_data={
                    'test_endpoint': True,
                    'user_id': request.user.id 
                     if request.user.is_authenticated else None
                }
            )
            
            return HttpResponse(
                "Test error generated and reported to Rollbar!",
                status=500
            )
        
        return HttpResponse("No error generated", status=200)
