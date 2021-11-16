import json
from json.decoder           import JSONDecodeError
from dateutil.relativedelta import relativedelta
from datetime               import datetime

from django.views           import View
from django.db.models       import Q
from django.http            import JsonResponse

from researches.models import *

class DetailView(View):
    def get(self, request, research_id):
        try:
            research = Research.objects.get(id=research_id)

            data = [{
                'id'                     : research.id,
                '과제번호'               : research.number,
                '과제명'                 : research.name,
                '전체목표연구대상자수'   : research.subject_number,
                '연구기간'               : research.period,
                '연구책임기관'           : research.institution.name,
                '연구종류'               : research.type.name,
                '임상시험단계(연구모형)' : research.stage.name,
                '연구범위'               : research.range.name,
                'created_at'             : research.created_at,
                'updated_at'             : research.updated_at
            }]

            return JsonResponse({'data': data}, status=200)
        
        except Research.DoesNotExist:
            return JsonResponse({'message': 'RESEARCH_DOES_NOT_EXIST'})

class ResearchView(View):
  def get(self, request):
      search = request.GET.get('search')
      period = request.GET.get('period')
      page   = int(request.GET.get('page', 1))

      page_size = 20
      limit     = page_size * page
      offset    = limit - page_size

      period_dic = {
                '1w' : datetime.now() - relativedelta(weeks= 1),
                '1m' : datetime.now() - relativedelta(months = 1),
                '3m' : datetime.now() - relativedelta(months = 3),
            }

      research_filter = Q()

      if search:
        research_filter.add(Q(name__icontains=search) | Q(institution__name__icontains=search), Q.AND)

      if period:
        research_filter.add(Q(updated_at__range=(period_dic.get(period, '1w'), datetime.now())))

      researches = Research.objects.select_related('research_ranges', 'research_institutions', 'research_types', 'research_stages')\
                                   .filter(research_filter)\
                                   .order_by('-created_at')

      data = [{
        'id'                     : research.id,
        '과제번호'               : research.number,
        '과제명'                 : research.name,
        '연구책임기관'           : research.institution.name,
        '전체목표연구대상자수'   : research.subject_number,
        '연구기간'               : research.period,
        '연구종류'               : research.type.name,
        '임상시험단계(연구모형)' : research.stage.name,
        '연구범위'               : research.range.name
      } for research in researches]

      return JsonResponse({'data' : data[offset:limit]}, status = 200) 