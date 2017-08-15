from django.contrib import admin
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
admin.site.register(Meds_given)

admin.site.register(Egg_Log)
admin.site.register(Wormer)
admin.site.register(Sheep_care)
admin.site.register(Forage)
admin.site.register(Paddock)
admin.site.register(Note)
admin.site.register(Destination)
admin.site.register(Sale)
admin.site.register(Slay_House)
admin.site.register(Slaughter)

admin.site.register(Other_Dest)
admin.site.register(Other_Reason)
admin.site.register(Other_Remove)
admin.site.register(Feed_Type)
admin.site.register(Feed_Subtype)
admin.site.register(Feed_Unit)
admin.site.register(Vendor)
admin.site.register(Feed_Purchase)
admin.site.register(Task)
admin.site.register(Task_Master)
admin.site.register(Task_Recurring)





