from flask import Flask, jsonify

app = Flask(__name__)

san_fran_breweries = [
    {
        "id": 385,
        "name": "Black Hammer Brewing",
        "brewery_type": "micro",
        "street": "544 Bryant St",
        "city": "San Francisco",
        "state": "California",
        "postal_code": "94107-1217",
        "country": "United States",
        "longitude": "-122.3969947",
        "latitude": "37.780655",
        "phone": "4155002273",
        "website_url": "http://www.blackhammerbrewing.com",
        "updated_at": "2018-08-23T23:25:33.033Z",
        "tag_list": []
    },
    {
        "id": 612,
        "name": "Fort Point Beer Company",
        "brewery_type": "regional",
        "street": "644 Mason St",
        "city": "San Francisco",
        "state": "California",
        "postal_code": "94129-1600",
        "country": "United States",
        "longitude": "-122.410227755102",
        "latitude": "37.789461244898",
        "phone": "4159064021",
        "website_url": "http://www.fortpointbeer.com",
        "updated_at": "2018-08-23T23:28:36.026Z",
        "tag_list": []
    },
    {
        "id": 804,
        "name": "Magnolia Dogpatch",
        "brewery_type": "micro",
        "street": "2505 3rd St",
        "city": "San Francisco",
        "state": "California",
        "postal_code": "94107-3112",
        "country": "United States",
        "longitude": "-122.3880818",
        "latitude": "37.7577437",
        "phone": "4158647468",
        "website_url": "http://www.magnoliasmokestack.com",
        "updated_at": "2018-08-23T23:59:22.426Z",
        "tag_list": []
    },
    {
        "id": 1069,
        "name": "Sufferfest Beer Company",
        "brewery_type": "proprietor",
        "street": "1770 UNION STREET",
        "city": "San Francisco",
        "state": "California",
        "postal_code": "94123-3404",
        "country": "United States",
        "longitude": "-122.428394714286",
        "latitude": "37.7980748571429",
        "phone": "4152386431",
        "website_url": "http://www.sufferfestbeer.com",
        "updated_at": "2018-08-24T00:03:23.447Z",
        "tag_list": []
    },
    {
        "id": 1182,
        "name": "Woods CervecerÃ­a",
        "brewery_type": "brewpub",
        "street": "3801 18th St",
        "city": "San Francisco",
        "state": "California",
        "postal_code": "94114-2615",
        "country": "United States",
        "longitude": "-122.4285438",
        "latitude": "37.761163",
        "phone": "4152739295",
        "website_url": "http://www.cerveceriasf.com",
        "updated_at": "2018-08-24T00:05:03.005Z",
        "tag_list": []
    },
    {
        "id": 354,
        "name": "Beach Chalet Brewing Co",
        "brewery_type": "brewpub",
        "street": "1000 Great Hwy",
        "city": "San Francisco",
        "state": "California",
        "postal_code": "94121-3268",
        "country": "United States",
        "longitude": "-122.502981",
        "latitude": "37.7252994",
        "phone": "4153868439",
        "website_url": "http://www.beachchalet.com",
        "updated_at": "2018-08-23T23:25:04.285Z",
        "tag_list": []
    },
    {
        "id": 271,
        "name": "21st Amendment Brewery Cafe",
        "brewery_type": "brewpub",
        "street": "563 2nd St",
        "city": "San Francisco",
        "state": "California",
        "postal_code": "94107-1411",
        "country": "United States",
        "longitude": "-122.3925769",
        "latitude": "37.782448",
        "phone": "4153690900",
        "website_url": "http://www.21st-amendment.com",
        "updated_at": "2018-08-23T23:23:46.486Z",
        "tag_list": []
    },
    {
        "id": 277,
        "name": "47 Hills Brewing Co",
        "brewery_type": "brewpub",
        "street": "137 S Linden Ave",
        "city": "South San Francisco",
        "state": "California",
        "postal_code": "94080-6410",
        "country": "United States",
        "longitude": "-122.413616770068",
        "latitude": "37.64425595",
        "phone": "6508678476",
        "website_url": "http://47hillsbrewingcompany.com",
        "updated_at": "2018-08-23T23:23:51.427Z",
        "tag_list": []
    },
    {
        "id": 323,
        "name": "Armstrong Brewing Co",
        "brewery_type": "micro",
        "street": "415 Grand Ave Ste 103",
        "city": "South San Francisco",
        "state": "California",
        "postal_code": "94080-3614",
        "country": "United States",
        "longitude": None,
        "latitude": None,
        "phone": "6509898447",
        "website_url": "http://www.armstrongbrewing.com",
        "updated_at": "2018-08-11T21:35:54.842Z",
        "tag_list": []
    },
    {
        "id": 314,
        "name": "Anchor Brewing Co",
        "brewery_type": "large",
        "street": "1705 Mariposa St",
        "city": "San Francisco",
        "state": "California",
        "postal_code": "94107-2334",
        "country": "United States",
        "longitude": "-122.4011065",
        "latitude": "37.7630772",
        "phone": "4158638350",
        "website_url": "http://www.anchorbrewing.com",
        "updated_at": "2018-08-23T23:24:25.576Z",
        "tag_list": []
    },
    {
        "id": 342,
        "name": "Barebottle Brewing Company",
        "brewery_type": "micro",
        "street": "1525 Cortland Ave",
        "city": "San Francisco",
        "state": "California",
        "postal_code": "94110-5714",
        "country": "United States",
        "longitude": "-122.40904048683",
        "latitude": "37.74000915",
        "phone": "4159268617",
        "website_url": "http://www.barebottlebeer.com",
        "updated_at": "2018-08-23T23:24:53.170Z",
        "tag_list": []
    },
    {
        "id": 348,
        "name": "Barrel Head Brewhouse",
        "brewery_type": "brewpub",
        "street": "1785 Fulton St",
        "city": "San Francisco",
        "state": "California",
        "postal_code": "94117-1202",
        "country": "United States",
        "longitude": "-122.446103285714",
        "latitude": "37.7757651428571",
        "phone": "4154166989",
        "website_url": "http://www.barrelheadsf.com",
        "updated_at": "2018-08-23T23:24:58.559Z",
        "tag_list": []
    },
    {
        "id": 350,
        "name": "Bartlett Hall",
        "brewery_type": "brewpub",
        "street": "242 Ofarrell St",
        "city": "San Francisco",
        "state": "California",
        "postal_code": "94102-2119",
        "country": "United States",
        "longitude": "-122.40872925",
        "latitude": "37.786406375",
        "phone": "4154334332",
        "website_url": "http://www.bartletthall.com",
        "updated_at": "2018-08-23T23:25:00.369Z",
        "tag_list": []
    },
    {
        "id": 389,
        "name": "Black Sands Brewery",
        "brewery_type": "micro",
        "street": "701 Haight St",
        "city": "San Francisco",
        "state": "California",
        "postal_code": "94117-3316",
        "country": "United States",
        "longitude": "-122.433863",
        "latitude": "37.7715719",
        "phone": "4155345194",
        "website_url": "",
        "updated_at": "2018-08-23T23:25:36.178Z",
        "tag_list": []
    },
    {
        "id": 417,
        "name": "Brewery in Planning - Calistoga",
        "brewery_type": "planning",
        "street": "",
        "city": "San Francisco",
        "state": "California",
        "postal_code": "94117-1576",
        "country": "United States",
        "longitude": "-122.4192363",
        "latitude": "37.7792808",
        "phone": "",
        "website_url": "",
        "updated_at": "2018-08-23T23:26:00.691Z",
        "tag_list": []
    },
    {
        "id": 469,
        "name": "Cellarmaker Brewing Company",
        "brewery_type": "micro",
        "street": "1150 Howard St",
        "city": "San Francisco",
        "state": "California",
        "postal_code": "94103-3914",
        "country": "United States",
        "longitude": "-122.4106996",
        "latitude": "37.7771589",
        "phone": "4158633940",
        "website_url": "http://www.cellarmakerbrewing.com",
        "updated_at": "2018-08-23T23:26:34.822Z",
        "tag_list": []
    },
    {
        "id": 591,
        "name": "Ferment.Drink.Repeat",
        "brewery_type": "micro",
        "street": "2636 San Bruno Ave",
        "city": "San Francisco",
        "state": "California",
        "postal_code": "94134-1507",
        "country": "United States",
        "longitude": "-122.403999122449",
        "latitude": "37.7283367755102",
        "phone": "",
        "website_url": "",
        "updated_at": "2018-08-23T23:28:18.211Z",
        "tag_list": []
    },
    {
        "id": 656,
        "name": "Hardwood Bar and Smokery",
        "brewery_type": "brewpub",
        "street": "680 8th St Ste 170",
        "city": "San Francisco",
        "state": "California",
        "postal_code": "94103",
        "country": "United States",
        "longitude": None,
        "latitude": None,
        "phone": "4157962437",
        "website_url": "http://www.hardwoodsf.com",
        "updated_at": "2018-08-11T21:36:05.741Z",
        "tag_list": []
    },
    {
        "id": 658,
        "name": "Harmonic Brewing",
        "brewery_type": "micro",
        "street": "1050 26th St",
        "city": "San Francisco",
        "state": "California",
        "postal_code": "94107-3513",
        "country": "United States",
        "longitude": "-122.390096163265",
        "latitude": "37.7514996122449",
        "phone": "4158726817",
        "website_url": "http://www.harmonicbrewing.com",
        "updated_at": "2018-08-23T23:29:14.130Z",
        "tag_list": []
    },
    {
        "id": 752,
        "name": "K-Oz Restaurant Brewery",
        "brewery_type": "brewpub",
        "street": "121 7th St",
        "city": "San Francisco",
        "state": "California",
        "postal_code": "94103-2835",
        "country": "United States",
        "longitude": "-122.409904",
        "latitude": "37.7786408",
        "phone": "4158729431",
        "website_url": "http://www.kandoz.com",
        "updated_at": "2018-08-23T23:58:37.200Z",
        "tag_list": []
    }
]

@app.route('/breweries', methods=['GET'])
def get_breweries():
    return jsonify(san_fran_breweries)

if __name__ == '__main__':
    app.run(debug=True)
