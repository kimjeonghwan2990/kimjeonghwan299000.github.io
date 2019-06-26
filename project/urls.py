from django.contrib import admin
from django.urls import path, include
import blog.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', blog.views.index, name='index'),
    # blog app
    path('blog/', include('blog.urls')),
    path('accounts/',include('accounts.urls')),
]
