from django.forms import ValidationError
from rest_framework import serializers

from teacher.models import Aula, Professor


class ProfessorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Professor
        fields = ('id', 'nome', 'valor_hora', 'descricao', 'foto')  # '__all__'


class CadastrarAulaSerializer(serializers.Serializer):
    email = serializers.EmailField(max_length=255)
    nome = serializers.CharField(max_length=100)

    def validate_nome(self, value):
        if len(value) < 3:
            raise ValidationError("deve conter mais do que 3 caracteres")
        return value
    
    def validate_email(self, value):
        if '@' not in value:
            raise ValidationError("email invalido")
        return value


class AulaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Aula
        fields = '__all__'
