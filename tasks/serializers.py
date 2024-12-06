from rest_framework import serializers # type: ignore
from .models import User, Company_Project, Task

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

    def validate_password(self, value):
        if len(value) < 8:
            raise serializers.ValidationError("Password must be at least 8 characters long.")
        if not any(char.isdigit() for char in value):
            raise serializers.ValidationError("Password must contain at least one digit.")
        if not any(char.isalpha() for char in value):
            raise serializers.ValidationError("Password must contain at least one letter.")
        return value

    def validate_email(self, value):
        if User.objects.filter(email=value).exists():
            raise serializers.ValidationError("Email must be unique.")
        return value

    def validate_role(self, value):
        valid_roles = ['admin', 'user', 'manager']  # Example roles
        if value not in valid_roles:
            raise serializers.ValidationError(f"Role must be one of {valid_roles}.")
        return value

    def validate(self, data):
        email = data.get('email')
        role = data.get('role')
        if User.objects.filter(email=email, role=role).exists():
            raise serializers.ValidationError("A user with this email and role already exists.")
        return data

class Company_ProjectSerializer(serializers.ModelSerializer):
    assigned_to_name = serializers.SerializerMethodField()
    created_by_name = serializers.SerializerMethodField()

    class Meta:
        model = Company_Project
        fields = '__all__'

    def get_assigned_to_name(self, obj):
        return obj.assigned_to.name if obj.assigned_to else None

    def get_created_by_name(self, obj):
        return obj.created_by.name if obj.created_by else None

    def validate_name(self, value):
        if not value:
            raise serializers.ValidationError("Project name cannot be empty.")
        return value

    def validate_description(self, value):
        if len(value) < 10:
            raise serializers.ValidationError("Description must be at least 10 characters long.")
        return value

    def validate(self, data):
        if data['start_date'] > data['end_date']:
            raise serializers.ValidationError("End date must be after start date.")
        return data