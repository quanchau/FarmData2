from django.db import models
from django.contrib import admin
from django.utils import timezone

from .farm import Farm, Farmer
from .task import Task


# Check if this is required
class Field(models.Model):
    size = models.DecimalField(max_digits=8, decimal_places=2)
    numberOfBeds = models.DecimalField(max_digits=5, decimal_places=2)  # I think this should be integer
    length = models.DecimalField(max_digits=8, decimal_places=2)
    active = models.BooleanField(default=True)


class Crop(models.Model):
    crop = models.CharField(max_length=30)
    units = models.CharField(max_length=30)
    units_per_case = models.FloatField()
    dh_units = models.CharField(max_length=30)
    active = models.BooleanField(default=True)


class Labor(models.Model):
    ##The farmer who created the labor job? Or is it for the laborer himself?
    farmer = models.ForeignKey(Farmer, on_delete=models.CASCADE)
    # Labor add date or labor work date?
    lDate = models.DateField(verbose='Labor Date')
    crop = models.ForeignKey(Crop,on_delete=models.CASCADE)
    field = models.ForeignKey(Field,on_delete=models.CASCADE)
    # Need to create a Task class
    task = models.ForeignKey(Task,on_delete=models.CASCADE)
    hours = models.DecimalField(max_digits=8, decimal_places=2)
    comments = models.TextField()

# What is this for?
class Flat(models.Model):
    cells = models.IntegerField()

    def __str__(self):
        return str(self.cells)


class TransferredTo(models.Model):
    farmer = models.ForeignKey(Farmer, on_delete=models.CASCADE)
    field = models.ForeignKey(Field, on_delete=models.CASCADE)
    crop = models.ForeignKey(Crop, on_delete=models.CASCADE)
    bedFt = models.DecimalField(max_digits=8, decimal_places=2)
    comments = models.TextField()
    rowsBed = models.PositiveIntegerField()
    hours = models.DecimalField(max_digits=8, decimal_places=2)
    # What's this used for?
    gen = models.IntegerField(default=1)
    annual = models.BooleanField(default=True)
    lastHarvest = models.DateField()


class Harvested(models.Model):
    farmer = models.ForeignKey(Farmer, on_delete=models.CASCADE)
    harvestDate = models.DateField()
    crop = models.ForeignKey(Crop, on_delete=models.CASCADE)
    field = models.ForeignKey(Field, on_delete=models.CASCADE)
    produce = models.DecimalField(max_digits=8, decimal_places=2)
    comments = models.TextField()
    hours = models.DecimalField(max_digits=8, decimal_places=2)
    unit = models.CharField(max_length=30)
    gen = models.IntegerField()


class comments(models.Model):
    farmer = models.ForeignKey(Farmer, on_delete=models.CASCADE)
    commentDate = models.DateField(auto_created=timezone.now)
    comments = models.TextField()
    filename = models.FileField(default=None, null=True)


class GhSeeding(models.Model):
    farmer = models.ForeignKey(Farmer, on_delete=models.CASCADE)
    crop = models.ForeignKey(Crop, on_delete=models.CASCADE)
    seedDate = models.DateField()
    # Why are there two flat references?
    flats = models.DecimalField(max_digits=8, decimal_places=2)
    cellsFlat = models.IntegerField()
    gen = models.IntegerField(default=1)
    numSeedsPlanted = models.PositiveIntegerField()
    comments = models.TextField()
    varieties = models.TextField()

    class Meta:
        unique_together = ('crop', 'seedDate', 'varieties')


class ExtUnits(models.Model):
    unit = models.CharField(max_length=30)


# dfTables

class Tool(models.Model):
    toolName = models.CharField(max_length=30)
    type = models.CharField(max_length=30)


class Harvest(models.Model):
    farm = models.ForeignKey(Farm, on_delete=models.CASCADE)
    comment = models.TextField()


class Target(models.Model):
    targetName = models.CharField(max_length=30)
    prefix = models.CharField(max_length=20)
    nextNum = models.SmallIntegerField(default=1)
    active = models.BooleanField(default=True)


class TargetEmail(models.Model):
    email = models.EmailField()
    target = models.ForeignKey(Target, on_delete=models.CASCADE)


