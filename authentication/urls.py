from django.urls import path
from .views import customer_view, home_view,UserRegisterView,login_view, order_delete, order_form, order_update,test_view,logout_view,dashboard


urlpatterns = [
    path('home/',home_view,name='home-view'),
    path('register/',UserRegisterView,name='register'),
    path('login/',login_view,name='login'),
    #path('login/',UserRegisterView,name='login')
    path('test/',test_view,name='test'),
    path('logout/',logout_view,name='logout'),
    path('dashboard',dashboard,name='dashboard'),
    path('orderform',order_form,name='order-form'),
    path('orderupdate/<int:order_id>/',order_update,name='order-update'),
    path('orderdelete/<int:order_id>/',order_delete,name='order-delete'),


]
