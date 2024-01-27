from django.shortcuts import render, redirect, get_object_or_404

# Create your views here.
from .models import TodoData


def home(request): 
        if request.method == 'POST': 
                
                headline = request.POST.get('headline')
                text = request.POST.get('text')
                TodoData.objects.create(headline=headline, text=text)
                return redirect('home')      
          
        todos = TodoData.objects.all()
        return render(request, 'app/home.html', {'todos' : todos})


def update_todo(request, todo_id):
        todo = get_object_or_404(TodoData, id=todo_id)
         
        if request.method == 'POST': 
                todo.headline = request.POST.get('headline')
                todo.text = request.POST.get('text')
                todo.status = False 
                todo.save()
                return redirect('home')
        
        return render(request, 'app/update_todo.html', {'todo' : todo})

def change_todo_status(request, todo_id, status): 
        todo = get_object_or_404(TodoData, id=todo_id)
        
        if status == 'done': # this time, todo.status is False 
                todo.status = True 
        else: # status == 'undone'
                todo.status = False 
                
        todo.save()
        return redirect('home')

def delete_todo(request, todo_id): 
        todo = get_object_or_404(TodoData, id=todo_id)
        todo.delete()
        return redirect('home')
        
                


# def process_from_data(request): 
#         if request.method == 'POST': 
#                 headline = request.POST.get('headline')
#                 text = request.POST.get('text')
#                 TodoData.objects.create(headline=headline, text=text)
#                 return redirect('home')        
#         return redirect('home')



