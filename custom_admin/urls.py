from django.urls import path

from . import views

urlpatterns = [
    path('admin-dashboard', views.admin_dashboard, name='admin_dashboard'),
    path('admin-dashboard/logout', views.admin_logout, name='admin_logout'),
    path('admin-dashboard/admin-listings', views.admin_listings, name='admin_listings'),
    path('admin-dashboard/admin-listings/add', views.admin_add_listing, name='admin_add_listing'),
    path('admin-dashboard/admin-listings/<int:listing_id>', views.admin_view_listing, name='admin_view_listing'),
    path('admin-dashboard/admin-listings/<int:listing_id>/edit', views.admin_edit_listing, name='admin_edit_listing'),
    path('admin-dashboard/admin-listings/<int:listing_id>/delete', views.admin_delete_listing, name='admin_delete_listing'),
    path('admin-dashboard/admin-users', views.admin_users, name='admin_users'),
    path('admin-dashboard/admin-users/<int:user_id>/delete', views.admin_delete_user, name='admin_delete_user'),
    path('admin-dashboard/admin-realtors', views.admin_realtors, name='admin_realtors'),
    path('admin-dashboard/admin-realtors/add', views.admin_add_realtor, name='admin_add_realtor'),
    path('admin-dashboard/admin-realtors/<int:realtor_id>/edit', views.admin_edit_realtor, name='admin_edit_realtor'),
    path('admin-dashboard/admin-realtors/<int:realtor_id>/delete', views.admin_delete_realtor, name='admin_delete_realtor'),
    path('admin-dashboard/admin-contacts', views.admin_contacts, name='admin_contacts'),
]
