from django.db   import models

from core.models import TimeStampModel

class Research(TimeStampModel):
    number         = models.CharField(max_length=50, unique=True)
    name           = models.CharField(max_length=200)
    subject_number = models.PositiveIntegerField(null=True)
    period         = models.CharField(max_length=50, null=True)
    institution    = models.ForeignKey('ResearchInstitution', on_delete=models.CASCADE)
    type           = models.ForeignKey('ResearchType', on_delete=models.CASCADE)
    stage          = models.ForeignKey('ResearchStage', on_delete=models.CASCADE, null=True)
    range          = models.ForeignKey('ResearchRange', on_delete=models.CASCADE)

    class Meta:
        db_table = 'researches'

class ResearchRange(TimeStampModel):
    name = models.CharField(max_length=50)

    class Meta:
        db_table = 'research_ranges'          

class ResearchInstitution(TimeStampModel):
    name = models.CharField(max_length=50)

    class Meta:
        db_table = 'research_institutions' 

class ResearchType(TimeStampModel):
    name = models.CharField(max_length=50)

    class Meta: 
        db_table = 'research_types' 

class ResearchStage(TimeStampModel):
    name = models.CharField(max_length=50)

    class Meta: 
        db_table = 'research_stages' 