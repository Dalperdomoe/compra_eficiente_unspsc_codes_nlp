# -*- coding: utf-8 -*-
import os


SOCRATA_DOMAIN = 'www.datos.gov.co'
SOCRATA_DATASET_IDENTIFIER = 'jbjy-vk9h'
SOCRATA_TOKEN = os.environ.get("SODAPY_APPTOKEN")

CURRENT_DIR = os.path.abspath(os.path.dirname(__file__))
RAW_DATA_DIR = os.path.join(
    CURRENT_DIR,
    os.pardir,
    os.pardir,
    "data",
    "raw"
)
RAW_DATA_FILE = os.path.join(
    RAW_DATA_DIR,
    'raw_data.csv'
)


def secop2_data_generator():
    """ Create SECOP II raw data using the sodapy package.
    """

    import pandas as pd
    from sodapy import Socrata

    client = Socrata(SOCRATA_DOMAIN, SOCRATA_TOKEN)

    df = pd.DataFrame(
        client.get(
            SOCRATA_DATASET_IDENTIFIER,
            query="""
                SELECT descripcion_del_proceso,
                    codigo_de_categoria_principal
                WHERE date_extract_y(ultima_actualizacion) IN (
                                                            2017,
                                                            2018,
                                                            2019,
                                                            2021,
                                                            2022)
                AND date_extract_m(ultima_actualizacion) IN (3,6,9,12)
                LIMIT 500000
            """
        )
    )

    return df.to_csv(
        RAW_DATA_FILE,
        index=False
    )


if __name__ == '__main__':

    if not os.path.exists(RAW_DATA_FILE):

        secop2_data_generator()

    else:

        print("raw dataset already exists.")
