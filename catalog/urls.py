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
    DescriptionListView,
    DescriptionCreateView,
    DescriptionUpdateView,
    ServicesCatalogDeleteView,
    ServicesCatalogListView,
    ServicesCatalogDetailView,
    ServicesCatalogCreateView,
    ServicesCatalogUpdateView,
)

app_name = CatalogConfig.name

urlpatterns = [
    path('base/', base, name='base'),

    path("", ServicesListView.as_view(), name="service_list"),
    path("catalog/<int:pk>/", ServicesDetailView.as_view(), name="service_detail"),
    path("catalog/create", ServicesCreateView.as_view(), name="service_create"),
    path(
        "catalog/<int:pk>/update/", ServicesUpdateView.as_view(), name="service_update"
    ),
    path(
        "catalog/<int:pk>/delete", ServicesDeleteView.as_view(), name="service_delete"
    ),

    path("description_list/", DescriptionListView.as_view(), name="description_list"),
    path("description_create/", DescriptionCreateView.as_view(), name="description_create"),
    path("description_update/<int:pk>/", DescriptionUpdateView.as_view(), name="description_update"),

    path('contacts/', contacts, name='contacts'),
    path('feedback/', feedback, name='feedback'),
    path('main_page/', main_page, name='main_page'),

    path("servicescatalog/", ServicesCatalogListView.as_view(), name="servicescatalog_list"),
    path("servicescatalog/<int:pk>/", ServicesCatalogDetailView.as_view(), name="servicescatalog_detail"),
    path("servicescatalog/create", ServicesCatalogCreateView.as_view(), name="servicescatalog_create"),
    path(
        "servicescatalog/<int:pk>/update/", ServicesCatalogUpdateView.as_view(), name="servicescatalog_update"
    ),
    path(
        "servicescatalog/<int:pk>/delete", ServicesCatalogDeleteView.as_view(), name="servicescatalog_delete"
    ),
]
