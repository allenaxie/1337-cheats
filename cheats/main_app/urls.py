from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('accounts/sign_up/', views.signup, name='signup'),
    path('menu/', views.menu, name='menu'),
    path('cheatsheets/', views.cheatsheets_index, name='cheatsheets_index'),
    path('cheatsheets/create/', views.CheatsheetCreate.as_view(),
         name='cheatsheets_create'),
    path('cheatsheets/<int:cheatsheet_id>/',
         views.cheatsheets_detail, name='cheatsheets_detail'),
    path('cheatsheets/<int:pk>/update/',
         views.CheatsheetUpdate.as_view(), name='cheatsheets_update'),
    path('cheatsheets/<int:pk>/delete/',
         views.CheatsheetDelete.as_view(), name='cheatsheets_delete'),
]
