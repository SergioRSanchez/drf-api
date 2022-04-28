from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from agenda.models import Agendamento
from agenda.serializer import AgendamentoSerializer

# Create your views here.

@api_view(http_method_names=['GET', 'PATCH', 'DELETE'])
def agendamento_detail(request, id):
    if request.method == 'GET':
        obj = get_object_or_404(Agendamento, id=id)
        serializer = AgendamentoSerializer(obj)
        return JsonResponse(serializer.data)
    if request.method == 'PATCH':
        obj = get_object_or_404(Agendamento, id=id)
        serializer = AgendamentoSerializer(data=request.data, partial=True)
        if serializer.is_valid():
            validated_data = serializer.validated_data
            obj.data_horario = validated_data.get("data_horario", obj.data_horario)
            obj.nome_cliente = validated_data.get("nome_cliente", obj.nome_cliente)
            obj.email_cliente = validated_data.get("email_cliente", obj.email_cliente)
            obj.telefone_cliente = validated_data.get("telefone_cliente", obj.telefone_cliente)
            obj.save()
            return JsonResponse(validated_data, status=200)
        return JsonResponse(serializer.errors, status=400)
    if request.method == 'DELETE':
        obj = get_object_or_404(Agendamento, id=id)
        obj.horario_cancelado = True
        obj.save()
        return Response(status=204)

@api_view(http_method_names=['GET', 'POST'])
def agendamento_list(request):
    if request.method == 'GET':
        queryset = Agendamento.objects.exclude(horario_cancelado=True)
        serializer = AgendamentoSerializer(queryset, many=True)
        return JsonResponse(serializer.data, safe=False)
    if request.method == 'POST':
        data = request.data
        serializer = AgendamentoSerializer(data=data)
        if serializer.is_valid():
            validated_data = serializer.validated_data
            Agendamento.objects.create(
                data_horario=validated_data["data_horario"],
                nome_cliente=validated_data["nome_cliente"],
                email_cliente=validated_data["email_cliente"],
                telefone_cliente=validated_data["telefone_cliente"]
            )
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)