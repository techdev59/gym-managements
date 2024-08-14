from rest_framework import serializers
from .models import Member, Trainer, GymClass, Payment, MemberEntry


class MemberSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    first_name = serializers.CharField(max_length=100)
    last_name = serializers.CharField(max_length=100)
    email = serializers.EmailField()
    phone_number = serializers.CharField(max_length=15)
    membership_start = serializers.DateField()
    membership_end = serializers.DateField()
    created_at = serializers.DateTimeField(read_only=True)
    updated_at = serializers.DateTimeField(read_only=True)

    def create(self, validated_data):
        db_name = self.context.get('db_name')
        return Member.objects.using(db_name).create(**validated_data)

    def update(self, instance, validated_data):
        db_name = self.context.get('db_name')
        
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        instance.email = validated_data.get('email', instance.email)
        instance.phone_number = validated_data.get('phone_number', instance.phone_number)
        instance.membership_start = validated_data.get('membership_start', instance.membership_start)
        instance.membership_end = validated_data.get('membership_end', instance.membership_end)

        instance.save(using=db_name)
        return instance
    

class MemberEntrySerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    member_id = serializers.IntegerField()
    entry_time = serializers.DateTimeField(read_only=True)
    exit_time = serializers.DateTimeField(required=False, allow_null=True)

    def create(self, validated_data):
        db_name = self.context.get('db_name')
        return MemberEntry.objects.using(db_name).create(**validated_data)

    def update(self, instance, validated_data):
        db_name = self.context.get('db_name')
        
        instance.member_id = validated_data.get('member_id', instance.member_id)
        instance.exit_time = validated_data.get('exit_time', instance.exit_time)

        instance.save(using=db_name)
        return instance



class TrainerSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=100)
    specialty = serializers.CharField(max_length=100)
    email = serializers.EmailField()
    phone_number = serializers.CharField(max_length=15)
    created_at = serializers.DateTimeField(read_only=True)
    updated_at = serializers.DateTimeField(read_only=True)

    def create(self, validated_data):
        db_name = self.context.get('db_name')
        return Trainer.objects.using(db_name).create(**validated_data)

    def update(self, instance, validated_data):
        db_name = self.context.get('db_name')
        
        instance.name = validated_data.get('name', instance.name)
        instance.specialty = validated_data.get('specialty', instance.specialty)
        instance.email = validated_data.get('email', instance.email)
        instance.phone_number = validated_data.get('phone_number', instance.phone_number)

        instance.save(using=db_name)
        return instance


class GymClassSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=100)
    trainer_id = serializers.IntegerField()
    member_id = serializers.IntegerField()
    start_time = serializers.TimeField()
    end_time = serializers.TimeField()
    created_at = serializers.DateTimeField(read_only=True)
    updated_at = serializers.DateTimeField(read_only=True)
    

    def create(self, validated_data):
        db_name = self.context.get('db_name')
        gym_class = GymClass.objects.using(db_name).create(**validated_data)
        return gym_class


    def update(self, instance, validated_data):
        db_name = self.context.get('db_name')

        instance.name = validated_data.get('name', instance.name)
        instance.trainer_id = validated_data.get('trainer_id', instance.trainer_id)
        instance.member_id = validated_data.get('member_id', instance.member_id)
        instance.start_time = validated_data.get('start_time', instance.start_time)
        instance.end_time = validated_data.get('end_time', instance.end_time)
        
        instance.save(using=db_name)
        return instance



class PaymentSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    member_id = serializers.IntegerField()
    amount = serializers.DecimalField(max_digits=10, decimal_places=2)
    payment_date = serializers.DateField()
    payment_method = serializers.ChoiceField(choices=Payment.PAYMENT_METHOD)
    created_at = serializers.DateTimeField(read_only=True)
    updated_at = serializers.DateTimeField(read_only=True)

    def create(self, validated_data):
        db_name = self.context.get('db_name')
        return Payment.objects.using(db_name).create(**validated_data)

    def update(self, instance, validated_data):
        db_name = self.context.get('db_name')
        
        instance.member_id = validated_data.get('member_id', instance.member_id)
        instance.amount = validated_data.get('amount', instance.amount)
        instance.payment_date = validated_data.get('payment_date', instance.payment_date)
        instance.payment_method = validated_data.get('payment_method', instance.payment_method)

        instance.save(using=db_name)
        return instance