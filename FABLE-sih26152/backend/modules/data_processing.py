"""
Data processing module.
Owner: Ashwin (Data/Backend + Integration)

Responsibilities:
- Parse uploaded files (CSV first, then Excel/JSON later)
- Clean and profile the data (missing values, column types, basic stats)
- Return a clean pandas DataFrame + a profile dict for the analysis module to use

Not implemented yet - this is a placeholder so the folder structure
and imports are ready for Phase 3, Task 1.
"""

import pandas as pd


def parse_csv(file_bytes: bytes) -> pd.DataFrame:
    """Parse raw CSV bytes into a DataFrame. TODO: implement."""
    raise NotImplementedError("Ashwin: implement CSV parsing here")


def profile_dataframe(df: pd.DataFrame) -> dict:
    """Return basic profile info: shape, dtypes, missing values, etc. TODO: implement."""
    raise NotImplementedError("Ashwin: implement profiling here")
