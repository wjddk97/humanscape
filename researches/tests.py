from django.test       import TestCase, Client, client

from researches.models import (
    Research, 
    ResearchInstitution, 
    ResearchRange, 
    ResearchStage, 
    ResearchType
)
class ResearchAppTest(TestCase):
    def setUp(self):
        research_range_list = [
            ResearchRange(
                id   = 1,
                name = '연구범위1'
            ),
            ResearchRange(
                id   = 2,
                name = '연구범위2'
            ),
            ResearchRange(
                id   = 3,
                name = '연구범위3'
            ),
            ResearchRange(
                id   = 4,
                name = '연구범위4'
            ),
            ResearchRange(
                id   = 5,
                name = '연구범위5'
            )
        ]
        ResearchRange.objects.bulk_create(research_range_list)

        research_institution_list = [
            ResearchInstitution(
                id   = 1,
                name = '책임기관1'
            ),
            ResearchInstitution(
                id   = 2,
                name = '책임기관2'
            ),
            ResearchInstitution(
                id   = 3,
                name = '책임기관3'
            ),
            ResearchInstitution(
                id   = 4,
                name = '책임기관4'
            ),
            ResearchInstitution(
                id   = 5,
                name = '책임기관5'
            )
        ]
        ResearchInstitution.objects.bulk_create(research_institution_list)

        research_type_list = [
            ResearchType(
                id   = 1,
                name = '연구타입1'
            ),
            ResearchType(
                id   = 2,
                name = '연구타입2'
            ),
            ResearchType(
                id   = 3,
                name = '연구타입3'
            ),
            ResearchType(
                id   = 4,
                name = '연구타입4'
            ),
            ResearchType(
                id   = 5,
                name = '연구타입5'
            ),    
        ]
        ResearchType.objects.bulk_create(research_type_list)

        research_stage_list = [
            ResearchStage(
                id   = 1,
                name = '연구단계1'
            ),
            ResearchStage(
                id   = 2,
                name = '연구단계2'
            ),
            ResearchStage(
                id   = 3,
                name = '연구단계3'
            ),
            ResearchStage(
                id   = 4,
                name = '연구단계4'
            ),
            ResearchStage(
                id   = 5,
                name = '연구단계5'
            ),
        ]
        ResearchStage.objects.bulk_create(research_stage_list)

        research_list = [
            Research(
                id             = 1,
                number         = 'C1',
                name           = '테스트1',
                subject_number = 100,
                period         = '1년',
                institution_id = 1,
                type_id        = 1,
                stage_id       = 1,
                range_id       = 1
            ),
            Research(
                id             = 2,
                number         = 'C2',
                name           = '테스트2',
                subject_number = 200,
                period         = '2년',
                institution_id = 2,
                type_id        = 2,
                stage_id       = 2,
                range_id       = 2
            ),
            Research(
                id             = 3,
                number         = 'C3',
                name           = '테스트3',
                subject_number = 300,
                period         = '3년',
                institution_id = 3,
                type_id        = 3,
                stage_id       = 3,
                range_id       = 3
            ),
            Research(
                id             = 4,
                number         = 'C4',
                name           = '테스트4',
                subject_number = 400,
                period         = '4년',
                institution_id = 4,
                type_id        = 4,
                stage_id       = 4,
                range_id       = 4
            ),
            Research(
                id             = 5,
                number         = 'C5',
                name           = '테스트5',
                subject_number = 500,
                period         = '5년',
                institution_id = 5,
                type_id        = 5,
                stage_id       = 5,
                range_id       = 5
            ),
            Research(
                id             = 6,
                number         = 'C6',
                name           = '테스트6',
                subject_number = 600,
                period         = '6년',
                institution_id = 1,
                type_id        = 2,
                stage_id       = 3,
                range_id       = 4
            ),
            Research(
                id             = 7,
                number         = 'C7',
                name           = '테스트7',
                subject_number = 700,
                period         = '7년',
                institution_id = 2,
                type_id        = 1,
                stage_id       = 3,
                range_id       = 4
            ),
            Research(
                id             = 8,
                number         = 'C8',
                name           = '테스트8',
                subject_number = 800,
                period         = '8년',
                institution_id = 3,
                type_id        = 2,
                stage_id       = 1,
                range_id       = 4
            ),
            Research(
                id             = 9,
                number         = 'C9',
                name           = '테스트9',
                subject_number = 900,
                period         = '9년',
                institution_id = 4,
                type_id        = 3,
                stage_id       = 2,
                range_id       = 1
            ),
            Research(
                id             = 10,
                number         = 'C10',
                name           = '테스트10',
                subject_number = 1000,
                period         = '10년',
                institution_id = 1,
                type_id        = 4,
                stage_id       = 3,
                range_id       = 2
            ),
        ]
        Research.objects.bulk_create(research_list)
    
    def tearDown(self):
        Research.objects.all().delete()
        ResearchRange.objects.all().delete()
        ResearchInstitution.objects.all().delete()
        ResearchType.objects.all().delete()
        ResearchStage.objects.all().delete()

    def test_research_list_get_success(self):
        client   = Client()
        response = client.get('/researches/5')
        self.assertEqual(response.status_code, 200)
    
    def test_research_list_get_does_not_exist(self):
        client   = Client()
        response = client.get('/researches/20')
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json(),{
            'message': 'RESEARCH_DOES_NOT_EXIST'
        })