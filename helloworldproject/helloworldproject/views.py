# djangoに搭載されているので....
from django.http import HttpResponse
# 同じく
from django.views.generic import TemplateView

# functionを定義してあげる
# requestじゃなくても良いけど、requestを受け取っているのでこれで良い
def helloworldfunction(request):
    # requestをもらったからレスポンスを返してあげる
    # djangoに標準搭載されているclassから新しいオブジェクトを作ってあげてreturn
    return HttpResponse('hello world')

# class based view
# django.views.genericクラスのTemplateViewを継承
class HelloWorldView(TemplateView):
    # hello.htmlを作っとかないといけない=>settings.pyにどこにTemplateを置くのか書いておく
    template_name = 'hello.html'