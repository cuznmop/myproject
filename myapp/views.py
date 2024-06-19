from django.shortcuts import render

# Create your views here.
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt  # 在开发时禁用 CSRF，但生产环境中应启用
def my_api_view(request):
    if request.method == 'POST':
        # 假设我们接收一个名为 'field1' 的字段
        field1 = request.POST.get('field1', '')
        
        # 你可以在这里添加处理逻辑
        
        # 发送一个名为 'field2' 的字段回给 Postman
        return JsonResponse({'field2': f'You sent: {field1}'})
    else:
        return JsonResponse({'error': 'Method Not Allowed'}, status=405)
