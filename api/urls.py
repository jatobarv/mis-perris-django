from django.conf.urls.import url, include, patterns
import views

url(r'^api/v1/', include('api.urls', namespace="api")),
