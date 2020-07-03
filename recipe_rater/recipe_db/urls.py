from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('register', views.reg_user),
    path('login', views.log_user),
    path('profile/<int:id>', views.profile),
    path('friend_profile/<int:id>', views.friend_profile),
    path('user_friends/<int:id>', views.user_friends),
    path('add_friend/<int:id>', views.add_friend),
    path('remove_friend/<int:id>', views.remove_friend),
    path('add_recipe', views.render_add_form),
    path('process_recipe', views.add_recipe),
    path('edit_recipe/<int:id>', views.render_edit_form),
    path('process_recipe_edit/<int:id>', views.process_edit),
    path('delete_recipe/<int:id>', views.delete_recipe),
    path('recipe/<int:id>', views.recipe_page),
    path('logout', views.logout),
]
