from django.db import models
from django.contrib import admin
from django.utils import timezone


# The model imports.
from .farm import Farm

# The definitions

class AnimalGroup(models.Model):
    farm = models.ForeignKey(Farm, on_delete=models.CASCADE)
    animalGroup = models.CharField(max_length=50)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.animalGroup


class AnimalGroupAdmin(admin.ModelAdmin):
    list_display = ('farm', 'animalGroup', 'active')
    search_fields = ('farm', 'animalGroup')
    list_filter = ('active',)
    ordering = ('farm', 'animalGroup')


class Breed(models.Model):
    farm = models.ForeignKey(Farm, on_delete=models.CASCADE)
    breed = models.CharField(max_length=50)
    animalGroup = models.ForeignKey(AnimalGroup, on_delete=models.CASCADE)
    active = models.BooleanField(default=True)

    class Meta:
        unique_together = ('animalGroup', 'breed')

    def __str__(self):
        return self.breed


class BreedAdmin(admin.ModelAdmin):
    list_display = ('farm', 'breed', 'active', 'animalGroup')
    search_fields = ('farm', 'breed')
    list_filter = ('active',)
    ordering = ('farm', 'breed')


class AnimalSubGroup(models.Model):
    farm = models.ForeignKey(Farm, on_delete=models.CASCADE)
    animalSubGroup = models.CharField(max_length=50)
    animalGroup = models.ForeignKey(AnimalGroup, on_delete=models.CASCADE,verbose_name='Animal Group')
    active = models.BooleanField(default=True)

    class Meta:
        unique_together = ('farm', 'animalGroup', 'animalSubGroup')

    def __str__(self):
        return self.animalSubGroup


class SubGroupAdmin(admin.ModelAdmin):
    list_display = ('farm', 'animalSubGroup', 'active', 'animalGroup')
    search_fields = ('farm', 'animalSubGroup')
    list_filter = ('active',)
    ordering = ('farm', 'animalSubGroup')


class Origin(models.Model):
    farm = models.ForeignKey(Farm, on_delete=models.CASCADE)
    origin = models.CharField(max_length=200)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.origin


class OriginAdmin(admin.ModelAdmin):
    list_display = ('farm', 'origin', 'active')
    search_fields = ('farm', 'origin')
    list_filter = ('active',)
    ordering = ('farm', 'origin')


