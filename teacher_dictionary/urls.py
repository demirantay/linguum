from django.urls import path
from . import views

urlpatterns = [
    # teacher dictionary - explore page
    path(
        "teacher/dictionary/explore/",
        views.teacher_dictionary_explore,
        name="teacher_dictionary_explore"
    ),

    # teacher dictionary - CRUD page
    path(
        "teacher/dictionary/build/<str:dict_lang>/<str:dict_speaker_language>/",
        views.teacher_dictionary_build,
        name="teacher_dictionary_build"
    ),

    # teacher dictionary - update page
    path(
        "teacher/dictionary/update/<int:id>/",
        views.teacher_dictionary_update,
        name="teacher_dictionary_update"
    ),
]
