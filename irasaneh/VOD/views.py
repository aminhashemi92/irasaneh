from django.shortcuts import render, get_object_or_404, get_list_or_404
from resaneh.models import Resaneh
from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import *
from .serializers import *
from .permissions import *
from account.models import CustomUser

# Create your views here.
class ResanehList(ListAPIView):
    queryset = Resaneh.objects.all()
    serializer_class = ResanehSerializer
    permission_classes = (IsSuperUser,)

class ResanehDetail(RetrieveAPIView):
    queryset = Resaneh.objects.all()
    serializer_class = ResanehSerializer


class AdVideoList(ListAPIView):
    queryset = AdVideo.objects.all()
    serializer_class = AdVideoSerializer

class AdVideoDetail(RetrieveAPIView):
    queryset = AdVideo.objects.all()
    serializer_class = AdVideoSerializer


class AdBoxList(ListAPIView):
    queryset = AdBox.objects.all()
    serializer_class = AdBoxSerializer

class AdBoxDetail(RetrieveAPIView):
    queryset = AdBox.objects.all()
    serializer_class = AdBoxSerializer


class AdEventList(ListAPIView):
    queryset = AdEvent.objects.all()
    serializer_class = AdEventSerializer

class AdEventDetail(RetrieveAPIView):
    queryset = AdEvent.objects.all()
    serializer_class = AdEventSerializer


class AdConnectionLogPost(CreateAPIView):
    queryset = AdConnectionLog.objects.all()
    serializer_class = AdConnectionLogSerializer


class AdApplicationLogPost(CreateAPIView):
    queryset = AdApplicationLog.objects.all()
    serializer_class = AdApplicationLogSerializer


class AdVideoLogPost(CreateAPIView):
    queryset = AdVideoLog.objects.all()
    serializer_class = AdVideoLogSerializer


class AdVideoCounterLogPost(CreateAPIView):
    queryset = AdVideoCounterLog.objects.all()
    serializer_class = AdVideoCounterLogSerializer


class AdMyBox(RetrieveAPIView):
    serializer_class = AdEventSerializer
    def get_object(self):
        pk = self.kwargs.get('pk')
        resaneh = get_object_or_404(Resaneh, id=pk)
        # resaneh = Resaneh.objects.get(id=pk)
        event = resaneh.adevent.last()

        return event


class AdMyResanehs(ListAPIView):
    serializer_class = ResanehSerializer
    def get_queryset(self):
        phone = self.kwargs.get('phone')
        user = get_object_or_404(CustomUser, phone=phone)
        company = user.profile.company
        resanehs = get_list_or_404(Resaneh,company=company, is_digital=True)
        return resanehs


@api_view()
def testapi(request):
    context ={
        "name" : 'amin',
        "id": 2,
        "url": "google.com",
        }
    return Response(context)
