from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.start, name='start'),
    path('emp_login/',views.emp_login, name='emp_login'),
    path('emp_login/tpr/', views.display_form_data, name='tpr'),
    path('prince/', views.prince, name='prince'),                                                                                           

    path('login/', views.login, name='login'),
    path('login/TPR/', views.TPR, name='TPR'),
    path('login/TPR/tpr', views.admin_view, name='a_tpr'),
    path('login/TPR/tpr/<str:tpr_number>/delete/', views.delete_tpr, name='delete_tpr'),
    path('CTL/', views.CTL, name='CTL'),
    path('CRCA/', views.CRCA, name='CRCA'),
    path('shearing/', views.shearing, name='shearing'),
    path('SPC/', views.SPC, name='SPC'),
    path('slitting/', views.slitting, name='slitting'),
    path('Galva/', views.Galva, name='Galva'),



]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
