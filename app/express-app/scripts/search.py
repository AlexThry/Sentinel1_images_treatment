import asf_search as asf
import argparse
import traceback
import json



def search(poligon, date_start, date_end):
    results = asf.geo_search(
    intersectsWith=poligon,
    platform=asf.PLATFORM.SENTINEL1A,
    processingLevel=asf.PRODUCT_TYPE.SLC,
    beamSwath='IW',
    flightDirection=asf.FLIGHT_DIRECTION.DESCENDING,
    polarization=asf.POLARIZATION.VV_VH,
    start=date_start,
    end=date_end,)
    return results


if __name__ == "__main__":    
    # Créer l'objet ArgumentParser
    parser = argparse.ArgumentParser(description='Recherche des images Sentinel-1 sur ASF.')

    try:
        # Ajouter les arguments
        parser.add_argument('--poligon', type=str, help='Le poligon pour la recherche')
        parser.add_argument('--date_start', type=str, help='La date de début pour la recherche')
        parser.add_argument('--date_end', type=str, help='La date de fin pour la recherche')

        # Parser les arguments
        args = parser.parse_args()

        result = search(args.poligon, args.date_start, args.date_end)
        with open("./data/search_data_output/output.json", "w") as f:
            f.write(str(result))


    except Exception as e:
        traceback.print_exc()