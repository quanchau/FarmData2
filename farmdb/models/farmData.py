from django.db import models
from django.contrib import admin
from django.utils import timezone

from .farm import Farm, Farmer
from .task import Task


# Check if this is required
class Field_GH(models.Model):
    size = models.DecimalField(max_digits=8, decimal_places=2)
    numberOfBeds = models.DecimalField(max_digits=5, decimal_places=2)  # I think this sound be integer
    length = models.DecimalField(max_digits=8, decimal_places=2)
    active = models.BooleanField(default=True)


class Plant(models.Model):
    crop = models.CharField(max_length=30)
    units = models.CharField(max_length=30)
    units_per_case = models.FloatField()
    dh_units = models.CharField(max_length=30)
    active = models.BooleanField(default=True)


class labor(models.Model):
    ##The farmer who created the labor job? Or is it for the laborer himself?
    farmer = models.ForeignKey(Farmer, on_delete=models.CASCADE)
    # Labor add date?
    ldate = models.DateField()
    crop = models.CharField(max_length=30)
    # Pretty sure this needs to be a FK for field_GH
    fieldID = models.CharField(max_length=30)
    # Need to create a Task class
    task = models.ForeignKey(Task)
    hours = models.DecimalField(max_digits=8, decimal_places=2)
    comments = models.TextField()


class flat(models.Model):
    cells = models.IntegerField()

    def __str__(self):
        return str(self.cells)


class transferred_to(models.Model):
    farmer = models.ForeignKey(Farmer, on_delete=models.CASCADE)
    field = models.ForeignKey(Field_GH, on_delete=models.CASCADE)
    crop = models.ForeignKey(Plant, on_delete=models.CASCADE)
    fieldID = models.CharField(max_length=30)
    bedft = models.DecimalField(max_digits=8, decimal_places=2)
    comments = models.TextField()
    rowsBed = models.PositiveIntegerField()
    hours = models.DecimalField(max_digits=8, decimal_places=2)
    gen = models.IntegerField(default=1)
    annual = models.BooleanField(default=True)
    lastHarvest = models.DateField()


class harvested(models.Model):
    farmer = models.ForeignKey(Farmer, on_delete=models.CASCADE)
    harvestDate = models.DateField()
    crop = models.ForeignKey(Plant, on_delete=models.CASCADE)
    field = models.ForeignKey(Field_GH, on_delete=models.CASCADE)
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


class gh_seeding(models.Model):
    farmer = models.ForeignKey(Farmer, on_delete=models.CASCADE)
    crop = models.ForeignKey(Plant, on_delete=models.CASCADE)
    seedDate = models.DateField()
    # Why are there two flat references?
    flats = models.DecimalField(max_digits=8, decimal_places=2)
    cellsFlat = models.IntegerField()
    gen = models.IntegerField(default=1)
    numseeds_planted = models.PositiveIntegerField()
    comments = models.TextField()
    varieties = models.TextField()

    class Meta:
        unique_together = ('crop', 'seedDate', 'varieties')


class extUnits(models.Model):
    unit = models.CharField(max_length=30)


# dfTables

class Tools(models.Model):
    tool_name = models.CharField(max_length=30)
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
    crop = models.ForeignKey(Plant, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=8, decimal_places=2)
    units = models.CharField(max_length=10)
    harvestList = models.ForeignKey(Harvest, on_delete=models.CASCADE)
    target = models.ForeignKey(Target, models.CASCADE)


class tractor(models.Model):
    tractorName = models.CharField(max_length=30)
    active = models.BooleanField(default=True)


class compostMaterial(models.Model):
    compostName = models.CharField(max_length=30)
    description = models.TextField()


class compostPile(models.Model):
    compostMat = models.ForeignKey(compostMaterial, on_delete=models.CASCADE)
    comments = models.TextField()
    cDate = models.DateField(verbose_name='Compost Date')
    active = models.BooleanField(default=True)

#What is compost activites and compost unit?

#Not sure what the use of the class is. The compostPile should take care of everything
class compost_units(models.Model):
    materials = models.ForeignKey(compostMaterial,on_delete=models.CASCADE)
    unit = models.CharField(max_length=30)
    pounds = models.DecimalField(max_digits=8,decimal_places=2)
    cubicYards = models.DecimalField(max_digits=8,decimal_places=2)
    comments = models.TextField()

class compost_activity(models.Model):
    actDate = models.DateField()
    pile= models.ForeignKey(compostPile,on_delete=models.CASCADE)
    activity=models.CharField(max_length=30)
    commments = models.TextField()

class compost_temperature(models.Model):
    tempDate=models.DateField()
    pile = models.ForeignKey(compostPile,on_delete=models.CASCADE)
    numReadings = models.IntegerField()
    comments = models.TextField()

