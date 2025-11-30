from django.shortcuts import render
from .models import Team


def team_list(request):
    """Отображает список всех активных команд."""
    teams = Team.objects.filter(is_active=True)

    context = {
        'teams': teams,
        'page_title': 'Наши Команды'
    }
    return render(request, 'teams/team_list.html', context)