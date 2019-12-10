from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .models import FreeLancer
from .permissions import UserIsOwnerTodo
from .serializers import FreelancerSerializer
from rest_framework import status


class FreelancerListCreateAPIView(ListCreateAPIView):
    serializer_class = FreelancerSerializer

    def get_queryset(self):
        return FreeLancer.objects.filter(user=self.request.user)

    def check_unique(self, user_id):

        freelancer = FreeLancer.objects.filter(user=user_id).first()
        if freelancer is None:
            freelancer = 'SUCCESS'
        else:
            freelancer = 'FAILED'
        return freelancer

    def perform_create(self, serializer):
        check = self.check_unique(self.request.user.id)
        if check == 'SUCCESS':
            serializer.save(user=self.request.user)
        else:
            return Response(
                data='A data with that username already exists',
                status=status.HTTP_400_BAD_REQUEST,
            )


class FreelancerDetailAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = FreelancerSerializer
    queryset = FreeLancer.objects.all()
    permission_classes = (IsAuthenticated, UserIsOwnerTodo)


