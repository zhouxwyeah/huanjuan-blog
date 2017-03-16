from django.conf.urls import include, url
from django.contrib import admin
import article.views as articleview

urlpatterns = [
    # Examples:
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', articleview.home, name='home'),
    url(r'^(?P<my_args>\d+)/$', articleview.detail, name='detail'),
    url(r'^test/$', articleview.test, name='test'),
]
