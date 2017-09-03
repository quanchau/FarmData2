from django.conf.urls import url, include
from . import views

app_name = 'farmdb'

urlpatterns = [
    url(r'^login/', views.login_user, name='login'),
    url(r'^$', views.index, name='index'),
    url(r'^logout', views.logout_user, name='logout'),

    # CreateViews
    url(r'^create/AnimalGroup$', views.AnimalGroupCreateView.as_view(), name="AnimalGroupCreate"),
    url(r'^create/Breed$', views.BreedCreateView.as_view(), name="BreedCreate"),
    url(r'^create/AnimalSubGroup$', views.AnimalSubGroupCreateView.as_view(), name="AnimalSubGroupCreate"),
    url(r'^create/Origin$', views.OriginCreateView.as_view(), name="OriginCreate"),
    url(r'^create/Animal$', views.AnimalCreateView.as_view(), name="AnimalCreate"),
    url(r'^create/Reason$', views.ReasonCreateView.as_view(), name="ReasonCreate"),
    url(r'^create/Vet$', views.VetCreateView.as_view(), name="VetCreate"),
    url(r'^create/Medication$', views.MedicationCreateView.as_view(), name="MedicationCreate"),
    url(r'^create/MedsGiven$', views.MedsGivenCreateView.as_view(), name="MedsGivenCreate"),
    url(r'^create/EggLog$', views.EggLogCreateView.as_view(), name="EggLogCreate"),
    url(r'^create/Wormer$', views.WormerCreateView.as_view(), name="WormerCreate"),
    url(r'^create/SheepCare$', views.SheepCareCreateView.as_view(), name="SheepCareCreate"),
    url(r'^create/Forage$', views.ForageCreateView.as_view(), name="ForageCreate"),
    url(r'^create/Paddock$', views.PaddockCreateView.as_view(), name="PaddockCreate"),
    url(r'^create/Note$', views.NoteCreateView.as_view(), name="NoteCreate"),
    url(r'^create/Sale$', views.SaleCreateView.as_view(), name="SaleCreate"),
    url(r'^create/SlayHouse$', views.SlayHouseCreateView.as_view(), name="SlayHouseCreate"),
    url(r'^create/Slaughter$', views.SlaughterCreateView.as_view(), name="SlaughterCreate"),
    url(r'^create/OtherDest$', views.OtherDestCreateView.as_view(), name="OtherDestCreate"),
    url(r'^create/OtherReason$', views.OtherReasonCreateView.as_view(), name="OtherReasonCreate"),
    url(r'^create/OtherRemove$', views.OtherRemoveCreateView.as_view(), name="OtherRemoveCreate"),
    url(r'^create/FeedType$', views.FeedTypeCreateView.as_view(), name="FeedTypeCreate"),
    url(r'^create/FeedUnit$', views.FeedUnitCreateView.as_view(), name="FeedUnitCreate"),
    url(r'^create/FeedSubtype$', views.FeedSubtypeCreateView.as_view(), name="FeedSubtypeCreate"),
    url(r'^create/Vendor$', views.VendorCreateView.as_view(), name="VendorCreate"),
    url(r'^create/FeedPurchase$', views.FeedPurchaseCreateView.as_view(), name="FeedPurchaseCreate"),

    # List views
    url(r'^list/AnimalGroup$', views.AnimalGroupListView.as_view(), name='AnimalGroupList'),

    # DetailViews

    # UpdateViews

    # DeleteViews

    # url(r'^$/', views.index, name='index'),
    # url(r'^$/', views.login_user, name='user_login'),
    # url(r'^$/', views.logout_user, name='user_logout'),

]
