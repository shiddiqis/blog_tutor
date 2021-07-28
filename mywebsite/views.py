

from django.shortcuts import render
   
def index(request):
     context = {
        'namaku' : 'Shiddiqis salamil latief',
        'emailku' : 'sejatigamers888@gmail.com',
        'nav':[
           ['/','MENU'],
           ['/blog','BLOG'],
           ['/about','ABOUT'],
        ]
        }
     return render(request,'index.html', context)

