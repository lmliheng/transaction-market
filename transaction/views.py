from django.shortcuts import render, redirect
from transaction.forms import UserForm, ItemForm, ContactForm
from django.http import HttpResponse
# Create your views here.

from django.shortcuts import render
from .models import Item
from django.contrib.auth.decorators import login_required
from .models import Item, Contact
from .forms import ItemForm, ContactForm
from .models import Contact



from django.shortcuts import get_object_or_404
from django.views.generic import DetailView
from .models import Item



def tra_index(request):
    items =Item.objects.all()
    return render(request, "index.html", {'items':items})
def tra_owner(request):
    return render(request, "owner.html")   


def post_item(request):
    if request.method == 'POST':
        form = ItemForm(request.POST, request.FILES)
        if form.is_valid():
            item = form.save(commit=False)
            item.owner = request.user
            item.save()
            return redirect('/transaction')
    else:
        form = ItemForm()
    return render(request, 'post_item.html', {'form': form})


def edit_contact(request):
    try:
        contact = Contact.objects.get(user=request.user)
    except Contact.DoesNotExist:
        contact = Contact(user=request.user)

    if request.method == 'POST':
        form = ContactForm(request.POST, instance=contact)
        if form.is_valid():
            form.save()
            return redirect('/transaction')
    else:
        form = ContactForm(instance=contact)
    return render(request, 'edit_contact.html', {'form': form})

def personal_page(request):
    contact = Contact.objects.get(user=request.user)
    context = {
        'contact': contact,
    }
    return render(request, 'personal_page.html', context)    



def manage_items(request):
    if request.method == 'POST':
        if 'delete' in request.POST:
            item_id = request.POST.get('item_id')
            Item.objects.filter(id=item_id).delete()
        else:
            form = ItemForm(request.POST)
            if form.is_valid():
                item = form.save(commit=False)
                item.user = request.user
                item.save()
                return redirect('manage_items')
    else:
        form = ItemForm()
    items = Item.objects.filter(owner=request.user)
    return render(request, 'manage_items.html', {'form': form, 'items': items})    

# 使用Django提供的基于类的视图（Class-Based View, CBV）——DetailView，它已经封装了处理单个对象展示的常见逻辑

from django.shortcuts import get_object_or_404
from django.views.generic import DetailView
from .models import Item,Contact


class ItemDetailView(DetailView):
    model = Item
    context_object_name = 'item'
    template_name = 'item_detail.html'

    def get_object(self, queryset=None):
        item_id = self.kwargs.get('pk')
        item = get_object_or_404(Item, pk=item_id)
        return item

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # 假设 Item 模型有一个名为 owner 的外键字段，指向user模型
        user = self.object.owner

        # 通过 user 找到关联的 contact 对象
        contact = get_object_or_404(Contact, user=user)

        # 将 contact 对象添加到上下文中
        context['contact'] = contact

        return context