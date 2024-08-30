from django.urls import path
from catalog.apps import CatalogConfig
from catalog.views import (
    ServicesListView,
    ServicesDetailView,
    ServicesCreateView,
    ServicesUpdateView,
    ServicesDeleteView,
    contacts,
    base,
    feedback,
    main_page,
    DescriptionCreateView,
    DescriptionUpdateView,

)

app_name = CatalogConfig.name

urlpatterns = [
    path('base/', base, name='base'),

    path("catalog/", ServicesListView.as_view(), name="service_list"),
    path("catalog/<int:pk>/", ServicesDetailView.as_view(), name="service_detail"),
    path("catalog/create", ServicesCreateView.as_view(), name="service_create"),
    path(
        "catalog/<int:pk>/update/", ServicesUpdateView.as_view(), name="service_update"
    ),
    path(
        "catalog/<int:pk>/delete", ServicesDeleteView.as_view(), name="service_delete"
    ),

    path("description/create", DescriptionCreateView.as_view(), name="description_create"),
    path("description/<int:pk>/update/", DescriptionUpdateView.as_view(), name="description_update"),

    path('contacts/', contacts, name='contacts'),
    path('feedback/', feedback, name='feedback'),
    path('', main_page, name='main_page'),

]