class HarvestListItem(models.Model):
    crop = models.ForeignKey(Crop, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=8, decimal_places=2)
    units = models.CharField(max_length=10)
    harvestList = models.ForeignKey(Harvest, on_delete=models.CASCADE)
    target = models.ForeignKey(Target, models.CASCADE)


class Tractor(models.Model):
    Name = models.CharField(max_length=30)
    active = models.BooleanField(default=True)


class CompostMaterial(models.Model):
    name = models.CharField(max_length=30)
    description = models.TextField()


class CompostPile(models.Model):
    compostMat = models.ForeignKey(CompostMaterial, on_delete=models.CASCADE)
    comments = models.TextField(blank=True)
    cDate = models.DateField(verbose_name='Compost Date')
    active = models.BooleanField(default=True)

#What is compost activites and compost unit?

#Not sure what the use of the class is. The compostPile should take care of everything
class CompostUnits(models.Model):
    materials = models.ForeignKey(CompostMaterial,on_delete=models.CASCADE)
    unit = models.CharField(max_length=30)
    pounds = models.DecimalField(max_digits=8,decimal_places=2)
    cubicYards = models.DecimalField(max_digits=8,decimal_places=2)
    comments = models.TextField(blank=True)

class CompostActivity(models.Model):
    actDate = models.DateField()
    pile= models.ForeignKey(CompostPile,on_delete=models.CASCADE)
    activity=models.CharField(max_length=30)
    commments = models.TextField()

class CompostTemperature(models.Model):
    tempDate=models.DateField()
    pile = models.ForeignKey(CompostPile,on_delete=models.CASCADE)
    numReadings = models.IntegerField()
    comments = models.TextField(blank=True)

# Insert values

#I think we need universal units for everything. Not just for crops

# Need to get this classes checks by Matt
class units(models.Model):
    crop = models.CharField(max_length=30)

class product(models.Model):
    product = models.CharField(max_length=30)
    unit = models.CharField(max_length=30)
    units_per_case = models.DecimalField(max_digits=8,decimal_places=2)
    dh_units = models.CharField(max_length=30)
    active = models.BooleanField(default=True)

class invoiceMaster(models.Model):
    invoice_no = models.AutoField(primary_key=True)
    invoide_id = models.CharField(max_length=30,unique=True)
    salesDate = models.DateField(default=timezone.now)
    approved_by = models.CharField(max_length=30)
    target = models.ForeignKey(Target,on_delete=models.CASCADE)
    comments= models.TextField(blank=True)

class invoiceEntry(models.Model):
    invoice_master=models.ForeignKey(invoiceMaster,on_delete=models.CASCADE)
    product = models.CharField(max_length=30)
    cases = models.DecimalField(max_digits=8,decimal_places=2)
    price_case = models.DecimalField(max_digits=8,decimal_places=2)

class CoverCrop(models.Model):
    crop = models.CharField(max_length=30)
    # Should this be a decimal?
    drillRateMin = models.PositiveIntegerField()
    drillRateMax = models.PositiveIntegerField()
    brcstRateMin = models.PositiveIntegerField()
    brcstRateMax = models.PositiveIntegerField()
    legume = models.PositiveIntegerField()
    active = models.BooleanField(default=True)

class SeedingMethod(models.Model):
    seed_method = models.CharField(max_length=30)

# Insert default values

# Need method

class coverSeedList(models.Model):
   seed_method = models.ForeignKey(SeedingMethod,on_delete=models.CASCADE)
   incorp_tool = models.ForeignKey(Tool,on_delete=models.CASCADE)
   comments = models.TextField(),
   seedDate = models.DateField()
   fieldID = models.ForeignKey(Field, on_delete=models.CASCADE)
   area_seeded =models.DecimalField(max_digits=8,decimal_places=2)

# Why is there coverseedMaster and coverseed?
class coverSeed(models.Model):
   crop = models.ForeignKey(Crop, on_delete=models.CASCADE)
   seedRate = models.DecimalField(max_digits=8,decimal_places=2)
   num_pounds = models.DecimalField(max_digits=8,decimal_places=2)
   coverSeed = models.IntegerField()


