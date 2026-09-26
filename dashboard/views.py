from rest_framework.views import APIView
from rest_framework.response import Response

class DashboardStatusView(APIView):
    def get(self, request):
        return Response({'status': 'active', 'app': 'dashboard'})
