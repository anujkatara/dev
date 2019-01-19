"""dev URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

# Call myroot properties
import myroot.views.vmain


urlpatterns = [
    path('admin/', admin.site.urls),
    path('helloworld/', myroot.views.vmain.hello_world_view,
         name='helloworld'),

    path('django-basic-crud-create/',
         myroot.views.vmain.basic_crud_create_view,
         name='basic_crud_create'),

    path('django-basic-crud-list/',
         myroot.views.vmain.basic_crud_list_view,
         name='basic_crud_list'),

    path('django_basic_crud_delete/',
         myroot.views.vmain.basic_crud_del_row_view,
         name='basic_crud_delete'),

    path('<slug:slug>-<int:id>/',
         myroot.views.vmain.basic_crud_dynamic_public_page_view,
         name='basic_crud_dyn_pub_page'),

    path('basic_crud/<int:id>/change/', myroot.views.vmain.basic_crud_update_row_view,
         name='change_basic_crud'),

    path('basic_search_text/', myroot.views.vmain.basic_search_text_view,
         name='basic_search_text'),

    path('basic_search_dr/', myroot.views.vmain.basic_search_dr_view,
         name='basic_search_dr'),

    path('search/', myroot.views.vmain.search_view,
         name='search'),

    path('emptysearch/', myroot.views.vmain.emptysearch_view,
         name='emptysearch'),
]