class CoverKillList(models.Model):
   killDate = models.DateField()
   seedDate = models.DateField()
   incorpTool = models.ForeignKey(Tool,on_delete=models.CASCADE)
   totalBiomass = models.DecimalField(max_digits=8,decimal_places=2)
   comments = models.TextField(),
   field = models.ForeignKey(Field, on_delete=models.CASCADE)

class CoverKill(models.Model):
   coverKill = models.ForeignKey(CoverKillList, on_delete=models.CASCADE)
   seedDate = models.DateField()
   coverCrop = models.ForeignKey(CoverCrop,on_delete=models.CASCADE)


class tSprayMaster(models.Model):
   sprayDate = models.DateField()
   noField = models.IntegerField()
   noMaterial = models.IntegerField()
   waterPerAcre = models.IntegerField()
   comment = models.TextField(),
   user = models.CharField(max_length=50),
   complete = models.BooleanField(default=True)
   initials = models.CharField(max_length=8, blank= True)


class tSprayField(models.Model):
   id = models.IntegerField()
   fieldID = models.CharField(max_length=30),
   numOfBed = models.IntegerField()
   crops = models.TextField(),
   foreign key(id) references tSprayMaster(id),
   foreign key(fieldID) references field_GH(fieldID) on update cascade


class tSprayMaterials(models.Model):
   sprayMaterial = models.CharField(max_length=30)
   TRateUnits = models.CharField(max_length=30),
   TRateMin = models.DecimalField(max_digits=8,decimal_places=2)TRateMax = models.DecimalField(max_digits=8,decimal_places=2)
   TRateDefault = models.DecimalField(max_digits=8,decimal_places=2) BRateUnits = models.CharField(max_length=30),
   BRateMin = models.DecimalField(max_digits=8,decimal_places=2)BRateMax = models.DecimalField(max_digits=8,decimal_places=2)
   BRateDefault = models.DecimalField(max_digits=8,decimal_places=2) REI_HRS = models.CharField(max_length=20),
   PPE = models.CharField(max_length=30),
   active = models.BooleanField(default=True)

class tSprayWater(models.Model):
   id = models.IntegerField()
   material = models.CharField(max_length=30),
   rate = models.DecimalField(max_digits=8,decimal_places=2)
   actualTotalAmount = models.DecimalField(max_digits=8,decimal_places=2)
   foreign key(id) references tSprayMaster(id),
   foreign key(material) references tSprayMaterials(sprayMaterial) on update cascade


class pest(models.Model):
   pestName = models.CharField(max_length=30)

class pestScout(models.Model):
   sDate = models.DateField()
   crops = models.TextField()
   fieldID = models.CharField(max_length=30)
   pest = models.CharField(max_length=30)
   avgCount = models.DecimalField(max_digits=8,decimal_places=2)
   comments = models.TextField()
   hours =models.DecimalField(max_digits=8,decimal_places=2)
   filename = models.FileField(default=None,null=True)
   foreign key(pest) references pest(pestName) on update cascade,
   foreign key (fieldID) references field_GH(fieldID) on update cascade) ENGINE=INNODB;

class bspray(models.Model):
   sprayDate = models.DateField()
   fieldID = models.CharField(max_length=30)
   water =models.DecimalField(max_digits=8,decimal_places=2)
   materialSprayed = models.CharField(max_length=30)
   rate =models.DecimalField(max_digits=8,decimal_places=2)
   totalMaterial =models.DecimalField(max_digits=8,decimal_places=2)
   mixedWith = models.CharField(max_length=30)
   crops = models.TextField()
   comments = models.TextField(),
   foreign key (fieldID) references field_GH(fieldID) on update cascade,
   foreign key (materialSprayed) references tSprayMaterials(sprayMaterial) on update cascade

class weed(models.Model):
   weedName = models.CharField(max_length=30,primary_key=True)

