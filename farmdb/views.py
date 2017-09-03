from django.shortcuts import render, get_object_or_404, HttpResponse, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.views.generic import CreateView, ListView, DetailView
from django.utils.decorators import method_decorator

from .forms import *
from .models import *


# Create your views here.

@login_required
def index(request):
    return render(request, 'farmdb/index.html')


def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return render(request, 'farmdb/index.html')
            else:
                return render(request, 'farmdb/login.html', {'error_message': 'Your account has been disabled'})
        else:
            return render(request, 'farmdb/login.html', {'error_message': 'Invalid username or password'})
    return render(request, 'farmdb/login.html')


def logout_user(request):
    logout(request)
    return render(request, 'farmdb/login.html', {'logout': 'True'})


def create_farmer(request):
    form = FarmerForm(request.POST or None)
    if form.is_valid():
        user = form.save(commit=False)
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user.set_password(password)
        user.save()
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return HttpResponse("<html><body><h1>Welcome, {}</h1></body></html>".format(user.first_name))
                # Do what needs to be done after a user logs in
    context = {
        "form": form,
    }
    return render(request, 'farmdb/register.html', context)


# CreateViews

@method_decorator(login_required, name='dispatch')
class AnimalGroupCreateView(CreateView):
    template_name = "farmdb/createView/create_animalGroup.html"
    model = AnimalGroup
    fields = ('animalGroup',)
    success_url = '/'

    def form_valid(self, form):
        # Assign the farm from request.user
        form.instance.farm = self.request.user.farmer.farm
        form.instance.active = True
        return super(AnimalGroupCreateView, self).form_valid(form)


@method_decorator(login_required, name='dispatch')
class BreedCreateView(CreateView):
    template_name = "farmdb/createView/create_breed.html"
    model = Breed
    fields = ('breed', 'animalGroup',)
    success_url = '/'

    def form_valid(self, form):
        # Assign the farm from request.user
        form.instance.farm = self.request.user.farmer.farm
        form.instance.active = True
        return super(BreedCreateView, self).form_valid(form)


@method_decorator(login_required, name='dispatch')
class AnimalSubGroupCreateView(CreateView):
    template_name = "farmdb/createView/create_animalSubGroup.html"
    model = AnimalSubGroup
    fields = ('animalSubGroup', 'animalGroup',)
    success_url = '/'

    def form_valid(self, form):
        # Assign the farm from request.user
        form.instance.farm = self.request.user.farmer.farm
        form.instance.active = True
        return super(AnimalSubGroupCreateView, self).form_valid(form)


@method_decorator(login_required, name='dispatch')
class OriginCreateView(CreateView):
    template_name = "farmdb/createView/create_origin.html"
    model = Origin
    fields = ('origin',)
    success_url = '/'

    def form_valid(self, form):
        # Assign the farm from request.user
        form.instance.farm = self.request.user.farmer.farm
        form.instance.active = True
        return super(OriginCreateView, self).form_valid(form)


@method_decorator(login_required, name='dispatch')
class AnimalCreateView(CreateView):
    template_name = "farmdb/createView/create_animal.html"
    model = Animal
    fields = (
    'animalId', 'gender', 'birthDate', 'mother', 'father', 'name', 'markings', 'filename', 'alive', 'comments',
    'animalGroup', 'breed', 'subGroup', 'origin',)
    success_url = '/'

    def form_valid(self, form):
        # Assign the farm from request.user
        form.instance.farm = self.request.user.farmer.farm
        form.instance.active = True
        return super(AnimalCreateView, self).form_valid(form)


@method_decorator(login_required, name='dispatch')
class ReasonCreateView(CreateView):
    template_name = "farmdb/createView/create_reason.html"
    model = Reason
    fields = ('reason')
    success_url = '/'

    def form_valid(self, form):
        # Assign the farm from request.user
        form.instance.farm = self.request.user.farmer.farm
        form.instance.active = True
        return super(ReasonCreateView, self).form_valid(form)


@method_decorator(login_required, name='dispatch')
class VetCreateView(CreateView):
    template_name = "farmdb/createView/create_vet.html"
    model = Vet
    fields = ('careDate', 'animalId',)
    success_url = '/'

    def form_valid(self, form):
        # Assign the farm from request.user
        form.instance.farm = self.request.user.farmer.farm
        form.instance.active = True
        return super(VetCreateView, self).form_valid(form)


