from . import views
from django.urls import path


urlpatterns = [
    path('', view=views.index, name="index"),
    path('home', view=views.home, name="home"),
    path('mark-complete/<int:item_id>', view=views.mark_complete, name="mark-complete"),
    path('delete_todo/<int:item_id>', view=views.delete_todo, name="delete-todo"),
    path('add_todo', view=views.add_todo, name='add-todo')
]