class weedScout(models.Model):
   sDate = models.DateField()
   fieldID = models.CharField(max_length=30),
   weed = models.CharField(max_length=30),
   infestLevel = models.IntegerField()
   goneToSeed = models.IntegerField()
   comments = models.TextField(),
   hours =models.DecimalField(max_digits=8,decimal_places=2)
   filename = models.FileField(default=None,null=True)
   foreign key(weed) references weed(weedName) on update cascade,
   foreign key(fieldID) references field_GH(fieldID) on update cascade,
   unique(sDate,fieldID,weed))


class tillage(models.Model):
   tractorName = models.CharField(max_length=30),
   fieldID = models.CharField(max_length=30),
   tilldate = models.DateField()
   tool = models.CharField(max_length=30),
   num_passes = models.IntegerField()
   comment = models.TextField(),
   minutes = models.IntegerField()
   percent_filled =models.DecimalField(max_digits=8,decimal_places=2)
   foreign key(tractorName) references tractor(tractorName) on update cascade,
   foreign key (fieldID) references field_GH(fieldID) on update cascade,
   UNIQUE(fieldID,tilldate,tool),
   primary key(id))



# Do we need two different databases for these?
class fertilizerReference(models.Model):
    farm = models.ForeignKey(Farm, on_delete=models.CASCADE)
    fertilizerName = models.CharField(max_length=30)
    active = models.BooleanField(default=True)

    class Meta:
        unique_together=('farm','fertilizerName')

class liquidFertilizerReference(models.Model):
   farm = models.ForeignKey(Farm,on_delete=models.CASCADE)
   fertilizerName = models.CharField(max_length=30)
   active = models.BooleanField(default=True)

class fertilizer(models.Model):
   inputDate = models.DateField()
   field = models.ForeignKey(Field, on_delete=models.CASCADE)
   fertilizer == models.ForeignKey(fertilizerReference,on_delete=models.CASCADE)
   farmer = models.ForeignKey(Farmer,on_delete=models.CASCADE)
   crops = models.TextField()
   rate = models.DecimalField(max_digits=8,decimal_places=2)
   numBeds = models.PositiveIntegerField()
   totalApply = models.DecimalField(max_digits=8,decimal_places=2)
   comments = models.TextField(),
   hours = models.DecimalField(max_digits=8,decimal_places=2)
   foreign key(fieldID) references field_GH(fieldId) on update cascade,
   foreign key(fertilizer) references fertilizerReference(fertilizerName) on update cascade


class liquid_fertilizer(models.Model):
   field = models.ForeignKey(Field, on_delete=models.CASCADE)
   farmer =models.ForeignKey(Farmer,on_delete=models.CASCADE)
   inputDate = models.DateField()
   fertilizer = models.CharField(max_length=30),
   quantity = models.DecimalField(max_digits=8,decimal_places=2)
   dripRows = models.PositiveIntegerField()
   unit = models.CharField(max_length=30)
   comments = models.CharField(max_length=30)
   hours = models.DecimalField(max_digits=8,decimal_places=2)
   foreign key(fieldID) references field_GH(fieldId) on update cascade,
   foreign key(fertilizer) references liquidFertilizerReference(fertilizerName) on update cascade

# Mabye add default and the farm name here
class stage(models.Model):
    farm =  models.ForeignKey(Farm,on_delete=models.CASCADE)
    stage = models.CharField(max_length=30)

    class Meta:
        unique_together=('farm','stage')

# insert into stage values('ESTABLISHING');
# insert into stage values('HARVEST READY');
# insert into stage values('MATURING');
# insert into stage values('NEW PLANTING');
# insert into stage values('POST HARVEST');

class disease (models.Model):
    farm = models.ForeignKey(Farm, on_delete=models.CASCADE)
    diseaseName = models.CharField(max_length=30)

    class Meta:
       unique_together = ('farm', 'stage')

class diseaseScout(models.Model):
   sDate = models.DateField()
   fieldID = models.CharField(max_length=30),
   crops = models.TextField(),
   disease = models.CharField(max_length=30),
   infest = models.IntegerField()
   stage = models.CharField(max_length=30),
   comments = models.TextField(),
   hours = models.DecimalField(max_digits=8,decimal_places=2)
   filename = models.FileField(default=None,null=True)
   foreign key(fieldID) references field_GH(fieldID) on update cascade,
   foreign key(disease) references disease(diseaseName) on update cascade,
   foreign key(stage) references stage(stage) on update cascade) ENGINE=INNODB;

