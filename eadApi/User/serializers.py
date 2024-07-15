from rest_framework import serializers
from .models import Student, Admin, ContentCreator
from Course.models import Course

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student 
        fields = ['id', 'first_name', 'last_name', 'email', 'cpf', 'username', 'password', 'role']
        extra_kwargs = {
            'password': {'write_only': True, 'required': False},
            'email': {'required': False},
            'cpf': {'required': False},
            'username': {'required': False},
            'first_name': {'required': False},
            'last_name': {'required': False},
            'role': {'required': False}
        }

    def create(self, validated_data):
        if 'password' not in validated_data:
            raise serializers.ValidationError({'password': 'This field is required.'})
        user = self.Meta.model(
            email=validated_data['email'],
            cpf=validated_data['cpf'],
            username=validated_data['username'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            role=validated_data.get('role', 'student')
        )
        user.set_password(validated_data['password'])
        user.save()
        return user

    def update(self, instance, validated_data):
        instance.email = validated_data.get('email', instance.email)
        instance.cpf = validated_data.get('cpf', instance.cpf)
        instance.username = validated_data.get('username', instance.username)
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        instance.role = validated_data.get('role', instance.role)

        if 'password' in validated_data:
            instance.set_password(validated_data['password'])

        instance.save()
        return instance

class StudentSerializer(UserSerializer):
    course_titles = serializers.SerializerMethodField()

    class Meta(UserSerializer.Meta):
        model = Student
        fields = UserSerializer.Meta.fields + ['courses', 'course_titles']

    def get_course_titles(self, obj):
        return [course.title for course in obj.courses.all()]

class AdminSerializer(UserSerializer):
    class Meta(UserSerializer.Meta):
        model = Admin

class ContentCreatorSerializer(UserSerializer):
    courses = serializers.PrimaryKeyRelatedField(queryset=Course.objects.all(), many=True, required=False)
    course_titles = serializers.SerializerMethodField()

    class Meta(UserSerializer.Meta):
        model = ContentCreator
        fields = UserSerializer.Meta.fields + ['courses', 'course_titles']

    def update(self, instance, validated_data):
        instance.email = validated_data.get('email', instance.email)
        instance.cpf = validated_data.get('cpf', instance.cpf)
        instance.username = validated_data.get('username', instance.username)
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        instance.role = validated_data.get('role', instance.role)

        if 'password' in validated_data:
            instance.set_password(validated_data['password'])

        if 'courses' in validated_data:
            instance.courses.set(validated_data['courses'])

        instance.save()
        return instance

    def get_course_titles(self, obj):
        return [course.title for course in obj.courses.all()]
