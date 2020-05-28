"""
Definition of models.
"""

from django.db import models
from django.utils.timezone import datetime
#region ENUMS MODEL UNUSEABLE PYTHON < 3.7

#class ModelType(Enum):

#    Estimated = "Estimated", # Calculated model threat
#    Alleged = "Alleged", # Thinking model threat
#    Expert = "Expert", # Expertcreation model threat
#    Manual = "Manual" # Handcreation model threat

#    @classmethod
#    def choices(cls):
#        print(tuple((i.name, i.value) for i in cls))
#        return tuple((i.name, i.value) for i in cls)
#class Relevance(Enum):

#    Actual = "Actual", #...
#    NotActual = "Actual", #...
    
#    @classmethod
#    def choices(cls):
#        print(tuple((i.name, i.value) for i in cls))
#        return tuple((i.name, i.value) for i in cls)
    
#endregion

#region MAINMODELSAPP
class ModelThreat(models.Model):
    Id = models.IntegerField()
    model_type = (
        ("Estimated" , "Estimated"), # Calculated model threat
        ("Alleged", "Alleged"), # Thinking model threat
        ("Expert",  "Expert"), # Expertcreation model threat
        ("Manual", "Manual") # Handcreation model threat
    )
    ModelType = models.CharField(
        max_length=2,
        choices=model_type
    )
    #models.CharField(max_length=255, choices = ModelType.choices())
    DateCreated = models.DateTimeField();
    NameModel = models.CharField(max_length=255)
    NameOrganization = models.CharField(max_length=255)

class Threat(models.Model):
    Id = models.IntegerField()
    Number = models.CharField(max_length=255)
    Name  = models.CharField(max_length=255)
    Probability = models.FloatField()
    Damage  = models.FloatField()
    relevance_enum = (
        ("Actual" , "Actual"), # ...
        ("NotActual", "NotActual") # ...
       
    )
    RelevanceEnum = models.CharField(
        max_length=2,
        choices=relevance_enum
    )  
    # models.CharField(max_length=255, choices = Relevance.choices())
    ModelThreatIN = models.ForeignKey(ModelThreat, on_delete = models.CASCADE)

class StatisticData(models.Model):
    Id = models.IntegerField()
    IdThreat = models.CharField(max_length=255)
    X  = models.IntegerField()
    Time = models.DateTimeField();
    Y = models.FloatField();
    Probability  = models.FloatField();
    Damage  = models.FloatField();
    relevance_enum = (
        ("Actual" , "Actual"), # ...
        ("NotActual", "NotActual") # ...
       
    )
    RelevanceEnum = models.CharField(
        max_length=2,
        choices=relevance_enum
    )  
    ThreatIN = models.ForeignKey(Threat, on_delete = models.CASCADE)
#endregion