from Samples.geocoder import geocode


def get_address_coords(address):
    toponym = geocode(address)

    toponym_address = toponym["metaDataProperty"]["GeocoderMetaData"]["text"]
    toponym_coodrinates = toponym["Point"]["pos"]
    return toponym_coodrinates


def main():
    # Получение координат по адресу.
    for address in ["Москва, Красная площадь, 1"]:
        coords = get_address_coords(address)
        print(f"{address} имеет координаты: {coords}")
    print("")


if __name__ == "__main__":
    main()
