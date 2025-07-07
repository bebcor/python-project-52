import logging
import rollbar
from django.http import HttpResponse

logger = logging.getLogger(__name__)

def test_rollbar(request):
    try:
        division_by_zero = 1 / 0
    except Exception as e:
        logger.error("Test error occurred: %s", str(e), exc_info=True)
        
        rollbar.report_exc_info(request=request)
        
        return HttpResponse("Test error generated and reported to Rollbar!")
    
    return HttpResponse("No error generated")
