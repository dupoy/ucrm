from django.contrib.auth.decorators import login_required

from companies.models import Company


def get_company_list(request):
    if request.user.is_authenticated:
        return {
            'companies': Company.objects.filter(user=request.user)
        }
    return {}
