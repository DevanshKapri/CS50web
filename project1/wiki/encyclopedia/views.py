from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.http import HttpResponse
from markdown2 import markdown
from django.contrib import messages
from django.urls import reverse
from random import choice

from encyclopedia.forms import PostForm, EditForm

from . import util

def index(request):
    
    if request.method == "GET":
        return render(request, "encyclopedia/index.html", {
            "entries": util.list_entries(),
            "heading": "All Pages",
        })
    else :
        title = request.POST["q"]
        query = util.search_title(title)
        print(query)

        if len(query) == 1 and query[0].lower() == title.lower():
            return entry(request, query[0])
        else :
            return render(request, "encyclopedia/index.html", {
                "entries": query,
                "heading": "Search Results", 
            })

def entry(request, title):
    content = util.get_entry(title.strip())
    if content == None:
        content = "## Page was not found"
    content = markdown(content)
    return render(request, "encyclopedia/entry.html", {'content': content, 'title': title})

def create(request):
    if request.method == "GET":
        form = PostForm()
        return render(request, "encyclopedia/post.html", {'form' : form} )
    else:
        form = PostForm(request.POST)

        if form.is_valid():
            title = form.cleaned_data["title"]
            entries = util.list_entries()
            for filename in entries:
                if title.lower() == filename.lower():
                    messages.warning(request, 'Entry already exists!')
                    return HttpResponseRedirect(reverse("create"))
            body = form.cleaned_data["text"]
            util.save_entry(title,body)
            return entry(request, title)

def edit(request, title):
    if request.method == 'GET':
        content = util.get_entry(title)
        
        context = {
            'edit': EditForm(initial={'text': content}),
            'title': title
        }

        return render(request, "encyclopedia/edit.html", context)
    else:
        form = EditForm(request.POST) 
        if form.is_valid():
            textarea = form.cleaned_data["text"]
            util.save_entry(title,textarea)
            return entry(request, title)
            
def random_page(request):
    entries = util.list_entries()
    title = choice(entries)
    return entry(request, title)

