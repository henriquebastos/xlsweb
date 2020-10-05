from django.core.files import File
from django.http import HttpResponse
from django.shortcuts import render
from xlsweb.lib.extract import Spreadsheet, Viewport


def home(request):
    if request.method == 'POST':
        file = File(request.FILES['xls'])
        xls = Spreadsheet.from_xls(file.open('rb').read(), Viewport(request.POST['range']))

        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = f'attachment; filename="{file.name}"'
        response.write(str(xls))

        return response
    else:
        return render(request, 'index.html')
