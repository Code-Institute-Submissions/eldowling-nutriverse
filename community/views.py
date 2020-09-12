from django.shortcuts import (
    render, redirect, reverse, get_object_or_404, HttpResponse
)
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView
from .forms import DiscussionsForm
from .models import Discussions
from profiles.models import UserProfile
from products.models import Product


class Discussions_List(ListView):
    """Create a listview of all Discussions"""
    template_name = 'community/discussions_list.html'
    queryset = Discussions.objects.all()


@login_required
def add_discussion_topic(request):
    """ Add a new discussion topic for a product """

    if request.method == 'POST':
        if request.user.is_authenticated:
            profile = UserProfile.objects.get(user=request.user)

            form_data = {
                'product': request.POST['product'],
                'topic': request.POST['topic'],
                'disc_topic_text': request.POST['disc_topic_text'],
            }
            
            discussion_form = DiscussionsForm(form_data)
            if discussion_form.is_valid():
                discussion_object = discussion_form.save(commit=False)
                discussion_object.user_profile = profile
                discussion_form.save()

                return redirect('discussions_list')
            else:
                messages.error(request, 'There is an error on the form. \
                    Please review the details entered')
    else:
        discussion_form = DiscussionsForm()

    template = 'community/add_discussion.html'
    context = {
        'form': discussion_form,
    }

    return render(request, template, context)


@login_required
def edit_discussion(request, product_id):
    """ Edit the selected discussion topic for a product """

    if request.method == 'POST':
        if request.user.is_authenticated:
            try:
                discussion = get_object_or_404(Product, pk=discussion_id)
                form_data = DiscussionsForm(initial={
                    'topic': request.POST['topic'],
                    'disc_topic_text': request.POST['disc_topic_text'],
                })
            except UserProfile.DoesNotExist:
                discussion_form = DiscussionsForm()

        discussion_form = DiscussionsForm(form_data)
        if discussion_form.is_valid():
            discussion_form.save()
            # update with discussion id
        else:
            messages.error(request, 'There is an error on the form. \
                Please review the details entered')
    else:
        discussion_form = DiscussionsForm(instance=discussion)

    template = 'community/edit_discussion.html'
    context = {
        'form': discussion_form,
    }

    return render(request, template, context)


def view_topic(request, discussion_id):
    """A view to display the discussion details for the selected topic"""

    discussion = get_object_or_404(Discussions, pk=discussion_id)

    template = 'community/view_discussion.html'
    context = {
        'discussion': discussion,
    }

    return render(request, template, context)
