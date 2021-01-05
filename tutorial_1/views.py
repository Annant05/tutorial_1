from django.http import HttpResponse


def indexpage(request):
    return HttpResponse(
        '''Please Select your choice
        <br>
       <button>
        <a href="/register/">  
        For Registration:   
        </a> 
        </button>
        
        <br>
        <button>
        <a href="/display">
        For List of Student
        </a>
        </button>
        
        '''
    )
