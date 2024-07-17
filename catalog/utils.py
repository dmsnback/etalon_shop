from django.core.paginator import Paginator


POST_IN_PAGE = 5


def get_page_context(product_list, request):
    paginator = Paginator(product_list, 3)
    page_number = request.GET.get('page')
    return paginator.get_page(page_number)
