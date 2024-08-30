#!/usr/bin/env python3

def map_range(value, src_min, src_max, tgt_min, tgt_max):
    scale = (tgt_max - tgt_min) / (src_max - src_min)
    
    return tgt_min + (value - src_min) * scale