from django.shortcuts import render
import sys
from pathlib import Path
from subprocess import run,PIPE


#For renderting the HTML page
def button(request):
    return render(request,'home.html')

#For displaying the output once the button is clicked
def output(request):
    #It's the current file location
    HERE = Path(__file__).parent
    sys.path.append(str(HERE / '../../'))
    #Importing the main() function
    from main import func
    search = func()
    if 'c0' not in search.payload[0].display_name:
        search = 'Distracted!'
    else:
        search = 'Not Distracted'

    return render(request,'home.html',{'search': search})

def external(request):
    HERE = Path(__file__).parent
    sys.path.append(str(HERE / '../../'))
    from main import call_drowsy
    call_drowsy()
    return render(request,'home.html')
