from django.http import HttpResponse
from reportlab.pdfgen import canvas
from ordens.models import OrdemServico

def gerar_relatorio(request):
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="relatorio_ordens.pdf"'

    p = canvas.Canvas(response)
    p.setFont("Helvetica-Bold", 16)
    p.drawString(100, 800, "Relatório de Ordens de Serviço")

    ordens = OrdemServico.objects.all()
    y = 760
    for ordem in ordens:
        p.setFont("Helvetica", 12)
        p.drawString(50, y, f"ID: {ordem.id} | Cliente: {ordem.cliente} | Descrição: {ordem.descricao} | Status: {ordem.status}")
        y -= 20
        if y < 50: 
            p.showPage()
            p.setFont("Helvetica", 12)
            y = 800

    p.showPage()
    p.save()
    return response
