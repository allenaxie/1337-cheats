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
    path('cheatsheets/<int:cheatsheet_id>/add_review',
         views.add_review, name='add_review'),
    path('reviews/<int:pk>/update/',
         views.ReviewUpdate.as_view(), name='reviews_update'),
    path('reviews/<int:pk>/delete/',
         views.ReviewDelete.as_view(), name='reviews_delete'),
    path('cheatsheets/<int:cheatsheet_id>/add_favorite',
         views.add_favorite, name='add_favorite'),
    path('favorites/<int:pk>/delete/',
         views.FavoriteDelete.as_view(), name='favorites_delete'),
    # path('favorites/', views.FavoriteList.as_view(), name='favorites_index')
    path('favorites/', views.favorites_index, name='favorites_index'),
    path('cheatsheets/<int:cheatsheet_id>/add_photo/',
         views.add_photo, name='add_photo'),
]
