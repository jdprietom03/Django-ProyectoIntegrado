from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from .models import TodoItem
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
first_time = True

# Create your views here.
@csrf_exempt
def todoView(request):
  global first_time
  all_todo_items = TodoItem.objects.all()
  if (first_time):
      new_item = TodoItem(content = "build a cool app on replit.com")
      new_item.save()
      first_time = False
  return render(request, 'index.html', 
  {'all_items': all_todo_items})
	
@csrf_exempt
def addTodo(request):
  new_item = TodoItem(content = request.POST['content'])
  new_item.save()
  return HttpResponseRedirect('/')

@csrf_exempt
def deleteTodo(request, todo_id):
  item_to_delete = TodoItem.objects.get(id=todo_id)
  item_to_delete.delete()
  return HttpResponseRedirect('/')

@csrf_exempt
def coverImage(request):
    image_data = open("./todo/app.png", "rb").read()
    return HttpResponse(image_data, content_type="image/png")