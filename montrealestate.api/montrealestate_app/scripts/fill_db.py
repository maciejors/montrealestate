import montrealestate_app.models as m
import csv


def run():
    with open('montrealestate.api/listings_final.csv', encoding='utf16') as file:
        reader = csv.reader(file)
        next(reader)

        m.Apartment.objects.all().delete()

        for row in reader:
            print(row)

            apartment = m.Apartment(
                address=row[0],
                city=row[1],
                district=row[2],
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
                apartment=row[22],
                commercial=row[23],
                detached=row[24],
                duplex=row[25],
                house=row[26],
                loftStudio=row[27],
                multiplex=row[28],
                other=row[29],
                quadruplex=row[30],
                triplex=row[31],
            )
            apartment.save()