from rest_framework import viewsets
from .models import GymClass, Member, MemberEntry, Payment, Trainer
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from .serializers import GymClassSerializer, MemberEntrySerializer, MemberSerializer, PaymentSerializer, TrainerSerializer
from rest_framework import generics, mixins
from rest_framework.response import Response
from rest_framework import generics, status


class MemberListCreateView(generics.GenericAPIView, mixins.ListModelMixin, mixins.CreateModelMixin):
    serializer_class = MemberSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        db_name = self.request.query_params.get('db_name')
        return Member.objects.using(db_name).all()

    def get(self, request, *args, **kwargs):
        members = self.get_queryset()
        return Response({"data": self.serializer_class(members, many=True).data}, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        db_name = request.query_params.get('db_name')
        serializer = self.serializer_class(data=request.data, context={'db_name': db_name})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            




class MemberRetrieveUpdateDestroyView(generics.GenericAPIView, mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin):
    serializer_class = MemberSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        db_name = self.request.query_params.get('db_name')
        return Member.objects.using(db_name).all()

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        instance = self.get_object()
        db_name = self.request.query_params.get('db_name')
        serializer = self.serializer_class(instance, data=request.data, context={'db_name': db_name}, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, *args, **kwargs):
        instance = self.get_object()
        db_name = self.request.query_params.get('db_name')
        instance.delete(using=db_name)
        return Response(status=status.HTTP_204_NO_CONTENT)




class MemberEntryListCreateView(generics.GenericAPIView, mixins.ListModelMixin, mixins.CreateModelMixin):
    serializer_class = MemberEntrySerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        db_name = self.request.query_params.get('db_name')
        return MemberEntry.objects.using(db_name).all()

    def get(self, request, *args, **kwargs):
        entries = self.get_queryset()
        return Response({"data": self.serializer_class(entries, many=True).data}, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        db_name = request.query_params.get('db_name')
        serializer = self.serializer_class(data=request.data, context={'db_name': db_name})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class MemberEntryRetrieveUpdateDestroyView(generics.GenericAPIView, mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin):
    serializer_class = MemberEntrySerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        db_name = self.request.query_params.get('db_name')
        return MemberEntry.objects.using(db_name).all()

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        instance = self.get_object()
        db_name = self.request.query_params.get('db_name')
        serializer = self.serializer_class(instance, data=request.data, context={'db_name': db_name}, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, *args, **kwargs):
        instance = self.get_object()
        db_name = self.request.query_params.get('db_name')
        instance.delete(using=db_name)
        return Response(status=status.HTTP_204_NO_CONTENT)



class TrainerListCreateView(generics.GenericAPIView, mixins.ListModelMixin, mixins.CreateModelMixin):
    serializer_class = TrainerSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        db_name = self.request.query_params.get('db_name')
        return Trainer.objects.using(db_name).all()

    def get(self, request, *args, **kwargs):
        trainers = self.get_queryset()
        return Response({"data": self.serializer_class(trainers, many=True).data}, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        db_name = request.query_params.get('db_name')
        serializer = self.serializer_class(data=request.data, context={'db_name': db_name})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class TrainerRetrieveUpdateDestroyView(generics.GenericAPIView, mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin):
    serializer_class = TrainerSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        db_name = self.request.query_params.get('db_name')
        return Trainer.objects.using(db_name).all()

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        instance = self.get_object()
        db_name = self.request.query_params.get('db_name')
        serializer = self.serializer_class(instance, data=request.data, context={'db_name': db_name}, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, *args, **kwargs):
        instance = self.get_object()
        db_name = self.request.query_params.get('db_name')
        instance.delete(using=db_name)
        return Response(status=status.HTTP_204_NO_CONTENT)



class GymClassListCreateView(generics.GenericAPIView, mixins.ListModelMixin, mixins.CreateModelMixin):
    serializer_class = GymClassSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        db_name = self.request.query_params.get('db_name')
        return GymClass.objects.using(db_name).all()

    def get(self, request, *args, **kwargs):
        gym_classes = self.get_queryset()
        return Response({"data": self.serializer_class(gym_classes, many=True).data}, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        db_name = request.query_params.get('db_name')
        serializer = self.serializer_class(data=request.data, context={'db_name': db_name})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class GymClassRetrieveUpdateDestroyView(generics.GenericAPIView, mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin):
    serializer_class = GymClassSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        db_name = self.request.query_params.get('db_name')
        return GymClass.objects.using(db_name).all()

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        instance = self.get_object()
        db_name = self.request.query_params.get('db_name')
        serializer = self.serializer_class(instance, data=request.data, context={'db_name': db_name}, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, *args, **kwargs):
        instance = self.get_object()
        db_name = self.request.query_params.get('db_name')
        instance.delete(using=db_name)
        return Response(status=status.HTTP_204_NO_CONTENT)



class PaymentListCreateView(generics.GenericAPIView, mixins.ListModelMixin, mixins.CreateModelMixin):
    serializer_class = PaymentSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        db_name = self.request.query_params.get('db_name')
        return Payment.objects.using(db_name).all()

    def get(self, request, *args, **kwargs):
        payments = self.get_queryset()
        return Response({"data": self.serializer_class(payments, many=True).data}, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        db_name = request.query_params.get('db_name')
        serializer = self.serializer_class(data=request.data, context={'db_name': db_name})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PaymentRetrieveUpdateDestroyView(generics.GenericAPIView, mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin):
    serializer_class = PaymentSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        db_name = self.request.query_params.get('db_name')
        return Payment.objects.using(db_name).all()

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        instance = self.get_object()
        db_name = self.request.query_params.get('db_name')
        serializer = self.serializer_class(instance, data=request.data, context={'db_name': db_name}, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, *args, **kwargs):
        instance = self.get_object()
        db_name = self.request.query_params.get('db_name')
        instance.delete(using=db_name)
        return Response(status=status.HTTP_204_NO_CONTENT)