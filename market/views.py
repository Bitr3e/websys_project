from pathlib import Path
from django.http import FileResponse

BASE = Path(__file__).resolve().parent.parent


def service_worker(request):
    sw_path = BASE / 'static' / 'js' / 'sw.js'
    return FileResponse(open(sw_path, 'rb'), content_type='application/javascript')
