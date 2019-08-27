from django.contrib import admin
from django.urls import path
from BooksInfo import views #import views
 
 
urlpatterns = [
    path('admin/', admin.site.urls),
    path('books/', views.booklist.as_view()),
]