@method_decorator(login_required, name='dispatch')
class MedicationCreateView(CreateView):
    template_name = "farmdb/createView/create_medication.html"
    model = Medication
    fields = ('medication', 'dosage')
    success_url = '/'

    def form_valid(self, form):
        # Assign the farm from request.user
        form.instance.farm = self.request.user.farmer.farm
        form.instance.active = True
        return super(MedicationCreateView, self).form_valid(form)


@method_decorator(login_required, name='dispatch')
class MedsGivenCreateView(CreateView):
    template_name = "farmdb/createView/create_medsGiven.html"
    model = MedsGiven
    fields = ('medication', 'units', 'units_given', 'vet_id')
    success_url = '/'

    def form_valid(self, form):
        # Assign the farm from request.user
        form.instance.farm = self.request.user.farmer.farm
        form.instance.active = True
        return super(MedsGivenCreateView, self).form_valid(form)


@method_decorator(login_required, name='dispatch')
class EggLogCreateView(CreateView):
    template_name = "farmdb/createView/create_eggLog.html"
    model = EggLog
    fields = ('collection_date', 'number', 'comments', 'vet_id')
    success_url = '/'

    def form_valid(self, form):
        # Assign the farm from request.user
        form.instance.farm = self.request.user.farmer.farm
        form.instance.active = True
        return super(EggLogCreateView, self).form_valid(form)


@method_decorator(login_required, name='dispatch')
class WormerCreateView(CreateView):
    template_name = "farmdb/createView/create_wormer.html"
    model = Wormer
    fields = ('wormer',)
    success_url = '/'

    def form_valid(self, form):
        # Assign the farm from request.user
        form.instance.farm = self.request.user.farmer.farm
        form.instance.active = True
        return super(WormerCreateView, self).form_valid(form)


@method_decorator(login_required, name='dispatch')
class SheepCareCreateView(CreateView):
    template_name = "farmdb/createView/create_sheepCare.html"
    model = SheepCare
    fields = (
        'care_date', 'animal', 'eye', 'body', 'tail', 'nose', 'coat', 'jaw', 'wormer', 'wormer_quantity', 'hoof',
        'weight', 'estimated', 'comments')
    success_url = '/'

    def form_valid(self, form):
        # Assign the farm from request.user
        form.instance.farm = self.request.user.farmer.farm
        form.instance.active = True
        return super(SheepCareCreateView, self).form_valid(form)


@method_decorator(login_required, name='dispatch')
class ForageCreateView(CreateView):
    template_name = "farmdb/createView/create_forage.html"
    model = Forage
    fields = ('forage', 'density')
    success_url = '/'

    def form_valid(self, form):
        # Assign the farm from request.user
        form.instance.farm = self.request.user.farmer.farm
        form.instance.active = True
        return super(ForageCreateView, self).form_valid(form)


@method_decorator(login_required, name='dispatch')
class PaddockCreateView(CreateView):
    template_name = "farmdb/createView/create_paddock.html"
    model = Paddock
    fields = ('size', 'forage')
    success_url = '/'

    def form_valid(self, form):
        # Assign the farm from request.user
        form.instance.farm = self.request.user.farmer.farm
        form.instance.active = True
        return super(PaddockCreateView, self).form_valid(form)


@method_decorator(login_required, name='dispatch')
class NoteCreateView(CreateView):
    template_name = "farmdb/createView/create_note.html"
    model = Note
    fields = ('note_date', 'note', 'filename')
    success_url = '/'

    def form_valid(self, form):
        # Assign the farm from request.user
        form.instance.farm = self.request.user.farmer.farm
        form.instance.active = True
        form.instance.created_by = self.request.farmer
        return super(NoteCreateView, self).form_valid(form)


@method_decorator(login_required, name='dispatch')
class DestinationCreateView(CreateView):
    template_name = "farmdb/createView/create_destination.html"
    model = Destination
    fields = ('destination')
    success_url = '/'

    def form_valid(self, form):
        # Assign the farm from request.user
        form.instance.farm = self.request.user.farmer.farm
        form.instance.active = True
        return super(DestinationCreateView, self).form_valid(form)


