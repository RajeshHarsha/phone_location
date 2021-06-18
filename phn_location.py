#importing_libraries 
import phonenumbers
from phonenumbers import carrier
from phonenumbers import geocoder

#clountry_code
cc = '+91'

#phone_number
number = input("with country code(includeing'+'): ")
ch_number = phonenumbers.parse(number,"CH")
#printing_geolocation
print(geocoder.description_for_number(ch_number,"en"))

s_number = phonenumbers.parse(number, "RO")
#printing_Service_provider_name
print(carrier.name_for_number(s_number,"en"))

