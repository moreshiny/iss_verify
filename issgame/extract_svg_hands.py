#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pandas as pd
import os
import issgame
from typing import List


def extract_svg_hands(raw_files: List[str],
                      converted_file: str,
                      testing: bool = False
                      ) -> None:
    """
    Converts a list of .svg (ISS games) files into a a single csv-formatted
    file which contains information on each hand dealt to each player in each
    of the games in the original file. The original files are left unchanged.

    Args:
        raw_files (List[str]): Input filename strings (.sgv ISS game files).
        converted_file (str): Output filename
        testing (bool, optional): Read a small part of files. Defaults to False.
    """
    CHUNKSIZE = 128

    include_header_line = True
    if os.path.isfile(converted_file):
        os.remove(converted_file)
    for raw_file in raw_files:
        reader = pd.read_csv(raw_file, chunksize=CHUNKSIZE, header=None)

        for chunk in reader:
            chunk.columns = ['imported_line']
            hand_frames = []

            for line in chunk.loc[:, 'imported_line']:
                hand_frames.append(issgame.GameLine(line).get_hands())

            all_hands = pd.concat(hand_frames)
            all_hands.to_csv(
                converted_file,
                index=False,
                header=include_header_line,
                sep="\t",
                mode='a'
            )
            include_header_line = False