@method_decorator(login_required, name='dispatch')
class SaleCreateView(CreateView):
    template_name = "farmdb/createView/create_sale.html"
    model = Sale
    fields = ('animal', 'saleTag', 'destination', 'weight', 'estimated', 'priceLb', 'fees', 'comments', 'saleDate')
    success_url = '/'

    def form_valid(self, form):
        # Assign the farm from request.user
        form.instance.farm = self.request.user.farmer.farm
        form.instance.active = True
        return super(SaleCreateView, self).form_valid(form)


@method_decorator(login_required, name='dispatch')
class SlayHouseCreateView(CreateView):
    template_name = "farmdb/createView/create_slayHouse.html"
    model = SlayHouse
    fields = ('slayHouse')
    success_url = '/'

    def form_valid(self, form):
        # Assign the farm from request.user
        form.instance.farm = self.request.user.farmer.farm
        form.instance.active = True
        return super(SlayHouseCreateView, self).form_valid(form)


@method_decorator(login_required, name='dispatch')
class SlaughterCreateView(CreateView):
    template_name = "farmdb/createView/create_slaughter.html"
    model = Slaughter
    fields = (
        'animal', 'saleTag', 'slayHouse', 'hauler', 'haulEquip', 'slayDate', 'weight', 'estimated', 'fees', 'comments')
    success_url = '/'

    def form_valid(self, form):
        # Assign the farm from request.user
        form.instance.farm = self.request.user.farmer.farm
        form.instance.active = True
        return super(SlaughterCreateView, self).form_valid(form)


@method_decorator(login_required, name='dispatch')
class OtherDestCreateView(CreateView):
    template_name = "farmdb/createView/create_otherDest.html"
    model = OtherDest
    fields = ('dest',)
    success_url = '/'

    def form_valid(self, form):
        # Assign the farm from request.user
        form.instance.farm = self.request.user.farmer.farm
        form.instance.active = True
        return super(OtherDestCreateView, self).form_valid(form)


@method_decorator(login_required, name='dispatch')
class OtherReasonCreateView(CreateView):
    template_name = "farmdb/createView/create_otherReason.html"
    model = OtherReason
    fields = ('reason',)
    success_url = '/'

    def form_valid(self, form):
        # Assign the farm from request.user
        form.instance.farm = self.request.user.farmer.farm
        form.instance.active = True
        return super(OtherReasonCreateView, self).form_valid(form)


@method_decorator(login_required, name='dispatch')
class OtherRemoveCreateView(CreateView):
    template_name = "farmdb/createView/create_otherRemove.html"
    model = OtherRemove
    fields = ('animal', 'removeDate', 'reason', 'destination', 'weight', 'comments',)
    success_url = '/'

    def form_valid(self, form):
        # Assign the farm from request.user
        form.instance.farm = self.request.user.farmer.farm
        form.instance.active = True
        return super(OtherRemoveCreateView, self).form_valid(form)


@method_decorator(login_required, name='dispatch')
class FeedTypeCreateView(CreateView):
    template_name = "farmdb/createView/create_feedType.html"
    model = FeedType
    fields = ('type',)
    success_url = '/'

    def form_valid(self, form):
        # Assign the farm from request.user
        form.instance.farm = self.request.user.farmer.farm
        form.instance.active = True
        return super(FeedTypeCreateView, self).form_valid(form)


@method_decorator(login_required, name='dispatch')
class FeedUnitCreateView(CreateView):
    template_name = "farmdb/createView/create_feedUnit.html"
    model = FeedUnit
    fields = ('unit',)
    success_url = '/'

    def form_valid(self, form):
        # Assign the farm from request.user
        form.instance.farm = self.request.user.farmer.farm
        form.instance.active = True
        return super(FeedUnitCreateView, self).form_valid(form)


@method_decorator(login_required, name='dispatch')
class FeedSubtypeCreateView(CreateView):
    template_name = "farmdb/createView/create_feedSubtype.html"
    model = FeedSubtype
    fields = ('type', 'subtype',)
    success_url = '/'

    def form_valid(self, form):
        # Assign the farm from request.user
        form.instance.farm = self.request.user.farmer.farm
        form.instance.active = True
        return super(FeedSubtypeCreateView, self).form_valid(form)


