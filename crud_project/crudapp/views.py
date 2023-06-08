from django.shortcuts import get_object_or_404, render, redirect
from .forms import ItemForm
from .models import Item 
from django .contrib import messages
from django.views.generic import ListView
# class ItemlistView(ListView):
#     model = Item
#     template_name='home.html' 

# Create your views here.
# def demo(request):
#     return render(request,'index.html')
def create(request):
    item1 = Item.objects.all()
    if request.method == 'POST':
        sl_no = request.POST.get('sl_no','')
        item_name = request.POST.get('item_name','')
        description = request.POST.get('description','')
        item = Item(sl_no=sl_no,item_name=item_name,description=description)
        item.save()
        messages.success(request, "Data saved Succesfully")
    return render(request,'home.html',{'item1':item1})
def update(request, id):
    contact1 = Item.objects.all()
    contact = Item.objects.get(id=id)

    if request.method == 'POST':
        sl_no = request.POST.get('sl_no', '')
        item_name = request.POST.get('item_name', '')
        description = request.POST.get('description', '')

        contact.sl_no = sl_no
        contact.item_name = item_name
        contact.description = description
        contact.save()
        messages.success(request, "Data saved Succesfully")
        return redirect('/')
    
    return render(request, 'update.html', {'contact1': contact1, 'contact': contact})
# def update(request, id):
#     item = get_object_or_404(Item, id=id)
#     if request.method == 'POST':
#         item.sl_no=request.POST.get('sl_no','')
#         item.item_name = request.POST.get('item_name','')
#         item.description = request.POST.get('description','')
#         # Update more fields as needed
#         item.save()
#         messages.info(request, "UPDATED SUCCESSFULLY!")
#         return redirect('/')
#     return render(request, 'update.html',{'item':item})
# def update(request,id):
#     item = Item.objects.get(id=id)
    # f = ItemForm(request.POST or None, instance=item)
    # if f.is_valid():
    #     f.save()
    #     return redirect('/')
    # return render(request, 'update.html',{'f': f,'item':item})
def delete(request, taskid):
    item1 = Item.objects.get(id=taskid)
    if request.method == 'POST':
        item1.delete()
        return redirect('/')
    return render(request, 'delete.html')


