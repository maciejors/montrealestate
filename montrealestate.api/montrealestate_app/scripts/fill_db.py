import montrealestate_app.models as m
import csv


def run():
    with open('./cities.csv', encoding='utf16') as file:
        reader = csv.reader(file)
        next(reader)

        m.CityMap.objects.all().delete()

        for row in reader:
            cityMap = m.CityMap(
                cityName=row[0],
                cityId=row[1],
            )
            cityMap.save()

    with open('./districts.csv', encoding='utf16') as file:
        reader = csv.reader(file)
        next(reader)

        m.DistrictMap.objects.all().delete()

        for row in reader:
            districtMap = m.DistrictMap(
                districtName=row[0],
                districtId=row[1],
            )
            districtMap.save()

    with open('./listings_final.csv', encoding='utf16') as file:
        reader = csv.reader(file)
        next(reader)

        m.Apartment.objects.all().delete()

        for row in reader:
            apartment = m.Apartment(
                address=row[0],
                city_id=row[1],
                district_id=row[2],
                postalCode=row[3],
                longDescription=row[4],
                price=row[5],
                constructionYear=row[6],
                walkScore=row[7],
                noRooms=row[8],
                noBathrooms=row[9],
                noBedrooms=row[10],
                noFireplaces=row[11],
                noGarages=row[12],
                noParkingLots=row[13],
                noPools=row[14],
                photoUrl=row[15],
                isNew=row[16],
                googleMapAddressLink=row[17],
                walkScoreMapped=row[18],
                livingArea=row[19],
                contactEmail=row[20],
                contactPhoneNumber=row[21],
            )
            apartment.save()
