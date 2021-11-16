from researches.views import PublicDataApi

from datetime import datetime
from django.db import transaction

from researches.models import Research, ResearchInstitution, ResearchRange, ResearchStage, ResearchType

@transaction.atomic
def batch_task(self,request):
    research_information = PublicDataApi().get_research_information().json()
    data = research_information.get('data')

    for data_number in range(len(data)):

        research_range, range_created = ResearchRange.objects.get_or_create(
            name = data[data_number]['연구범위']
        )
        research_institution, institution_created = ResearchInstitution.objects.get_or_create(
            name = data[data_number]['연구책임기관']
        )
        research_type, type_created = ResearchType.objects.get_or_create(
            name = data[data_number]['연구종류']
        )
        research_stage, stage_created = ResearchStage.objects.get_or_create(
            name = data[data_number]['임상시험단계(연구모형)']
        )

        institution      = ResearchInstitution.objects.latest('id').id if institution_created == True else research_institution.id
        type             = ResearchType.objects.latest('id').id if type_created == True else research_type.id
        stage            = ResearchStage.objects.latest('id').id if stage_created == True else research_stage.id
        researches_range = ResearchRange.objects.latest('id').id if range_created == True else research_range.id
        subject_number   = data[data_number]['전체목표연구대상자수']

        if not Research.objects.filter(number=data[data_number]['과제번호']).exists():
            Research.objects.create(
                number         = data[data_number]['과제번호'],
                name           = data[data_number]['과제명'],
                subject_number = None if subject_number == '' else subject_number,
                period         = data[data_number]['연구기간'],
                institution_id = institution,
                type_id        = type,
                range_id       = researches_range,
                stage_id       = None if stage == '' else stage 
            )

        else:
            research = Research.objects.get(number = data[data_number]['과제번호'])
            
            if not research.period == data[data_number]['연구기간']:
                    research.period     = data[data_number]['연구기간']
                    research.updated_at = datetime.now()
                    research.save()
                
            if not research.stage_id == stage:
                research.stage_id   = stage
                research.updated_at = datetime.now()
                research.save()