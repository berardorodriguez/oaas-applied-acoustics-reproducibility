#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from pathlib import Path
import pandas as pd
import numpy as np

MASTER = Path("data/OAAS_master_projected_with_noise_reference.csv")
S7 = Path("data/Table_S7_OAAS_full_ranking.csv")
OUT = Path("data/Table_S7_noise_only.csv")

def euclid(a,b):
    return np.sqrt(((a-b)**2).sum())

def main():

    master = pd.read_csv(MASTER)
    s7 = pd.read_csv(S7)

    master["domain"] = master["domain"].astype(str)

    noise = master[master["domain"].str.contains("noise",case=False,na=False)].copy()

    print("Noise rows:",len(noise))
    print(noise[["file","domain"]])

    # reconstruir centroides POS y NEG desde S7
    pos_centroid = s7.loc[s7["delta_euclid"] < 0, ["OAAS1","OAAS2","OAAS3"]].mean().values
    neg_centroid = s7.loc[s7["delta_euclid"] > 0, ["OAAS1","OAAS2","OAAS3"]].mean().values

    rows = []

    for _,r in noise.iterrows():

        p = np.array([r.OAAS1,r.OAAS2,r.OAAS3])

        dpos = euclid(p,pos_centroid)
        dneg = euclid(p,neg_centroid)

        rows.append({
            "file":r.file,
            "d_pos_euclid":dpos,
            "d_neg_euclid":dneg
        })

    out = pd.DataFrame(rows)

    OUT.parent.mkdir(parents=True,exist_ok=True)
    out.to_csv(OUT,index=False)

    print("OK ->",OUT)
    print(out)

if __name__ == "__main__":
    main()