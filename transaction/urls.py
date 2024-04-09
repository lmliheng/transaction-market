from django.urls import path,include
from . import views

app_name = 'translation'

urlpatterns = [
    path('', views.tra_index, name='index'),
    path('owner', views.tra_owner, name='owner'),
    # ... 其他URL模式 ...

    path('post_item/', views.post_item, name='post_item'),
    path('edit_contact/', views.edit_contact, name='edit_contact'),
    path('personal_page/', views.personal_page, name='personal_page'),
    path('manage_items/', views.manage_items, name='manage_items'),
    path('item/<int:pk>/', views.ItemDetailView.as_view(), name='item_detail'),
]