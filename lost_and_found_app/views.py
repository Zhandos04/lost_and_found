# Create your views here.

from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Item
from .forms import ItemForm
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.admin.views.decorators import staff_member_required
from django.shortcuts import render
from django.contrib.auth.decorators import permission_required
from .models import Item

from django.contrib.auth.mixins import PermissionRequiredMixin
from django.views.generic import ListView
from .models import Item

class ItemManagementView(PermissionRequiredMixin, ListView):
    permission_required = 'lost_and_found_app.change_item'
    model = Item
    template_name = 'item_management.html'
    context_object_name = 'items'

@permission_required('lost_and_found_app.change_item', raise_exception=True)
def item_management(request):
    items = Item.objects.all()
    return render(request, 'item_management.html', {'items': items})


@staff_member_required
def item_moderation(request):
    items = Item.objects.filter(is_approved=False)
    return render(request, 'item_moderation.html', {'items': items})

@staff_member_required
def item_approve(request, item_id):
    item = get_object_or_404(Item, id=item_id)
    item.is_approved = True
    item.save()
    return redirect('item_moderation')

def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('item_list')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('login')


@login_required
def item_list(request):
    query = request.GET.get('q')
    if request.user.is_staff:
        items = Item.objects.all()
    else:
        items = Item.objects.filter(is_approved=True)

    if query:
        items = items.filter(title__istartswith=query)

    return render(request, 'item_list.html', {'items': items})


@login_required
def item_detail(request, item_id):
    item = get_object_or_404(Item, id=item_id)

    recently_viewed = request.session.get('recently_viewed', [])
    if item_id not in recently_viewed:
        recently_viewed.append(item_id)
        if len(recently_viewed) > 5:
            recently_viewed = recently_viewed[-5:]
        request.session['recently_viewed'] = recently_viewed

    return render(request, 'item_detail.html', {'item': item})


@login_required
def item_create(request):
    if request.method == 'POST':
        form = ItemForm(request.POST, request.FILES)
        if form.is_valid():
            item = form.save(commit=False)
            item.user = request.user
            item.save()
            return redirect('item_list')
    else:
        form = ItemForm()
    return render(request, 'item_form.html', {'form': form})


@login_required
def item_update(request, item_id):
    item = get_object_or_404(Item, id=item_id)
    if request.method == 'POST':
        form = ItemForm(request.POST, request.FILES, instance=item)
        if form.is_valid():
            form.save()
            return redirect('item_list')
    else:
        form = ItemForm(instance=item)
    return render(request, 'item_form.html', {'form': form})


@login_required
def item_delete(request, item_id):
    item = get_object_or_404(Item, id=item_id)
    if request.method == 'POST':
        item.delete()
        return redirect('item_list')
    return render(request, 'item_confirm_delete.html', {'item': item})

@login_required
def recently_viewed_items(request):
    viewed_ids = request.session.get('recently_viewed', [])
    items = Item.objects.filter(id__in=viewed_ids) if viewed_ids else []
    items = sorted(items, key=lambda x: viewed_ids.index(x.id), reverse=True)
    return render(request, 'recently_viewed.html', {'items': items})
