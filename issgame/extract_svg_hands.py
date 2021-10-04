#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pandas as pd
import numpy as np
import issgame
from typing import List


def extract_svg_hands(raw_files: List[str], converted_file: str, testing=False) -> None:
    """
    Converts a list of .svg (ISS games) files into a a single csv-formatted
    file which contains information on each hand dealt to each player in each
    of the games in the original file. The original files are left unchanged.

    Args:
        raw_files (List[str]): Input filename strings (.sgv ISS game files).
        converted_file (str): Output filename
        testing (bool, optional): Read a small part of files. Defaults to False.
    """
    df_list = []
    # skip all rows higher than 5000 if testing
    skiprows = (lambda x: x < 5000) if testing else -1
    for raw_file in raw_files:
        df_list.append(pd.read_csv(raw_file, header=None, skiprows=skiprows))

    infile = pd.concat(df_list)

    outfile = pd.DataFrame([])
    for __i, row in infile.iterrows():
        temp_frame = pd.DataFrame(
            issgame.GameLine(row[0]).get_all_file_strings()
        )
        outfile = pd.concat([outfile, temp_frame])

    np.savetxt(converted_file, outfile.values, fmt="%s", delimiter=",")
