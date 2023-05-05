from trading_price.etl.transform import Transform
from trading_price.etl.load import Load
import pandas as pd
import os 
import shutil


def test_transform():
    # assemble 
    df_input = pd.DataFrame({
        "t": ["123", "124"],
        "x": ["A", "B"],
        "p": [10.1, 20.1],
        "s": [10, 20]
    })

    df_exchange_codes = pd.DataFrame({
        "exchange_code": ["A", "B"],
        "exchange_name": ["NYSE American (AMEX)", "NASDAQ OMX BX"]
    })

    df_expected = pd.DataFrame({
        "timestamp": ["123", "124"],
        "exchange": ["NYSE American (AMEX)", "NASDAQ OMX BX"],
        "price": [10.1, 20.1],
        "size": [10, 20]
    })

    # act 
    df_output = Transform.transform(df=df_input,df_exchange_codes=df_exchange_codes)

    # assert 
    pd.testing.assert_frame_equal(left=df_output, right=df_expected,check_exact=True)