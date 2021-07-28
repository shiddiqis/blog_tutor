




from django.conf.urls import url , include
from django.contrib import admin

from . import views
from blog import views as blogviews
from blog1 import views as blog1views
from blog2 import views as blog2views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^blog/$',  blogviews.index),
    url(r'^blog1/$',  blog1views.index),
    url(r'^blog2/$',  blog2views.index),
    url(r'^about/', include('about.urls')),
    url(r'^$',      views.index)
]
