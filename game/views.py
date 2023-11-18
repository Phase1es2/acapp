from django.http import HttpResponse

def index(request):
    line1 = '<h1 style="text-align: center">my first web</h1>'
    line2 = '<img src="https://images-wixmp-ed30a86b8c4ca887773594c2.wixmp.com/f/16839a88-ba93-4b12-a311-eded58cf9f7e/dg0tyb0-1f228fd0-e0ca-4430-9450-2fba89c89dd2.png/v1/fill/w_894,h_894,q_70,strp/warlock_by_alyskan_dg0tyb0-pre.jpg?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ1cm46YXBwOjdlMGQxODg5ODIyNjQzNzNhNWYwZDQxNWVhMGQyNmUwIiwiaXNzIjoidXJuOmFwcDo3ZTBkMTg4OTgyMjY0MzczYTVmMGQ0MTVlYTBkMjZlMCIsIm9iaiI6W1t7ImhlaWdodCI6Ijw9MTAyNCIsInBhdGgiOiJcL2ZcLzE2ODM5YTg4LWJhOTMtNGIxMi1hMzExLWVkZWQ1OGNmOWY3ZVwvZGcwdHliMC0xZjIyOGZkMC1lMGNhLTQ0MzAtOTQ1MC0yZmJhODljODlkZDIucG5nIiwid2lkdGgiOiI8PTEwMjQifV1dLCJhdWQiOlsidXJuOnNlcnZpY2U6aW1hZ2Uub3BlcmF0aW9ucyJdfQ.wgnH8uSLNTSv5ySBaFcVgF8hhhY89QrOOpwYkZqRVQI" width=2000>'
    line3 = '<hr>'
    line4 = '<a href="/play/">Enter</a>'
    return HttpResponse(line1 + line4 + line3 + line2)


def play(request):
    line1 = '<h1>Gmae mode</h1>'
    line2 = '<img src="https://images-wixmp-ed30a86b8c4ca887773594c2.wixmp.com/f/16839a88-ba93-4b12-a311-eded58cf9f7e/dg0tyb0-1f228fd0-e0ca-4430-9450-2fba89c89dd2.png/v1/fill/w_894,h_894,q_70,strp/warlock_by_alyskan_dg0tyb0-pre.jpg?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ1cm46YXBwOjdlMGQxODg5ODIyNjQzNzNhNWYwZDQxNWVhMGQyNmUwIiwiaXNzIjoidXJuOmFwcDo3ZTBkMTg4OTgyMjY0MzczYTVmMGQ0MTVlYTBkMjZlMCIsIm9iaiI6W1t7ImhlaWdodCI6Ijw9MTAyNCIsInBhdGgiOiJcL2ZcLzE2ODM5YTg4LWJhOTMtNGIxMi1hMzExLWVkZWQ1OGNmOWY3ZVwvZGcwdHliMC0xZjIyOGZkMC1lMGNhLTQ0MzAtOTQ1MC0yZmJhODljODlkZDIucG5nIiwid2lkdGgiOiI8PTEwMjQifV1dLCJhdWQiOlsidXJuOnNlcnZpY2U6aW1hZ2Uub3BlcmF0aW9ucyJdfQ.wgnH8uSLNTSv5ySBaFcVgF8hhhY89QrOOpwYkZqRVQI" width=2000>'
    line4 = '<a href="/">Back</a>'
    return HttpResponse(line1 + line4 + line2)
