from django.contrib import admin
from django.urls import include, path
from rest_framework.documentation import include_docs_urls
from rest_framework.schemas import get_schema_view
from rest_framework_swagger.views import get_swagger_view # new

API_TITLE = 'Blog API'
API_DESCRIPTION = 'A Web API for creating and editing blog posts.'
schema_view = get_swagger_view(title=API_TITLE) # new

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('posts.urls')),
    path('api-auth/', include('rest_framework.urls')),
    path('docs/', include_docs_urls(title=API_TITLE,
                                    description=API_DESCRIPTION)),
    # path('schema/', schema_view), # new
    path('swagger-docs/', schema_view), # new
]
