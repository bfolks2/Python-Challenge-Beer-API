from rest_framework import serializers
from mybeerapp.models import Beer, Rating

class BeerSerializer(serializers.ModelSerializer):

    average_rating = serializers.SerializerMethodField('_get_beer_average')

    def _get_beer_average(self, beer):
        return beer.total_average

    class Meta():
        model = Beer
        fields = ('name','id','user','calories','abv','style','location','created_at','glass','average_rating')

class RatingSerializer(serializers.ModelSerializer):
    class Meta():
        model = Rating
        fields = '__all__'