class pack (models.Model):
   packDate = models.DateField()
   crop_product = models.CharField(max_length=30)
   grade = models.PositiveIntegerField()
   amount = models.DecimalField(max_digits=8,decimal_places=2)
   unit = models.CharField(max_length=30)
   comments = models.TextField()
   bringBack =models.Boolean(default=True)
   Target = models.CharField(max_length=30)
   foreign key(Target) references targets(targetName) on update cascade


class distribution (models.Model):
   distDate = models.DateField()
   crop_product = models.CharField(max_length=30),
   grade = models.PositiveIntegerField()
   target = models.CharField(max_length=30),
   amount = models.DecimalField(max_digits=8,decimal_places=2)
   unit = models.CharField(max_length=30),
   pricePerUnit = models.DecimalField(max_digits=8,decimal_places=2,default=0)
   comments = models.TextField(),
   foreign key(target) references targets(targetName) on update cascade


class correct (models.Model):
   correctDate = models.DateField()
   crop_product = models.CharField(max_length=30)
   grade = models.IntegerField()
   amount = models.DecimalField(max_digits=8,decimal_places=2)
   unit = models.CharField(max_length=30)

class IrrigationDevice(models.Model):
    farm = models.ForeignKey(Farm,on_delete=models.CASCADE)
    irrigation_device = models.CharField(max_length=30)

   class Meta:
       unique_together= ('farm','irrigation_device')

class pump_master (models.Model):
   pumpDate = models.DateField()
   valve_open = models.TextField()
   driveHZ = models.DecimalField(max_digits=8,decimal_places=2)
   outlet_psi = models.IntegerField()
   pump_kwh = models.DecimalField(max_digits=8,decimal_places=2)
   solar_kwh = models.DecimalField(max_digits=8,decimal_places=2)
   comment = models.TextField()
   rain = models.DecimalField(max_digits=8,decimal_places=2)
   run_time =models.PositiveIntegerField()



class pump_field ( models.Model):
   fieldID = models.CharField(max_length=30)
   irr_device = models.CharField(max_length=30)
   elapsed_time = models.IntegerField()
   foreign key (id) references pump_master(id) on delete cascade on update cascade,
   foreign key (irr_device) references irrigation_device(irrigation_device) on update cascade) engine=INNODB;

class field_irrigation(models.Model):
   field = models.ForeignKey(Field, on_delete=models.CASCADE)
   elapsed_time = models.DecimalField(max_digits=8,decimal_places=2)
   irr_device=  models.ForeignKey(IrrigationDevice,on_delete=models.CASCADE)
   start_time = models.IntegerField()


class pump_log_temp (models.Model):
  pumpDate =models.DateField(default=timezone.now)
  valve_open = models.TextField()
  driveHZ =models.DecimalField(max_digits=8,decimal_places=2)
  outlet_psi =models.IntegerField()
  pump_kwh =models.DecimalField(max_digits=8,decimal_places=2)
  solar_kwh =models.DecimalField(max_digits=8,decimal_places=2)
  comment = models.TextField(),
  start_time =models.TimeField(default=timezone.now)

class utilized_on (models.Model):
  util_date = models.DateField(default=timezone.now)
  fieldID = models.CharField(max_length=30)
  incorpTool = models.CharField(max_length=30)
  pileID = models.CharField(max_length=30)
  tperacre = models.DecimalField(max_digits=8,decimal_places=2)
  incorpTiming = models.CharField(max_length=30),
  fieldSpread = models.DecimalField(max_digits=8,decimal_places=2)
  comments = models.TextField()
   UNIQUE util_date (util_= models.DateField()fieldID,incorpTool,pileID),
   FOREIGN KEY (incorpTool) REFERENCES tools (tool_name) ON UPDATE CASCADE,
   FOREIGN KEY (fieldID) REFERENCES field_GH (fieldID) ON UPDATE CASCADE,
   FOREIGN KEY (pileID) REFERENCES compost_pile (pileID) ON UPDATE CASCADE


