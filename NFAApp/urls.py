from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('home',views.home,name='home'),
    path('',views.index,name='index'),
    path('add',views.add,name='add'),
    path('edit',views.edit,name='edit'),
    path('update/<str:id>',views.update,name='update'),
    path('delete/<str:id>',views.delete,name='delete'),
    path('chatpost',views.chatpost,name='chatpost'),
    path('chatget',views.chatget,name='chatget'),
    path('view_project/<str:id>',views.view_project,name='view_project'),

    path('vendor_add',views.vendor_add,name='vendor_add'),
    path('vendor_edit',views.vendor_edit,name='vendor_edit'),
    path('vendor_update/<str:id>',views.vendor_update,name='vendor_update'),
    path('vendor_delete/<str:id>',views.vendor_delete,name='vendor_delete')

]
