from django.shortcuts import render,redirect
from time import time, strftime

def index(req):
    return render(req,'session_words/index.html')

def add(req):
    now = strftime('%b %d %Y %H:%M:%S')
    print(now)
    if 'activity' not in req.session:
        req.session['activity'] = []
    if 'big' in req.POST:
        req.session['activity'] = req.session['activity'] + [f'<p class="{req.POST["color"]} {req.POST["big"]}">{req.POST["word"]}<span> -- {now}</span></p>']
    else:
        req.session['activity'] = req.session['activity'] + [f'<p class="{req.POST["color"]}">{req.POST["word"]}<span>-- {now}</span></p>']
    
    print(req.session['activity'])
    return redirect('/sess/words')

def clear(req):
    req.session.flush()
    return redirect('/sess/words')