@method_decorator(login_required, name='dispatch')
class VendorCreateView(CreateView):
    template_name = "farmdb/createView/create_vendor.html"
    model = Vendor
    fields = ('vendor',)
    success_url = '/'

    def form_valid(self, form):
        # Assign the farm from request.user
        form.instance.farm = self.request.user.farmer.farm
        form.instance.active = True
        return super(VendorCreateView, self).form_valid(form)


@method_decorator(login_required, name='dispatch')
class FeedPurchaseCreateView(CreateView):
    template_name = "farmdb/createView/create_feedPurchase.html"
    model = FeedPurchase
    fields = ('purchaseDate', 'type', 'subtype', 'animalGroup', 'vendor', 'units', 'priceUnit', 'weightUnit',)
    success_url = '/'

    def form_valid(self, form):
        # Assign the farm from request.user
        form.instance.farm = self.request.user.farmer.farm
        form.instance.active = True
        return super(FeedPurchaseCreateView, self).form_valid(form)

# ListViews


@method_decorator(login_required, name='dispatch')
class AnimalGroupListView(ListView):
    model = AnimalGroup
    template_name = 'farmdb/listView/animalGroup_list.html'

    def get_queryset(self):
        return AnimalGroup.objects.filter(farm=self.request.user.farmer.farm)


@method_decorator(login_required, name='dispatch')
class BreedListView(ListView):
    model = Breed
    template_name = 'farmdb/listView/breed_list.html'

    def get_queryset(self):
        return Breed.objects.filter(frm=self.request.user.farmer.farm)


@method_decorator(login_required, name='dispatch')
class SubGroupListView(ListView):
    model = AnimalSubGroup
    template_name = 'farmdb/listView/animalSubGroup_list.html'

    def get_queryset(self):
        return AnimalSubGroup.objects.filter(frm=self.request.user.farmer.farm)


@method_decorator(login_required, name='dispatch')
class OriginListView(ListView):
    model = Origin
    template_name = 'farmdb/listView/origin_list.html'

    def get_queryset(self):
        return Origin.objects.filter(frm=self.request.user.farmer.farm)


@method_decorator(login_required, name='dispatch')
class AnimalListView(ListView):
    model = Animal
    template_name = 'farmdb/listView/animal_list.html'

    def get_queryset(self):
        return Animal.objects.filter(frm=self.request.user.farmer.farm)


@method_decorator(login_required, name='dispatch')
class ReasonListView(ListView):
    model = Reason
    template_name = 'farmdb/listView/reason_list.html'

    def get_queryset(self):
        return Reason.objects.filter(frm=self.request.user.farmer.farm)


@method_decorator(login_required, name='dispatch')
class VetListView(ListView):
    model = Vet
    template_name = 'farmdb/listView/vet_list.html'

    def get_queryset(self):
        return Vet.objects.filter(frm=self.request.user.farmer.farm)


@method_decorator(login_required, name='dispatch')
class MedicationListView(ListView):
    model = Medication
    template_name = 'farmdb/listView/medication_list.html'

    def get_queryset(self):
        return Medication.objects.filter(frm=self.request.user.farmer.farm)


@method_decorator(login_required, name='dispatch')
class MedsGivenListView(ListView):
    model = MedsGiven
    template_name = 'farmdb/listView/medsGiven_list.html'

    def get_queryset(self):
        return MedsGiven.objects.filter(frm=self.request.user.farmer.farm)


@method_decorator(login_required, name='dispatch')
class EggLogListView(ListView):
    model = EggLog
    template_name = 'farmdb/listView/eggLog_list.html'

    def get_queryset(self):
        return EggLog.objects.filter(frm=self.request.user.farmer.farm)


@method_decorator(login_required, name='dispatch')
class WormerListView(ListView):
    model = Wormer
    template_name = 'farmdb/listView/wormer_list.html'

    def get_queryset(self):
        return Wormer.objects.filter(frm=self.request.user.farmer.farm)


@method_decorator(login_required, name='dispatch')
class SheepCareListView(ListView):
    model = SheepCare
    template_name = 'farmdb/listView/sheepCare_list.html'

    def get_queryset(self):
        return SheepCare.objects.filter(frm=self.request.user.farmer.farm)


