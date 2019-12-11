from django.contrib import admin
# アプリとの連携にincludeが必要
from django.urls import path, include

# helloworldfunctionのディレクトリを教えてあげる
# HelloWorldViewのディレクトリも教えてあげる

from .views import helloworldfunction, HelloWorldView




# リクエストを受けて、次に何をするのか？
urlpatterns = [
    # 初めから書かれている
    # adminが実際に受け取るリクエスト、admin.site.urlsがレスポンス（ここでは管理画面を出しなさい）という設定
    # /adminでアクセスできる
    path('admin/', admin.site.urls),
    # funciton method classのどれかを書く必要がある。
    path('helloworld/', helloworldfunction),
    # TemplateViewのas_view()を呼び出すのかな？
    path('helloworld2/', HelloWorldView.as_view()),
    
    # projectとappの繋ぎこみ
    # helloworldappのurls.py
    # imort include忘れずにしましょう
    path('hello/', include('helloworldapp.urls')) # 次はアプリ側の設定する
]
