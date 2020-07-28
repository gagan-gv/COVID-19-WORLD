import COVID19Py as cv
covid = cv.COVID19()
countrycode=input("Enter the country code: ").upper()
location=covid.getLocationByCountryCode(countrycode)
loc_data=location[0]
virus_data=dict(loc_data['latest'])
print("India: ", virus_data)