class Animal(models.Model):
    farm = models.ForeignKey(Farm, on_delete=models.CASCADE)
    animalId = models.CharField(max_length=50, unique=True)
    gender = models.CharField(max_length=1)
    birthDate = models.DateField()
    mother = models.CharField(max_length=50)
    father = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    markings = models.CharField(max_length=200)
    filename = models.FileField(null=True)
    alive = models.BooleanField(default=True)
    comments = models.TextField(blank=True)
    animalGroup = models.ForeignKey(AnimalGroup, on_delete=models.CASCADE)
    breed = models.ForeignKey(Breed, on_delete=models.CASCADE)
    animalSubGroup = models.ForeignKey(AnimalSubGroup, on_delete=models.CASCADE)
    origin = models.ForeignKey(Origin, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class AnimalAdmin(admin.ModelAdmin):
    list_display = ('farm')
    search_fields = ('farm', 'name')
    list_filter = ('active',)
    ordering = ('farm', 'name')


class Reason(models.Model):
    farm = models.ForeignKey(Farm, on_delete=models.CASCADE)
    reason = models.CharField(max_length=50)
    active = models.BooleanField()

    def __str__(self):
        return self.reason


class Vet(models.Model):
    farm = models.ForeignKey(Farm, on_delete=models.CASCADE)
    careDate = models.DateField(blank=True)
    animalId = models.ForeignKey(Animal, on_delete=models.CASCADE)
    reason = models.ForeignKey(Reason, on_delete=models.CASCADE)
    symptoms = models.TextField(blank=True)
    temperature = models.SmallIntegerField(blank=True)
    care = models.TextField(blank=True)
    weight = models.SmallIntegerField(blank=True)
    vet = models.CharField(max_length=100, blank=True)
    contact = models.IntegerField(blank=True)
    assistants = models.CharField(max_length=100, blank=True)
    comments = models.TextField(blank=True)

    # def __str__(self):
    #     return self.reason


class Medication(models.Model):
    farm = models.ForeignKey(Farm, on_delete=models.CASCADE)
    medication = models.CharField(max_length=100)
    dosage = models.CharField(max_length=100, blank=True)
    active = models.BooleanField()

    def __str__(self):
        return self.medication


class MedsGiven(models.Model):
    farm = models.ForeignKey(Farm, on_delete=models.CASCADE)
    medication = models.ForeignKey(Medication, on_delete=models.CASCADE)
    units = models.SmallIntegerField()
    units_given = models.SmallIntegerField()
    vet_id = models.ForeignKey(Vet, on_delete=models.CASCADE)

    # def __str__(self):
    #     return self.medication


class EggLog(models.Model):
    farm = models.ForeignKey(Farm, on_delete=models.CASCADE)
    collection_date = models.DateField()
    number = models.IntegerField()
    comments = models.TextField(max_length=300,blank=True)

    # def __str__(self):
    #     return self.collection_date


class Wormer(models.Model):
    farm = models.ForeignKey(Farm, on_delete=models.CASCADE)
    wormer = models.CharField(max_length=100)
    active = models.BooleanField()

    def __str__(self):
        return self.wormer


class SheepCare(models.Model):
    farm = models.ForeignKey(Farm, on_delete=models.CASCADE)
    care_date = models.DateField()
    animal = models.ForeignKey(Animal, on_delete=models.CASCADE)
    eye = models.SmallIntegerField()
    body = models.SmallIntegerField()
    tail = models.CharField(max_length=6)
    nose = models.CharField(max_length=100)
    coat = models.CharField(max_length=100)
    jaw = models.SmallIntegerField()
    wormer = models.CharField(max_length=100)
    wormer_quantity = models.IntegerField
    hoof = models.CharField(max_length=3)
    weight = models.IntegerField()
    estimated = models.CharField(max_length=9)
    comments = models.TextField()

    # def __str__(self):
    #     return self.animal


class Forage(models.Model):
    farm = models.ForeignKey(Farm, on_delete=models.CASCADE)
    forage = models.CharField(max_length=100)
    density = models.FloatField()
    active = models.BooleanField()


class Paddock(models.Model):
    farm = models.ForeignKey(Farm, on_delete=models.CASCADE)
    size = models.FloatField()
    forage = models.ForeignKey(Forage, on_delete=models.CASCADE)
    active = models.BooleanField()


# The move table has been omitted

class Note(models.Model):
    farm = models.ForeignKey(Farm, on_delete=models.CASCADE)
    note_date = models.DateField()
    note = models.TextField()
    filename = models.FileField(blank=True)
    created_by = models.CharField(max_length=50)


class Destination(models.Model):
    farm = models.ForeignKey(Farm, on_delete=models.CASCADE)
    destination = models.CharField(max_length=200)
    active = models.BooleanField()

    def __str__(self):
        return self.destination


class Sale(models.Model):
    farm = models.ForeignKey(Farm, on_delete=models.CASCADE)
    animal = models.OneToOneField(Animal, on_delete=models.CASCADE)
    saleTag = models.CharField(max_length=50)
    destination = models.ForeignKey(Destination, on_delete=models.CASCADE)
    weight = models.SmallIntegerField()
    estimated = models.CharField(max_length=9)
    priceLb = models.DecimalField(max_digits=8, decimal_places=2)
    fees = models.DecimalField(max_digits=6, decimal_places=2)
    comments = models.TextField()
    saleDate = models.DateField(auto_created=timezone.now)

    # def __str__(self):
    #     return self.animal


class SlayHouse(models.Model):
    farm = models.ForeignKey(Farm, on_delete=models.CASCADE)
    slayHouse = models.CharField(max_length=200)
    active = models.BooleanField()

    def __str__(self):
        return self.slay_house


class Slaughter(models.Model):
    farm = models.ForeignKey(Farm, on_delete=models.CASCADE)
    animal = models.OneToOneField(Animal, on_delete=models.CASCADE)
    saleTag = models.CharField(max_length=50)  # I suspect this should be a foreign key with the table sale
    slayHouse = models.ForeignKey(SlayHouse, on_delete=models.CASCADE)
    hauler = models.CharField(max_length=200)
    haulEquip = models.CharField(max_length=200)
    slayDate = models.DateField()
    weight = models.PositiveSmallIntegerField
    estimated = models.CharField(max_length=9)
    fees = models.DecimalField(max_digits=5, decimal_places=2)
    comments = models.TextField()

    # def __str__(self):
    #     return self.animal


class OtherDest(models.Model):
    farm = models.ForeignKey(Farm, on_delete=models.CASCADE)
    dest = models.CharField(max_length=50)
    active = models.BooleanField()

    def __str__(self):
        return self.dest


class OtherReason(models.Model):
    farm = models.ForeignKey(Farm, on_delete=models.CASCADE)
    reason = models.CharField(max_length=50)
    active = models.BooleanField()

    def __str__(self):
        return self.reason


class OtherRemove(models.Model):
    farm = models.ForeignKey(Farm, on_delete=models.CASCADE)
    animal = models.OneToOneField(Animal, on_delete=models.CASCADE)
    removeDate = models.DateField()
    reason = models.ForeignKey(OtherReason, on_delete=models.CASCADE)
    destination = models.ForeignKey(OtherDest, on_delete=models.CASCADE)
    weight = models.PositiveSmallIntegerField()
    comments = models.TextField()

    # def __str__(self):
        # return self.reason


class FeedType(models.Model):
    farm = models.ForeignKey(Farm, on_delete=models.CASCADE)
    type = models.CharField(max_length=50)
    active = models.BooleanField(default=True)


class FeedSubtype(models.Model):
    farm = models.ForeignKey(Farm, on_delete=models.CASCADE)
    type = models.ForeignKey(FeedType, on_delete=models.CASCADE)
    subtype = models.CharField(max_length=50)
    active = models.BooleanField(default=True)


class FeedUnit(models.Model):
    farm = models.ForeignKey(Farm, on_delete=models.CASCADE)
    unit = models.CharField(max_length=50)
    active = models.BooleanField(default=True)


class Vendor(models.Model):
    farm = models.ForeignKey(Farm, on_delete=models.CASCADE)
    vendor = models.CharField(max_length=200)
    active = models.BooleanField(default=True)


class FeedPurchase(models.Model):
    farm = models.ForeignKey(Farm, on_delete=models.CASCADE)
    purchaseDate = models.DateField()
    type = models.ForeignKey(FeedType, on_delete=models.CASCADE)
    subtype = models.ForeignKey(FeedSubtype, on_delete=models.CASCADE)
    animalGroup = models.ForeignKey(AnimalGroup, on_delete=models.CASCADE)
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE)
    units = models.ForeignKey(FeedUnit, on_delete=models.CASCADE)
    priceUnit = models.DecimalField(max_digits=8, decimal_places=2)
    weightUnit = models.DecimalField(max_digits=8, decimal_places=2)