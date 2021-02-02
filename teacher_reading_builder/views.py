# Main Imports

# Django Imports
from django.shortcuts import render, get_object_or_404, HttpResponse
from django.http import HttpResponseRedirect
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.models import User

# My Module Imports
from profile_settings.models import BasicUserProfile
from teacher_authentication.models import TeacherUserProfile
from utils.session_utils import get_current_user, get_current_user_profile
from utils.session_utils import get_current_teacher_user_profile

from .models import TeacherReadingLesson, TeacherReadingLessonSentence
from .models import TeacherReadingLessonSentenceTolerance


def teacher_reading_build(request, course_language, course_speaker_language):
    """
    in this page the teacher can build the neccessary reading lessons
    """
    # Deleting admin-typed user session
    # Deleting programmer-typed-user session

    # Get the current users
    current_basic_user = get_current_user(request, User, ObjectDoesNotExist)

    current_basic_user_profile = get_current_user_profile(
        request,
        User,
        BasicUserProfile,
        ObjectDoesNotExist
    )

    # Getting the teacher profile
    current_teacher_profile = get_current_teacher_user_profile(
        request,
        User,
        TeacherUserProfile,
        ObjectDoesNotExist
    )

    # Adding a new lesson to the teacher course form processing
    empty_lesson_name = False

    if request.POST.get("teacher_reading_builder_lesson_add_button"):
        lesson_name = request.POST.get("lesson_name")
        lesson_level = request.POST.get("lesson_level")

        if bool(lesson_name) == False or lesson_name == "":
            empty_lesson_name = True
        else:
            new_lesson = TeacherReadingLesson(
                course=current_teacher_profile.teacher_course,
                teacher=current_teacher_profile,
                title=lesson_name,
                level=lesson_level,
            )
            new_lesson.save()
            return HttpResponseRedirect(
                "/teacher/reading/build/" + course_language +
                "/" + course_speaker_language + "/"
            )

    # Getting all of the lessons of the current course

    # Automation for the teacher course

    data = {
        "current_basic_user": current_basic_user,
        "current_basic_user_profile": current_basic_user_profile,
        "current_teacher_profile": current_teacher_profile,
        "empty_lesson_name": empty_lesson_name,
    }

    if "teacher_user_logged_in" in request.session:
        return render(request, "teacher_reading_builder/build.html", data)
    else:
        return HttpResponseRedirect("/")


def teacher_reading_update(request, id):
    """

    """

    data = {

    }

    return render(request, "teacher_reading_builder/update.html", data)


def teacher_reading_add_sentence(request):
    """
    in this page the teachers can add sentences to the reading lessons
    """
    # Deleting admin-typed user session
    # Deleting programmer-typed-user session

    # Get the current users
    current_basic_user = get_current_user(request, User, ObjectDoesNotExist)

    current_basic_user_profile = get_current_user_profile(
        request,
        User,
        BasicUserProfile,
        ObjectDoesNotExist
    )

    # Getting the teacher profile
    current_teacher_profile = get_current_teacher_user_profile(
        request,
        User,
        TeacherUserProfile,
        ObjectDoesNotExist
    )

    # Get the current reading lessons for 'select' dropdown
    try:
        all_lessons = TeacherReadingLesson.objects.filter(
            course=current_teacher_profile.teacher_course
        )
    except ObjectDoesNotExist:
        all_lessons = None

    # Add the new lesson form processing
    empty_input = False

    if request.POST.get("teacher_reading_sentence_addition_form_submit_btn"):
        sentence_level = request.POST.get("sentence_level")
        question_prompt = request.POST.get("question_prompt")
        answer = request.POST.get("answer")
        selected_lesson_id = request.POST.get("selected_lesson_id")

        # get the selected lesson
        try:
            selected_lesson = TeacherReadingLesson.objects.get(
                id=selected_lesson_id
            )
        except ObjectDoesNotExist:
            selected_lesson = None

        # check if anything has empty input
        if bool(question_prompt) == False or question_prompt == "" or \
           bool(answer) == False or answer == "":
            empty_input = True
        else:
            new_sentence = TeacherReadingLessonSentence(
                lesson=selected_lesson,
                level=sentence_level,
                question_prompt=question_prompt,
                answer=answer
            )
            new_sentence.save()
            return HttpResponseRedirect(
                "/teacher/reading/build/" +
                current_teacher_profile.teacher_course.course_language + "/" +
                current_teacher_profile.teacher_course.course_speakers_language
                + "/"
            )

    data = {
        "current_basic_user": current_basic_user,
        "current_basic_user_profile": current_basic_user_profile,
        "current_teacher_profile": current_teacher_profile,
        "all_lessons": all_lessons,
        "empty_input": empty_input,
    }

    if "teacher_user_logged_in" in request.session:
        return render(request, "teacher_reading_builder/add_sentence.html", data)
    else:
        return HttpResponseRedirect("/")