# Insert values

#I think we need universal units. Not just for crops

# Need to get this classes checks by Matt
class units(models.Model):
    crop = models.CharField(max_length=30)

class product(models.Model):
    product = models.CharField(max_length=30)
    unit = models.CharField(max_length=30)
    units_per_case = models.DecimalField(max_digits=8,decimal_places=2)
    dh_units = models.CharField(max_length=30)
    active = models.BooleanField(default=True)

class invoice_master(models.Model):
    invoice_no = models.AutoField(primary_key=True)
    invoide_id = models.CharField(max_length=30,unique=True)
    salesDate = models.DateField(default=timezone.now)
    approved_by = models.CharField(max_length=30)
    target = models.ForeignKey(Target,on_delete=models.CASCADE)
    comments= models.TextField()

class invoice_entry(models.Model):
    invoice_master=models.ForeignKey(invoice_master,on_delete=models.CASCADE)
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
   incorp_tool = models.ForeignKey(Tools,on_delete=models.CASCADE)
   comments = models.TextField(),
   seedDate = models.DateField()
   fieldID = models.ForeignKey(Field_GH,on_delete=models.CASCADE)
   area_seeded =models.DecimalField(max_length=8,decimal_places=2)
   
# Why is there coverseedMaster and coverseed?
class coverSeed(models.Model):
   crop = models.ForeignKey(Plant,on_delete=models.CASCADE)
   seedRate = models.DecimalField(max_digits=8,decimal_places=2)
   num_pounds = models.DecimalField(max_digits=8,decimal_places=2)
   coverSeed = models.IntegerField()


class coverKill_master(models.Model):
   killDate = models.DateField()
   seedDate = models.DateField()
   incorpTool = models.CharField(max_length=30),
   totalBiomass = models.DecimalField(max_digits=8,decimal_places=2)
   comments = models.TextField(),
   fieldID = models.CharField(max_length=30),
   foreign key(fieldID) references field_GH(fieldID) on update cascade,
   foreign key(incorpTool) references tools(tool_name) on update cascade
) ENGINE=INNODB;

class coverKill(models.Model):
   id = models.IntegerField()
   seedDate = models.DateField()
   coverCrop = models.CharField(max_length=30), 
   foreign key(coverCrop) references coverCrop(crop) on update cascade,
foreign key(id) references coverKill_master(id)
   

class tSprayMaster(models.Model):
   sprayDate = models.DateField()
   noField = models.IntegerField()
   noMaterial = models.IntegerField()
   waterPerAcre = models.IntegerField()
   comment = models.TextField(),
   user = models.CharField(max_length=50),
   complete = models.BooleanField(default+True)
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



class fertilizerReference(models.Model):
    fertilizerName = models.CharField(max_length=30) primary key,
    active = models.BooleanField(default=True)

class liquidFertilizerReference(models.Model):
   fertilizerName = models.CharField(max_length=30) primary key,
   active tinyint(1) default 1) ENGINE=INNODB;

class fertilizer(models.Model):
   id int NOT NULL AUTO_INCREMENT primary key,
   username = models.CharField(max_length=50),
   inputDate = models.DateField()
   fieldID = models.CharField(max_length=30),
   fertilizer = models.CharField(max_length=30),
   crops = models.TextField(), rate float not null,
   numBeds int not null,
   totalApply float not null,
   comments = models.TextField(),
   hours float default 0,
   foreign key(fieldID) references field_GH(fieldId) on update cascade,
   foreign key(fertilizer) references fertilizerReference(fertilizerName) on update cascade
   ) ENGINE = INNODB;

class liquid_fertilizer(models.Model):
   id int NOT NULL AUTO_INCREMENT primary key,
   fieldID = models.CharField(max_length=30),
   username = models.CharField(max_length=50),
   inputDate = models.DateField()
   fertilizer = models.CharField(max_length=30),
   quantity = models.DecimalField(max_digits=8,decimal_places=2)
   dripRows int(11),
   unit = models.CharField(max_length=30),
   comments = models.CharField(max_length=30),
   hours float default 0,
   foreign key(fieldID) references field_GH(fieldId) on update cascade,
   foreign key(fertilizer) references liquidFertilizerReference(fertilizerName) on update cascade
   ) ENGINE=INNODB;

class stage(models.Model):
   stage = models.CharField(max_length=30) primary key) ENGINE=INNODB;

# insert into stage values('ESTABLISHING');
# insert into stage values('HARVEST READY');
# insert into stage values('MATURING');
# insert into stage values('NEW PLANTING');
# insert into stage values('POST HARVEST');

class disease (models.Model):
   diseaseName = models.CharField(max_length=30) primary key) ENGINE=INNODB;

