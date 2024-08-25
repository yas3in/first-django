from webdesign.urls import path
from blog.views import blog_pages, list_number, sum_number


urlpatterns = [
    path('list/', blog_pages),
    
    #get a number for show in url
    #variable use to path in <> and can use thi varibale in function
    path('list/<int:number>', list_number),
    path('list/<slug:number>', sum_number),
]