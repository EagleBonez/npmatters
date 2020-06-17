from django.conf import settings
from django.conf.urls import include, url
from django.contrib import admin

from django.urls import path, include

from wagtail.admin import urls as wagtailadmin_urls
from wagtail.core import urls as wagtail_urls
from wagtail.documents import urls as wagtaildocs_urls

from search import views as search_views
from django.views.generic.base import TemplateView

from wagtail.contrib.sitemaps.views import sitemap

urlpatterns = [
    url(r'^django-admin/', admin.site.urls),

    url(r'^ednps-admin/', include(wagtailadmin_urls)),
    url(r'^documents/', include(wagtaildocs_urls)),

    url(r'^search/$', search_views.search, name='search'),

    path('planfinder/', include('planfinder.urls')),
    path('lhn/', include('lhn.urls')),

    path("robots.txt",TemplateView.as_view(template_name="robots.txt", content_type="text/plain")),
    url('^sitemap\.xml$', sitemap),
    # For anything not caught by a more specific rule above, hand over to
    # Wagtail's page serving mechanism. This should be the last pattern in
    # the list:
    url(r'', include(wagtail_urls)),

    # Alternatively, if you want Wagtail pages to be served from a subpath
    # of your site, rather than the site root:
    #    url(r'^pages/', include(wagtail_urls)),

]


if settings.DEBUG:
    from django.conf.urls.static import static
    from django.contrib.staticfiles.urls import staticfiles_urlpatterns

    # Serve static and media files from development server
    urlpatterns += staticfiles_urlpatterns()
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)