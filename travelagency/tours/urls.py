from django.contrib import admin
from django.urls import path, re_path
from tours.views import *

urlpatterns = [
    path('', main_page, name='home'),
    re_path(r'archive/(?P<year>[0-9]{4})/', archive),
    # path(r'^test/(?P<page>\w+\.html)$', page_view),
    # path('test/<str:page>/', page_view)
    path('category/<slug:tour_category>/', show_post, name='category'),
    path('/admin/logout/', logout_func, name='logout'),
    path('/admin/', admin.site.urls, name='admin_panel'),
    path('bored/', bored_api_test),
    path('jokes/', jokes_api_test),
]
