#
# Copyright (c) 2022 Airbyte, Inc., all rights reserved.
#


import sys

from airbyte_cdk.entrypoint import launch
from source_alpaca_trades import SourceAlpacaTrades

if __name__ == "__main__":
    source = SourceAlpacaTrades()
    launch(source, sys.argv[1:])