class diseaseScout(models.Model):
   sDate = models.DateField()
   fieldID = models.CharField(max_length=30),
   crops = models.TextField(),
   disease = models.CharField(max_length=30),
   infest = models.IntegerField()
   stage = models.CharField(max_length=30),
   comments = models.TextField(),
   hours float default 0,
   id int NOT NULL AUTO_INCREMENT primary key,
   filename = models.CharField(max_length=200) default null,
   foreign key(fieldID) references field_GH(fieldID) on update cascade,
   foreign key(disease) references disease(diseaseName) on update cascade,
   foreign key(stage) references stage(stage) on update cascade) ENGINE=INNODB;

class pack (models.Model):
   packDate = models.DateField() 
   crop_product = models.CharField(max_length=30), 
   grade int(1),
   amount = models.DecimalField(max_digits=8,decimal_places=2)
   unit = models.CharField(max_length=30),
   comments = models.TextField(),
   bringBack tinyint(1), 
   Target = models.CharField(max_length=30),
   id int NOT NULL AUTO_INCREMENT primary key,
   foreign key(Target) references targets(targetName) on update cascade
) ENGINE=INNODB;

class distribution (models.Model):
   distDate = models.DateField() 
   crop_product = models.CharField(max_length=30), 
   grade int(1), 
   target = models.CharField(max_length=30), 
   amount = models.DecimalField(max_digits=8,decimal_places=2) 
   unit = models.CharField(max_length=30), 
   pricePerUnit double default 0,
   comments = models.TextField(), 
   id int NOT NULL AUTO_INCREMENT primary key,
   foreign key(target) references targets(targetName) on update cascade
) ENGINE=INNODB;


class correct (models.Model):
   id int auto_increment not null,
   correctDate = models.DateField()
   crop_product = models.CharField(max_length=30),
   grade = models.IntegerField()
   amount = models.DecimalField(max_digits=8,decimal_places=2)
   unit = models.CharField(max_length=30),
   primary key (id)
) ENGINE=INNODB;

class irrigation_device(models.Model):
   id int primary key not null auto_increment,
   irrigation_device = models.CharField(max_length=30) not null,
   unique(irrigation_device)
) ENGINE=INNODB; 

class pump_master (models.Model):
   id int NOT NULL AUTO_INCREMENT primary key,
   pumpDate = models.DateField()
   valve_open = models.TextField(),
   driveHZ = models.DecimalField(max_digits=8,decimal_places=2)
   outlet_psi = models.IntegerField()
   pump_kwh = models.DecimalField(max_digits=8,decimal_places=2)
   solar_kwh = models.DecimalField(max_digits=8,decimal_places=2)
   comment = models.TextField(),
   rain = models.DecimalField(max_digits=8,decimal_places=2)
   run_time int)
ENGINE=INNODB;


class pump_field ( models.Model):
   id int not null, 
   fieldID = models.CharField(max_length=30) not null,
   irr_device = models.CharField(max_length=30) not null,
   elapsed_time = models.IntegerField() 
   foreign key (id) references pump_master(id) on delete cascade on update cascade, 
   foreign key (irr_device) references irrigation_device(irrigation_device) on update cascade) engine=INNODB;

class field_irrigation(models.Model):
   fieldID = models.CharField(max_length=30) not null,
   elapsed_time int not null,
   irr_device = models.CharField(max_length=30),
   start_time = models.IntegerField()
   constraint foreign key (fieldID) references field_GH(fieldID) on update
cascade,
   constraint foreign key (irr_device) references
irrigation_device(irrigation_device) on update cascade) ENGINE=INNODB;

class pump_log_temp (models.Model):
  pumpDate date NOT NULL,
  valve_open = models.TextField(),
  driveHZ float NOT NULL,
  outlet_psi int(11) NOT NULL,
  pump_kwh float NOT NULL,
  solar_kwh float NOT NULL,
  comment = models.TextField(),
  start_time int
) ENGINE=INNODB;

class utilized_on (models.Model):
  util_date date NOT NULL,
  fieldID = models.CharField(max_length=30) NOT NULL,
  incorpTool = models.CharField(max_length=30) NOT NULL,
  pileID = models.CharField(max_length=30) NOT NULL,
  tperacre = models.DecimalField(max_digits=8,decimal_places=2)
  incorpTiming = models.CharField(max_length=30),
  fieldSpread = models.DecimalField(max_digits=8,decimal_places=2)
  comments = models.TextField(),
  id int NOT NULL AUTO_INCREMENT,
  PRIMARY KEY (id),
  UNIQUE util_date (util_= models.DateField()fieldID,incorpTool,pileID),
   FOREIGN KEY (incorpTool) REFERENCES tools (tool_name) ON UPDATE CASCADE,
   FOREIGN KEY (fieldID) REFERENCES field_GH (fieldID) ON UPDATE CASCADE,
   FOREIGN KEY (pileID) REFERENCES compost_pile (pileID) ON UPDATE CASCADE
) ENGINE=InnoDB;

