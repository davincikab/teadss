from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('decisionsupport.urls')),
    path('account/', include('account.urls')),
]

admin.AdminSite.site_header = "Tea Decision Support"
admin.AdminSite.site_title = "Tea Decision Support"
admin.AdminSite.index_title = "Tea Decision Support"
