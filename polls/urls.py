from django.urls import path
from polls import views
from django.conf.urls.static import static
from django.conf import settings

app_name = 'polls'

urlpatterns = [
    path('',views.Home),
    path('first_page/',views.Location),
    path('finished/',views.finished),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)