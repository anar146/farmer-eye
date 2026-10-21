from rest_framework.decorators import api_view, parser_classes
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response
from .models import Scan
from .serializers import ScanSerializer

@api_view(["POST"])
@parser_classes([MultiPartParser, FormParser])
def scan(request):
    img = request.FILES.get("image")
    if not img:
        return Response({"error": "image field required"}, status=400)

    # TODO: yahan baad me asli model ka prediction lagega
    obj = Scan.objects.create(
        image=img,
        crop="Tomato",
        disease="Early Blight (dummy)",
        confidence=0.91,
        severity="Medium",
        latitude=request.data.get("latitude") or None,
        longitude=request.data.get("longitude") or None,
    )
    return Response(ScanSerializer(obj, context={"request": request}).data, status=201)

@api_view(["GET"])
def history(request):
    qs = Scan.objects.all()[:50]
    return Response(ScanSerializer(qs, many=True, context={"request": request}).data)