class seedInfo (models.Model):
   crop = models.CharField(max_length=30) not null primary key,
   seedsGram = models.DecimalField(max_digits=8,decimal_places=2)
   seedsRowFt = models.DecimalField(max_digits=8,decimal_places=2)
   defUnit = models.CharField(max_length=10),
   foreign key (crop) references plant(crop) on update cascade)
   ENGINE=InnoDB;

class coverSeedInfo (models.Model):
   crop = models.CharField(max_length=30) not null primary key,
   rate = models.DecimalField(max_digits=8,decimal_places=2)
   foreign key (crop) references coverCrop(crop) on update cascade)
ENGINE=InnoDB;

class coverToOrder (models.Model):
   crop = models.CharField(max_length=30) not null,
   year = models.IntegerField()
   acres float default 0,
   nextNum int not null default 1,
   primary key (crop, year),
   foreign key (crop) references coverCrop(crop) on update cascade)
ENGINE=InnoDB;

class variety (models.Model):
   crop = models.CharField(max_length=30) not null,
   variety = models.CharField(max_length=50) not null,
   primary key (crop, variety),
   foreign key (crop) references plant(crop) on update cascade)
   ENGINE=InnoDB;

class coverVariety (models.Model):
   crop = models.CharField(max_length=30) not null,
   variety = models.CharField(max_length=50) not null,
   primary key (crop, variety),
   foreign key (crop) references coverCrop(crop) on update cascade)
   ENGINE=InnoDB;

class source (models.Model):
   source = models.CharField(max_length=50) not null primary key) ENGINE=InnoDB;

class toOrder (models.Model):
   crop = models.CharField(max_length=30) not null,
   year int not null,
   rowFt float not null default 0,
   nextNum int not null default 1,
   foreign key (crop) references plant(crop) on update cascade)
   ENGINE=InnoDB;

class orderItem (models.Model):
   crop = models.CharField(max_length=30) not null,
   variety = models.CharField(max_length=50) not null,
   year int not null,
   source = models.CharField(max_length=50) not null,
   catalogOrder = models.CharField(max_length=30),
   organic tinyint(1) default 1,
   catalogUnit = models.CharField(max_length=30),
   price = models.DecimalField(max_digits=8,decimal_places=2)
   unitsPerCatUnit real,
   catUnitsOrdered = models.IntegerField()
   status = models.CharField(max_length=10) default 'PENDING',
   source1 = models.CharField(max_length=50),
   sdate1 = models.DateField()
   source2 = models.CharField(max_length=50),
   sdate2 = models.DateField()
   source3 = models.CharField(max_length=50),
   sdate3 = models.DateField()
   id int not null,
   foreign key (crop) references plant(crop) on update cascade)
   ENGINE=InnoDB;

class coverOrderItem (models.Model):
   crop = models.CharField(max_length=30) not null,
   variety = models.CharField(max_length=50) not null,
   year int not null,
   source = models.CharField(max_length=50) not null,
   catalogOrder = models.CharField(max_length=30),
   organic tinyint(1) default 1,
   catalogUnit = models.CharField(max_length=30),
   price = models.DecimalField(max_digits=8,decimal_places=2)
   unitsPerCatUnit real,
   catUnitsOrdered = models.IntegerField()
   status = models.CharField(max_length=10) default 'PENDING',
   source1 = models.CharField(max_length=50),
   sdate1 = models.DateField()
   source2 = models.CharField(max_length=50),
   sdate2 = models.DateField()
   source3 = models.CharField(max_length=50),
   sdate3 = models.DateField()
   id int not null,
   foreign key (crop) references coverCrop(crop) on update cascade)
   ENGINE=InnoDB;

class seedInventory (models.Model):
   crop = models.CharField(max_length=30) not null,
   variety = models.CharField(max_length=50) not null,
   year int not null,
   code = models.CharField(max_length=20) not null,
   rowFt float not null default 0,
   inInventory float not null default 0,
   foreign key(crop) references plant(crop) on update cascade)
   ENGINE=InnoDB;

class coverSeedInventory (models.Model):
   crop = models.CharField(max_length=30) not null,
   variety = models.CharField(max_length=50) not null,
   year int not null,
   code = models.CharField(max_length=20) not null,
   acres float not null default 0,
   inInventory float not null default 0,
   foreign key(crop) references coverCrop(crop) on update cascade)
   ENGINE=InnoDB;
    






























