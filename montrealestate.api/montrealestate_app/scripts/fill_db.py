from montrealestate_app.models import Apartment

import csv


def run():
    with open('listings_final.csv', encoding='utf16') as file:
        reader = csv.reader(file)
        next(reader)

        Apartment.objects.all().delete()

        for row in reader:
            print(row)

            apartment = Apartment(
                latitude=row[0],
                longitude=row[1],
                address=row[2],
                city=row[3],
                district=row[4],
                postalCode=row[5],
                longDescription=row[6],
                price=row[7],
                category=row[8],
                constructionYear=row[9],
                walkScore=row[10],
                noRooms=row[11],
                noBedrooms=row[12],
                noFireplaces=row[13],
                noGarages=row[14],
                noParkingLots=row[15],
                noPools=row[16],
                photoUrl=row[17],
                isNew=row[18],
                googleMapAddressLink=row[19],
                walkScoreMapped=row[20],
                livingArea=row[21],
                contactEmail=row[22],
                contactPhoneNumber=row[23],
                noBathrooms=row[24]
            )
            print('done')
            apartment.save()
