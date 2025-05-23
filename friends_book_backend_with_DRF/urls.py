"""
URL configuration for friends_book_backend_with_DRF project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include


from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include("main.urls")),
    path("api/v1/",include("api.urls")),
    # path("certificate/", include("certificate.urls")),
    # path("comment/", include("comment.urls")),
    # path("experience/", include("experience.urls")),
    # path("like/", include("likeAndEmoji.urls")),
    # path("photo/", include("photo.urls")),
    # path("post/", include("post.urls")),
    # path("personal_details/", include("personal_details.urls")),
    # path("school/", include("school.urls")),
    # path("collage/", include("collage.urls")),
    # path("university/", include("university.urls")),
    # path("story/", include("story.urls")),
    # path("video/", include("video.urls")),
    # path("viewer/", include("viewer.urls")),
    # path("person/", include("person.urls")),
]



urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)