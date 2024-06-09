from app import views
from django.urls import path

urlpatterns = [
    path('', views.index, name='index'),
    path('index', views.index, name='index'),
    path('contato', views.contato, name='contato'),
    path('sobre', views.sobre, name='sobre'),
    path('projetos', views.projetos, name='projetos'),
    path('habilidades', views.habilidades, name='habilidades'),
    path('infatec', views.infatec, name='infatec'),
    path('uol', views.uol, name='uol'),
    path('ionic', views.ionic, name='ionic'),
    path('tecsus', views.tecsus, name='tecsus'),
    path('kitsune', views.kitsune, name='kitsune'),
    path('appOracle', views.appOracle, name='appOracle'),
]
