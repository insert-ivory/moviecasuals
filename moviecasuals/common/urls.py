from django.urls import path, include

from moviecasuals.common.views import HomePageView, AddCommentView, EditCommentView, DeleteCommentView

urlpatterns = [
    path('', HomePageView.as_view(), name='homepage'),
    path('add_comment/<int:movie_id>/', AddCommentView.as_view(), name='add_comment'),
    path('<int:pk>/', include([
        path('edit_comment/', EditCommentView.as_view(), name='edit_comment'),
        path('delete_comment/', DeleteCommentView.as_view(), name='delete_comment'),
    ])),
]