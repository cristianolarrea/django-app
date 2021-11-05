from django.urls import path
from fgv import views as views

urlpatterns=[
    path('', views.index, name='index'),
    path('index/', views.index, name='index'),
    path('redireciona/', views.redireciona, name="redireciona"),
    path('special/', views.retorna_html, name='retorna-html'),
    path('special/<int:param>', views.view_dinamic_int, name='dinamica-int'),
    path('special/<str:param>', views.view_dinamic_str, name='dinamica-str'),
    path('dtl/', views.special_dtl, name="retorna-html-dtl")
]