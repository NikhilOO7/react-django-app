from rest_framework import serializers
from leads.models import Lead

# Lead serializer
class LeadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lead
        fields = "__all__"      # To fetch all the fields of model
        