# apps/categories/views.py

from django.http import JsonResponse

def category_list(request):
    return JsonResponse({"message": "Category list endpoint"})
