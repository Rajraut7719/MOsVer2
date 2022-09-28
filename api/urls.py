from django.urls import path
from . import views


urlpatterns = [
     path('transaction/',views.MosCreateList.as_view()),
    path('transaction/<int:pk>',views.MosRetrieveUpdateDestroy.as_view()),
]
