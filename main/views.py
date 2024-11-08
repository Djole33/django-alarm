from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Timer
from datetime import timedelta
from django.conf import settings

def index(request):
    timers = Timer.objects.all()
    alarm_song_url = settings.MEDIA_URL + 'songs/Godzila.mp3'
    if request.method == "POST":
        name = request.POST.get("name")
        seconds = int(request.POST.get("seconds"))
        minutes = int(request.POST.get("minutes"))
        hours = int(request.POST.get("hours"))

        duration_time = timedelta(hours=hours, minutes=minutes, seconds=seconds)

        Timer.objects.create(name=name, duration=duration_time, start_time=timezone.now())

    return render(request, 'main/index.html', {'timers':timers, 'alarm_song_url': alarm_song_url})

def timer_detail(request, timer_id):
    timer = get_object_or_404(Timer, id=timer_id)
    remaining_time = timer.remaining_time()

    # Calculate hours, minutes, and seconds from remaining_time
    total_seconds = int(remaining_time.total_seconds())
    hours = total_seconds // 3600
    minutes = (total_seconds % 3600) // 60
    seconds = total_seconds % 60

    context = {
        'timer': timer,
        'hours': hours,
        'minutes': minutes,
        'seconds': seconds,
        'time_up': timer.is_time_up()
    }
    return render(request, 'main/timer.html', context)