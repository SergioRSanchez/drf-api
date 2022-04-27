from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from agenda.models import Agendamento
from agenda.serializer import AgendamentoSerializer

# Create your views here.

def agendamento_detail(request, id):
    obj = get_object_or_404(Agendamento, id=id)
    serializer = AgendamentoSerializer(obj)
    return JsonResponse(serializer.data)

def agendamento_list(request):
    queryset = Agendamento.objects.all()
    serializer = AgendamentoSerializer(queryset, many=True)
    return JsonResponse(serializer.data, safe=False)