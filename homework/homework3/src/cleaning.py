# src/cleaning.py
from __future__ import annotations
from typing import Iterable, Optional, Tuple
import pandas as pd
import numpy as np

def fill_missing_median(
    df: pd.DataFrame,
    columns: Optional[Iterable[str]] = None,
    by: Optional[Iterable[str]] = None
) -> pd.DataFrame:
    """
    Fill NaNs in numeric columns with median. If `by` is given, do group-wise medians.
    Returns a copy.
    """
    out = df.copy()
    if columns is None:
        columns = out.select_dtypes(include=[np.number]).columns

    if by is None:
        med = out[columns].median(numeric_only=True)
        out[columns] = out[columns].fillna(med)
    else:
        out[columns] = (
            out.groupby(list(by))[list(columns)]
              .transform(lambda g: g.fillna(g.median(numeric_only=True)))
        )
    return out


def drop_missing(
    df: pd.DataFrame,
    how: str = "any",
    thresh: Optional[int] = None,
    subset: Optional[Iterable[str]] = None
) -> pd.DataFrame:
    """
    Drop rows with missing values. Returns a copy.
    """
    return df.dropna(axis=0, how=how, thresh=thresh, subset=subset)


def normalize_data(
    df: pd.DataFrame,
    columns: Optional[Iterable[str]] = None,
    method: str = "zscore",
    clip_outliers: Optional[Tuple[float, float]] = None
) -> pd.DataFrame:
    """
    Normalize numeric columns (zscore or minmax). Optional winsorization via clip_outliers=(0.01,0.99).
    Returns a copy.
    """
    out = df.copy()
    if columns is None:
        columns = out.select_dtypes(include=[np.number]).columns

    work = out[columns].astype(float)

    if clip_outliers is not None:
        lo, hi = clip_outliers
        ql = work.quantile(lo)
        qh = work.quantile(hi)
        work = work.clip(lower=ql, upper=qh, axis=1)

    if method == "zscore":
        mu = work.mean()
        sigma = work.std(ddof=0).replace(0, np.nan)
        work = (work - mu) / sigma
    elif method == "minmax":
        mn = work.min()
        mx = work.max()
        denom = (mx - mn).replace(0, np.nan)
        work = (work - mn) / denom
    else:
        raise ValueError("method must be 'zscore' or 'minmax'")

    out[columns] = work
    return out