@method_decorator(login_required, name='dispatch')
class ForageListView(ListView):
    model = Forage
    template_name = 'farmdb/listView/forage_list.html'

    def get_queryset(self):
        return Forage.objects.filter(frm=self.request.user.farmer.farm)


@method_decorator(login_required, name='dispatch')
class PaddockListView(ListView):
    model = Paddock
    template_name = 'farmdb/listView/paddock_list.html'

    def get_queryset(self):
        return Paddock.objects.filter(frm=self.request.user.farmer.farm)


@method_decorator(login_required, name='dispatch')
class NoteListView(ListView):
    model = Note
    template_name = 'farmdb/listView/note_list.html'

    def get_queryset(self):
        return Note.objects.filter(frm=self.request.user.farmer.farm)


@method_decorator(login_required, name='dispatch')
class DestinationListView(ListView):
    model = Destination
    template_name = 'farmdb/listView/destination_list.html'

    def get_queryset(self):
        return Destination.objects.filter(frm=self.request.user.farmer.farm)


@method_decorator(login_required, name='dispatch')
class SaleListView(ListView):
    model = Sale
    template_name = 'farmdb/listView/sale_list.html'

    def get_queryset(self):
        return Sale.objects.filter(frm=self.request.user.farmer.farm)


@method_decorator(login_required, name='dispatch')
class SlayHouseListView(ListView):
    model = SlayHouse
    template_name = 'farmdb/listView/slayHouse_list.html'

    def get_queryset(self):
        return SlayHouse.objects.filter(frm=self.request.user.farmer.farm)


@method_decorator(login_required, name='dispatch')
class SlaughterListView(ListView):
    model = Slaughter
    template_name = 'farmdb/listView/slaughter_list.html'

    def get_queryset(self):
        return Slaughter.objects.filter(frm=self.request.user.farmer.farm)


@method_decorator(login_required, name='dispatch')
class OtherDestListView(ListView):
    model = OtherDest
    template_name = 'farmdb/listView/otherDest_list.html'

    def get_queryset(self):
        return OtherDest.objects.filter(frm=self.request.user.farmer.farm)


@method_decorator(login_required, name='dispatch')
class OtherReasonListView(ListView):
    model = OtherReason
    template_name = 'farmdb/listView/otherReason_list.html'

    def get_queryset(self):
        return OtherReason.objects.filter(frm=self.request.user.farmer.farm)


@method_decorator(login_required, name='dispatch')
class OtherRemoveListView(ListView):
    model = OtherRemove
    template_name = 'farmdb/listView/otherRemove_list.html'

    def get_queryset(self):
        return OtherRemove.objects.filter(frm=self.request.user.farmer.farm)


@method_decorator(login_required, name='dispatch')
class FeedTypeListView(ListView):
    model = FeedType
    template_name = 'farmdb/listView/feedType_list.html'

    def get_queryset(self):
        return FeedType.objects.filter(frm=self.request.user.farmer.farm)


@method_decorator(login_required, name='dispatch')
class FeedSubtypeListView(ListView):
    model = FeedSubtype
    template_name = 'farmdb/listView/feedSubtype_list.html'

    def get_queryset(self):
        return FeedSubtype.objects.filter(frm=self.request.user.farmer.farm)


@method_decorator(login_required, name='dispatch')
class FeedUnitListView(ListView):
    model = FeedUnit
    template_name = 'farmdb/listView/feedUnit_list.html'

    def get_queryset(self):
        return FeedUnit.objects.filter(frm=self.request.user.farmer.farm)


@method_decorator(login_required, name='dispatch')
class VendorListView(ListView):
    model = Vendor
    template_name = 'farmdb/listView/vendor_list.html'

    def get_queryset(self):
        return Vendor.objects.filter(frm=self.request.user.farmer.farm)


@method_decorator(login_required, name='dispatch')
class FeedPurchaseListView(ListView):
    model = FeedPurchase
    template_name = 'farmdb/listView/feedPurchase_list.html'

    def get_queryset(self):
        return FeedPurchase.objects.filter(frm=self.request.user.farmer.farm)

