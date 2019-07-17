from django.contrib import messages
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.template.response import TemplateResponse
from django.db import transaction
from django.utils.translation import ugettext_lazy as _
from django.urls import reverse
from django.shortcuts import get_object_or_404, redirect, render

from imagetagger.abml.forms import ABMLExperimentCreationForm
from imagetagger.abml.models import ABMLExperiment
from imagetagger.images.models import ImageSet
from imagetagger.users.models import User, Team


# Create your views here.

@login_required
def index(request):
    # needed to show the list of the users imagesets
    userteams = Team.objects.filter(members=request.user)

    abml_experiments = ABMLExperiment.objects.filter(team__in=userteams) \
                                     .order_by('-time')

    return TemplateResponse(request, 'abml/index.html', {
        'abml_experiments': abml_experiments
    })

@login_required
def create_abmlexperiment(request):
    # team = get_object_or_404(Team, id=request.POST['team'])
    # image_set = get_object_or_404(ImageSet, id=request.POST['image_set'])
    form = ABMLExperimentCreationForm()

    if request.method == 'POST':
        form = ABMLExperimentCreationForm(request.POST)

        if form.is_valid():
            team = form.instance.image_set.team

        # if not team.has_perm('', request.user):
            # messages.warning(
                # request,
                # _('You do not have permission to create image sets in the team {}.')
                # .format(team.name))
            # return redirect(reverse('users:team', args=(team.id,)))
            with transaction.atomic():
                form.instance.team = team
                form.instance.creator = request.user
                form.instance.save()

            messages.success(request,
                                _('The ABML experiment was created successfully.'))
            return redirect(reverse('abml:index',
                                    ))

    return render(request, 'abml/create_abmlexperiment.html', {
        'form': form
    })
