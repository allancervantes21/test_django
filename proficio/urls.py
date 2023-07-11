from django.urls import path
from .views import item_list, item_detail, item_create, item_update, item_delete


urlpatterns = [
    path('', item_list, name="item_list"),
    path('<int:pk>', item_detail, name="item_detail"),
    path('create', item_create, name="item_create"),
    path('<int:pk>/update', item_update, name="item_update"),
    path('<int:pk>/delete', item_delete, name="item_delete"),
]