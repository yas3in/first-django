from webdesign.urls import path
from blog.views import blog_pages


urlpatterns = [
    path('list/', blog_pages),
]