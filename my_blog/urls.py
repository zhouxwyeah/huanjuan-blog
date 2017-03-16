from django.conf.urls import include, url
from django.contrib import admin
import article.views as articleview
from article.views import RssFeed

urlpatterns = [
    # Examples:
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', articleview.home, name='home'),
    url(r'^(?P<id>\d+)/$', articleview.detail, name='detail'),
    url(r'^archives/$', articleview.archives, name='archives'),
    url(r'^aboutme/$', articleview.aboutme, name='aboutme'),
    url(r'^tag(?P<tag>\w+)/$', articleview.searchtag, name="search_tag"),
    url(r'^feed/$', RssFeed(), name="RSS"),  # 新添加的urlconf, 并将name设置为RSS, 方便在模板中使用url
    url(r'^test/$', articleview.test, name='test'),
]
