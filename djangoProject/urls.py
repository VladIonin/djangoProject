from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from django.urls import path
from main import views

urlpatterns = [
    path('', views.index, name='home'),
    path('adding', views.add, name='add'),
    path('admin/', admin.site.urls),
    path('delete-card/<int:id>/', views.deleteCard, name='delete')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
