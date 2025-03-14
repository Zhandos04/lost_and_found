from django.urls import path
from .views import item_list, item_detail, item_create, item_update, item_delete, item_moderation, item_approve, \
    recently_viewed_items, item_management
from .views import login_view, logout_view

urlpatterns = [
    path('items/', item_list, name='item_list'),
    path('items/<int:item_id>/', item_detail, name='item_detail'),
    path('items/new/', item_create, name='item_create'),
    path('items/<int:item_id>/edit/', item_update, name='item_update'),
    path('items/<int:item_id>/delete/', item_delete, name='item_delete'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('moderation/', item_moderation, name='item_moderation'),
    path('moderation/<int:item_id>/approve/', item_approve, name='item_approve'),
    path('recently_viewed/', recently_viewed_items, name='recently_viewed'),
    path('management/', item_management, name='item_management')
]
