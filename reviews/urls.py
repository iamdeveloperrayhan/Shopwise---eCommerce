from django.urls import path
from reviews import views

urlpatterns = [
    path('<int:pk>/update/', views.review_update, name='review_update'),
    path('<int:pk>/delete/', views.review_delete, name='review_delete'),
]
