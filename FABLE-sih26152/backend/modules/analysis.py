"""
Analysis module.
Owner: Charan (Analytics/Baseline + Evaluation)

Responsibilities:
- Sentiment analysis on any text columns
- Keyword/topic extraction
- Trend-over-time calculation
- A simple baseline method (e.g. keyword counting) to compare against,
  for the SIH evaluation requirement

Not implemented yet - placeholder for Phase 3.
"""

import pandas as pd


def analyze_sentiment(df: pd.DataFrame, text_column: str) -> dict:
    """Run sentiment analysis on a text column. TODO: implement."""
    raise NotImplementedError("Charan: implement sentiment analysis here")


def extract_keywords(df: pd.DataFrame, text_column: str) -> list:
    """Extract top keywords/topics from a text column. TODO: implement."""
    raise NotImplementedError("Charan: implement keyword extraction here")


def compute_trend(df: pd.DataFrame, date_column: str, value_column: str) -> dict:
    """Compute a simple trend over time. TODO: implement."""
    raise NotImplementedError("Charan: implement trend calculation here")
