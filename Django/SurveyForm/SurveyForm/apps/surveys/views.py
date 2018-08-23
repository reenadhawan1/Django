from django.shortcuts import render, HttpResponse,redirect


def index(req):
    return render(req,'surveys/index.html')

def submit(req):
    print(req.POST)
    if req.method == "POST":
        req.session['name'] = req.POST['name']
        req.session['location'] = req.POST['location']
        req.session['lang'] = req.POST['language']
        req.session['comment'] = req.POST['comments']
        return redirect('/results')
    else:
        return redirect('/')

def results(req):
    return render(req,'surveys/results.html')