from django.http import HttpResponse
from django.shortcuts import render


def homepage(request):
    return render(request, "home.html")


def title(request):
    djtext = request.GET.get("text", "default")
    newvalue = str(djtext).title()
    return HttpResponse('''{} <button onclick="window.location.href='/'">Back</button> '''.format(newvalue))


def lower(request):
    return HttpResponse("Lower")


def analize(request):
    textvalue = request.GET.get('text', 'default')
    punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    newtext = ''
    checkbox = request.GET.get('check', 'default')
    upper = request.GET.get('upper', 'default')
    lowercase = request.GET.get('lower', 'default')
    space = request.GET.get('space', 'default')
    length = request.GET.get('length', 'default')
    char = request.GET.get('char', 'default')
    purpose = " "

    if checkbox == 'on':
        newtext = ''
        for char in textvalue:
            if char not in punctuations:
                newtext = newtext + char
            elif char == '\n':
                newtext = newtext + char
        purpose = "Remove punctuations"
        params = {'Newvalue': newtext, 'Type': purpose}
        textvalue = newtext
    if upper == 'on':
        newtext = ''
        newtext = textvalue.upper()
        purpose += ' Uppercase'
        params = {'Newvalue': newtext, 'Type': purpose}
        textvalue = newtext

    if lowercase == 'on':
        newtext = ''

        newtext = textvalue.lower()
        purpose += ' Lowercase'
        params = {'Newvalue': newtext, 'Type': purpose}
        textvalue = newtext

    if space == 'on':
        newtext = ''
        for index, char in enumerate(textvalue):
            if not (textvalue[index] == ' ' and textvalue[index + 1] == ' '):
                newtext = newtext + char
        purpose += ' Remove spaces'
        params = {'Newvalue': newtext, 'Type': purpose}
        textvalue = newtext

    if length == 'on':
        newtext = ''
        newtext = 'The length of the string is ' + str(len(textvalue))
        params = {'Newvalue': newtext, 'Type': "Total length"}
        textvalue = newtext

    if char == 'on':
        newtext = ''
        count = 0
        for index, item in enumerate(textvalue):
            if not (textvalue[index] == ' '):
                count = count + 1
        newtext = count
        params = {'Newvalue': newtext, 'Type': "words count"}
        textvalue = newtext

    if (checkbox != 'on' and upper != 'on' and lowercase != 'on' and space != 'on' and char != 'on' and length != 'on'):
        return HttpResponse("Something Went wrong Please try again")

    return render(request, 'remove.html', params)
