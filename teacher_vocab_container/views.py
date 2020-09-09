# Main Imports

# Django Imports
from django.shortcuts import render, get_object_or_404, HttpResponse
from django.http import HttpResponseRedirect
from django.core.exceptions import ObjectDoesNotExist
from django.core.files import File
from django.contrib.auth.models import User

# My Module Imports
from profile_settings.models import BasicUserProfile
from teacher_authentication.models import TeacherUserProfile
from .models import TeacherVocabularyContainer
from utils.session_utils import get_current_user, get_current_user_profile
from utils.session_utils import get_current_teacher_user_profile


def teacher_vocab_container_overview(request):
    """
    in this view the teachers can create the vocabulary packs
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

    # Listing all of the words in tables
    # A0
    try:
        a0_word_list = TeacherVocabularyContainer.objects.filter(
            course=current_teacher_profile.teacher_course, level="a0"
        ).order_by("id")
    except ObjectDoesNotExist:
        a0_word_list = None

    # A0 words id count such as 1, 2, 3, 4 ... 100 .. etc.
    a0_word_count = {}
    count = 0
    for word in a0_word_list:
        count += 1
        a0_word_count[word.id] = count

    # A1
    try:
        a1_word_list = TeacherVocabularyContainer.objects.filter(
            course=current_teacher_profile.teacher_course, level="a1"
        ).order_by("id")
    except ObjectDoesNotExist:
        a1_word_list = None

    # A1 words id count such as 1, 2, 3, 4 ... 100 .. etc.
    a1_word_count = {}
    count = 0
    for word in a1_word_list:
        count += 1
        a1_word_count[word.id] = count

    # A2
    try:
        a2_word_list = TeacherVocabularyContainer.objects.filter(
            course=current_teacher_profile.teacher_course, level="a2"
        ).order_by("id")
    except ObjectDoesNotExist:
        a2_word_list = None

    # A1 words id count such as 1, 2, 3, 4 ... 100 .. etc.
    a2_word_count = {}
    count = 0
    for word in a2_word_list:
        count += 1
        a2_word_count[word.id] = count

    # B1
    try:
        b1_word_list = TeacherVocabularyContainer.objects.filter(
            course=current_teacher_profile.teacher_course, level="b1"
        ).order_by("id")
    except ObjectDoesNotExist:
        b1_word_list = None

    # A1 words id count such as 1, 2, 3, 4 ... 100 .. etc.
    b1_word_count = {}
    count = 0
    for word in b1_word_list:
        count += 1
        b1_word_count[word.id] = count

    # B2
    try:
        b2_word_list = TeacherVocabularyContainer.objects.filter(
            course=current_teacher_profile.teacher_course, level="b2"
        ).order_by("id")
    except ObjectDoesNotExist:
        b2_word_list = None

    b2_word_count = {}
    count = 0
    for word in b2_word_list:
        count += 1
        b2_word_count[word.id] = count

    # C1
    try:
        c1_word_list = TeacherVocabularyContainer.objects.filter(
            course=current_teacher_profile.teacher_course, level="c1"
        ).order_by("id")
    except ObjectDoesNotExist:
        c1_word_list = None

    c1_word_count = {}
    count = 0
    for word in c1_word_list:
        count += 1
        c1_word_count[word.id] = count

    # Advanced
    try:
        advanced_word_list = TeacherVocabularyContainer.objects.filter(
            course=current_teacher_profile.teacher_course, level="advanced"
        ).order_by("id")
    except ObjectDoesNotExist:
        advanced_word_list = None

    advanced_word_count = {}
    count = 0
    for word in advanced_word_list:
        count += 1
        advanced_word_count[word.id] = count

    # vocab add A0 processing
    a0_limit_reached = False

    if request.POST.get("teacher_word_add_a0_submit"):
        word = request.POST.get("word")
        # check if a0 list has 100 words
        if len(a0_word_list) > 100:
            a0_limit_reached = True
        else:
            new_word_record = TeacherVocabularyContainer(
                course=current_teacher_profile.teacher_course,
                teacher=current_teacher_profile,
                word=word,
                level="a0"
            )
            new_word_record.save()
            return HttpResponseRedirect("/teacher/vocab/container/overview/")

    # vocab add A1 processing
    a1_limit_reached = False

    if request.POST.get("teacher_word_add_a1_submit"):
        word = request.POST.get("word")
        # check if a1 list has 500 words
        if len(a1_word_list) > 500:
            a1_limit_reached = True
        else:
            new_word_record = TeacherVocabularyContainer(
                course=current_teacher_profile.teacher_course,
                teacher=current_teacher_profile,
                word=word,
                level="a1"
            )
            new_word_record.save()
            return HttpResponseRedirect("/teacher/vocab/container/overview/")

    # vocab add A2 processing
    a2_limit_reached = False

    if request.POST.get("teacher_word_add_a2_submit"):
        word = request.POST.get("word")
        # check if a2 list has 1000 words
        if len(a2_word_list) > 1000:
            a2_limit_reached = True
        else:
            new_word_record = TeacherVocabularyContainer(
                course=current_teacher_profile.teacher_course,
                teacher=current_teacher_profile,
                word=word,
                level="a2"
            )
            new_word_record.save()
            return HttpResponseRedirect("/teacher/vocab/container/overview/")

    # vocab add B1 processing
    b1_limit_reached = False

    if request.POST.get("teacher_word_add_b1_submit"):
        word = request.POST.get("word")
        # check if b1 list has 2000 words
        if len(b1_word_list) > 2000:
            b1_limit_reached = True
        else:
            new_word_record = TeacherVocabularyContainer(
                course=current_teacher_profile.teacher_course,
                teacher=current_teacher_profile,
                word=word,
                level="b1"
            )
            new_word_record.save()
            return HttpResponseRedirect("/teacher/vocab/container/overview/")

    # vocab add B2 processing
    b2_limit_reached = False

    if request.POST.get("teacher_word_add_b2_submit"):
        word = request.POST.get("word")
        # check if b2 list has 4000 words
        if len(b2_word_list) > 4000:
            b2_limit_reached = True
        else:
            new_word_record = TeacherVocabularyContainer(
                course=current_teacher_profile.teacher_course,
                teacher=current_teacher_profile,
                word=word,
                level="b2"
            )
            new_word_record.save()
            return HttpResponseRedirect("/teacher/vocab/container/overview/")

    # vocab add C1 processing
    c1_limit_reached = False

    if request.POST.get("teacher_word_add_c1_submit"):
        word = request.POST.get("word")
        # check if c1 list has 8000 words
        if len(c1_word_list) > 8000:
            c1_limit_reached = True
        else:
            new_word_record = TeacherVocabularyContainer(
                course=current_teacher_profile.teacher_course,
                teacher=current_teacher_profile,
                word=word,
                level="c1"
            )
            new_word_record.save()
            return HttpResponseRedirect("/teacher/vocab/container/overview/")

    # vocab add Advanced processing
    advanced_limit_reached = False

    if request.POST.get("teacher_word_add_advanced_submit"):
        word = request.POST.get("word")
        # check if advanced list has 16000 words
        if len(c1_word_list) > 16000:
            advanced_limit_reached = True
        else:
            new_word_record = TeacherVocabularyContainer(
                course=current_teacher_profile.teacher_course,
                teacher=current_teacher_profile,
                word=word,
                level="advanced"
            )
            new_word_record.save()
            return HttpResponseRedirect("/teacher/vocab/container/overview/")

    # vocab update form processing

    data = {
        "current_basic_user": current_basic_user,
        "current_basic_user_profile": current_basic_user_profile,
        "current_teacher_profile": current_teacher_profile,
        "a0_word_list": a0_word_list,
        "a0_word_count": a0_word_count,
        "a1_word_list": a1_word_list,
        "a1_word_count": a1_word_count,
        "a2_word_list": a2_word_list,
        "a2_word_count": a2_word_count,
        "b1_word_list": b1_word_list,
        "b1_word_count": b1_word_count,
        "b2_word_list": b2_word_list,
        "b2_word_count": b2_word_count,
        "c1_word_list": c1_word_list,
        "c1_word_count": c1_word_count,
        "advanced_word_list": advanced_word_list,
        "advanced_word_count": advanced_word_count,
        "a0_limit_reached": a0_limit_reached,
        "a1_limit_reached": a1_limit_reached,
        "a2_limit_reached": a2_limit_reached,
        "b1_limit_reached": b1_limit_reached,
        "b2_limit_reached": b2_limit_reached,
        "c1_limit_reached": c1_limit_reached,
        "advanced_limit_reached": advanced_limit_reached,
    }

    if "teacher_user_logged_in" in request.session:
        return render(request, "teacher_vocab_container/overview.html", data)
    else:
        return HttpResponseRedirect("/")
