from django.http import HttpResponse
import rollbar

def test_rollbar(request):
    try:
        division_by_zero = 1 / 0
    except Exception as e:
        rollbar.report_exc_info()
        return HttpResponse("Произошла тестовая ошибка. Проверьте Rollbar!")
    
    return HttpResponse("Все работает!")