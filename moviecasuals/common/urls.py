from django.urls import path, include

from moviecasuals.common.views import HomePageView, AddCommentView, EditCommentView, DeleteCommentView, \
    AccessControlView, SearchBarView, GiveRatingView

urlpatterns = [
    path('', HomePageView.as_view(), name='homepage'),
    path('<int:pk>/', include([
        path('add_comment/', AddCommentView.as_view(), name='add_comment'),
        path('edit_comment/', EditCommentView.as_view(), name='edit_comment'),
        path('delete_comment/', DeleteCommentView.as_view(), name='delete_comment'),
    ])),
    path('access-control/', AccessControlView.as_view(), name='access-control'),
    path('searchbar/', SearchBarView.as_view(), name='searchbar'),
    path('rate_movie/<int:movie_id>/', GiveRatingView.as_view(), name='rate_movie'),
]