class seedInfo (models.Model):
   crop = models.ForeignKey(Crop, on_delete=models.CASCADE)
   seedsGram = models.DecimalField(max_digits=8,decimal_places=2)
   seedsRowFt = models.DecimalField(max_digits=8,decimal_places=2)
   defUnit = models.CharField(max_length=10)

class coverSeedInfo (models.Model):
   crop = models.ForeignKey(Crop, on_delete=models.CASCADE)
   rate = models.DecimalField(max_digits=8,decimal_places=2)


class coverToOrder (models.Model):
   crop = models.ForeignKey(CoverCrop,on_delete=models.CASCADE)
   year = models.IntegerField()
   acres = models.DecimalField(max_digits=8,decimal_places=2)
   nextNum = models.PositiveIntegerField(default=1)

   class Meta:
       unique_together = ('crop','year')

class variety (models.Model):
   crop = models.ForeignKey(CoverCrop,on_delete=models.CASCADE)
   variety = models.CharField(max_length=50)

      class Meta:
       unique_together = ('crop','variety')

class coverVariety (models.Model):
   crop = models.ForeignKey(CoverCrop,on_delete=models.CASCADE)
   variety = models.CharField(max_length=50)

   class Meta:
       unique_together = ('crop','variety')

class source (models.Model):
   source = models.CharField(max_length=50)

class toOrder (models.Model):
   crop = models.ForeignKey(Crop, on_delete=models.CASCADE)
   year = models.PositiveIntegerField()
   rowFt = models.DecimalField(max_digits=8,decimal_places=2)
   nextNum = models.PositiveIntegerField(default=1)

class orderItem (models.Model):
   crop = models.ForeignKey(Crop, on_delete=models.CASCADE)
   variety = models.CharField(max_length=50)
   year = models.PositiveIntegerField()
   source = models.CharField(max_length=50)
   catalogOrder = models.CharField(max_length=30),
   organic = models.BooleanField(default=True)
   catalogUnit = models.CharField(max_length=30)
   price = models.DecimalField(max_digits=8,decimal_places=2)
   unitsPerCatUnit = models.DecimalField(max_digits=8,decimal_places=2)
   catUnitsOrdered = models.IntegerField()
   status = models.CharField(max_length=10, default= 'PENDING')
   source1 = models.CharField(max_length=50),
   sdate1 = models.DateField()
   source2 = models.CharField(max_length=50),
   sdate2 = models.DateField()
   source3 = models.CharField(max_length=50),
   sdate3 = models.DateField()

class coverOrderItem (models.Model):
   crop = models.ForeignKey(CoverCrop,on_delete=models.CASCADE)
   variety = models.CharField(max_length=50)
   year = models.PositiveIntegerField()
   source = models.CharField(max_length=50)
   catalogOrder = models.CharField(max_length=30)
   organic = models.BooleanField(default=True)
   catalogUnit = models.CharField(max_length=30)
   price = models.DecimalField(max_digits=8,decimal_places=2)
   unitsPerCatUnit = models.DecimalField(max_digits=8,decimal_places=2)
   catUnitsOrdered = models.IntegerField()
   status = models.CharField(max_length=10, default= 'PENDING')
   source1 = models.CharField(max_length=50),
   sdate1 = models.DateField()
   source2 = models.CharField(max_length=50),
   sdate2 = models.DateField()
   source3 = models.CharField(max_length=50),
   sdate3 = models.DateField()

class seedInventory (models.Model):
   crop = models.ForeignKey(Crop, on_delete=models.CASCADE)
   variety = models.CharField(max_length=50)
   year = models.PositiveIntegerField()
   code = models.CharField(max_length=20)
   rowFt = models.DecimalField(max_digits=8,decimal_places=2)
   inInventory = models.DecimalField(max_digits=8,decimal_places=2,default=0)

class coverSeedInventory (models.Model):
   crop = models.ForeignKey(CoverCrop,on_delete=models.CASCADE)
   variety = models.CharField(max_length=50)
   year = models.PositiveIntegerField()
   code = models.CharField(max_length=20)
   acres = models.DecimalField(max_digits=8,decimal_places=2)
   inInventory = models.DecimalField(max_digits=8,decimal_places=2,default=0)































