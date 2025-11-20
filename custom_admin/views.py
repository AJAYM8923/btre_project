
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages, auth
from django.contrib.auth.models import User
from listings.models import Listing
from realtors.models import Realtor
from contacts.models import Contact
from .forms import ListingForm

# Create your views here.
def admin_dashboard(request):
  total_users = User.objects.count()
  total_listings = Listing.objects.count()
  return render(request, 'admin/admin_dashboard.html', {'total_users': total_users, 'total_listings': total_listings})


def admin_users(request):
  users = User.objects.all().order_by('-date_joined')
  return render(request, 'admin/admin_users.html', {'users': users})


def admin_delete_user(request, user_id):
  user = get_object_or_404(User, pk=user_id)
  # Prevent deleting the currently logged-in admin via this interface
  if request.user.is_authenticated and request.user.pk == user.pk:
    messages.error(request, 'You cannot delete the currently logged-in user.')
    return redirect('admin_users')

  if request.method == 'POST':
    user.delete()
    messages.success(request, 'User deleted successfully')
    return redirect('admin_users')

  return render(request, 'admin/admin_confirm_delete_user.html', {'user_obj': user})

def admin_logout(request):
    auth.logout(request)
    messages.success(request, 'Admin logged out successfully')
    return redirect('index')

def admin_listings(request):
  listings = Listing.objects.all().order_by('-list_date')
  return render(request,'admin/admin_listings.html',{'listings': listings})


def admin_add_listing(request):
  if request.method == 'POST':
    form = ListingForm(request.POST, request.FILES)
    if form.is_valid():
      form.save()
      messages.success(request, 'Listing added successfully')
      return redirect('admin_listings')
  else:
    form = ListingForm()

  return render(request, 'admin/admin_add_edit_listing.html', {'form': form, 'action': 'Add'})


def admin_view_listing(request, listing_id):
  listing = get_object_or_404(Listing, pk=listing_id)
  imgs = [
    listing.photo_main,
    listing.photo_1,
    listing.photo_2,
    listing.photo_3,
    listing.photo_4,
    listing.photo_5,
    listing.photo_6,
  ]
  return render(request, 'admin/admin_view_listing.html', {'listing': listing, 'imgs': imgs})


def admin_edit_listing(request, listing_id):
  listing = get_object_or_404(Listing, pk=listing_id)
  if request.method == 'POST':
    form = ListingForm(request.POST, request.FILES, instance=listing)
    if form.is_valid():
      form.save()
      messages.success(request, 'Listing updated successfully')
      return redirect('admin_listings')
  else:
    form = ListingForm(instance=listing)

  return render(request, 'admin/admin_add_edit_listing.html', {'form': form, 'action': 'Edit', 'listing': listing})


def admin_delete_listing(request, listing_id):
  listing = get_object_or_404(Listing, pk=listing_id)
  if request.method == 'POST':
    listing.delete()
    messages.success(request, 'Listing deleted successfully')
    return redirect('admin_listings')

  return render(request, 'admin/admin_confirm_delete.html', {'listing': listing})


def admin_realtors(request):
  realtors = Realtor.objects.all().order_by('-hire_date')
  return render(request, 'admin/admin_realtors.html', {'realtors': realtors})


def admin_add_realtor(request):
  if request.method == 'POST':
    name = request.POST.get('name')
    email = request.POST.get('email')
    phone = request.POST.get('phone')
    description = request.POST.get('description')
    is_mvp = request.POST.get('is_mvp') == 'on'
    photo = request.FILES.get('photo')
    
    realtor = Realtor(
      name=name,
      email=email,
      phone=phone,
      description=description,
      is_mvp=is_mvp,
      photo=photo
    )
    realtor.save()
    messages.success(request, 'Realtor added successfully')
    return redirect('admin_realtors')
  
  return render(request, 'admin/admin_add_realtor.html')


def admin_edit_realtor(request, realtor_id):
  realtor = get_object_or_404(Realtor, pk=realtor_id)
  if request.method == 'POST':
    realtor.name = request.POST.get('name')
    realtor.phone = request.POST.get('phone')
    realtor.email = request.POST.get('email')
    realtor.description = request.POST.get('description')
    realtor.is_mvp = request.POST.get('is_mvp') == 'on'
    
    if 'photo' in request.FILES:
      realtor.photo = request.FILES['photo']
    
    realtor.save()
    messages.success(request, 'Realtor updated successfully')
    return redirect('admin_realtors')
  
  return render(request, 'admin/admin_edit_realtor.html', {'realtor': realtor})


def admin_delete_realtor(request, realtor_id):
  realtor = get_object_or_404(Realtor, pk=realtor_id)
  if request.method == 'POST':
    realtor.delete()
    messages.success(request, 'Realtor deleted successfully')
    return redirect('admin_realtors')

  return render(request, 'admin/admin_confirm_delete_realtor.html', {'realtor': realtor})


def admin_contacts(request):
  contacts = Contact.objects.all().order_by('-contact_date')
  return render(request, 'admin/admin_contacts.html', {'contacts': contacts})