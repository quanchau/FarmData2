from .models import *

admin.site.register(Farm,FarmAdmin)
admin.site.register(Farmer,FarmerAdmin)
admin.site.register(AnimalGroup,AnimalGroupAdmin)
admin.site.register(Breed,BreedAdmin)
admin.site.register(SubGroup,SubGroupAdmin)
admin.site.register(Origin)
admin.site.register(Animal)
admin.site.register(Reason)
admin.site.register(Vet)
admin.site.register(Medication)
admin.site.register(MedsGiven)

admin.site.register(EggLog)
admin.site.register(Wormer)
admin.site.register(SheepCare)
admin.site.register(Forage)
admin.site.register(Paddock)
admin.site.register(Note)
admin.site.register(Destination)
admin.site.register(Sale)
admin.site.register(SlayHouse)
admin.site.register(Slaughter)

admin.site.register(OtherDest)
admin.site.register(OtherReason)
admin.site.register(OtherRemove)
admin.site.register(FeedType)
# admin.site.register(FeedSubtype)
admin.site.register(FeedUnit)
admin.site.register(Vendor)
admin.site.register(FeedPurchase)
admin.site.register(Task)
admin.site.register(TaskMaster)
admin.site.register(TaskRecurring)





