from company.models import Company


def companies(request):
    return {
        'companies': Company.objects.filter(user=request.user)
    }
