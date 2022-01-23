from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from core.serializers import UserSerializer, GroupSerializer, AmountSerializer,SearchSerializer

from core.models import Amount


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class AmountViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows places to be viewed or edited.
    """
    queryset = Amount.objects.all()
    serializer_class = AmountSerializer


class SearchView(APIView):
    def calculate_amount(self, searched_value):
        try:
            sum = 0
            result_list = []
            amounts_list = Amount.objects.order_by('-amount').all()
            for i in amounts_list:
                if sum < searched_value and searched_value - sum > i.amount:
                    if i.amount <= searched_value:
                        if sum + i.amount < searched_value:
                            result_list.append(i.amount)
                            print('falta ' + str(searched_value - sum))
                            sum = sum + i.amount
                            print('sum: after' + str(sum))
            print('total' + str(sum))
            print(result_list)
            self.response.update({
            'list of values': result_list,
            'total': sum,
            'searched value': searched_value,
            'status': status.HTTP_200_OK
            })
        except:
            self.response.update({
            'msg': "No amount available",
            'status': status.HTTP_400_BAD_REQUEST
            })

    #def get(self, request, format=None):
    #    return Response([{'msg': ''}])
    
    def post(self, request, *args, **kwargs):
        serializer_class = SearchSerializer(data=request.data)
        self.response = dict()
        self.calculate_amount(request.data.get('amount'))
        return Response(self.response, status=self.response['status'])
        