from django.urls import path

from researches.views import ResearchDetailView, ResearchView

urlpatterns = [
    path('/<int:research_id>', ResearchDetailView.as_view()),
    path('', ResearchView.as_view())
]