"""A simple HTTP client for API endpoints."""
from .components import (
    calculator,
    chronicle,
    daily,
    diary,
    geetest,
    hoyolab,
    lineup,
    transaction,
    wiki,
    wish,
)

__all__ = ["Client"]


class Client(
    chronicle.BattleChronicleClient,
    hoyolab.HoyolabClient,
    daily.DailyRewardClient,
    calculator.CalculatorClient,
    diary.DiaryClient,
    lineup.LineupClient,
    wiki.WikiClient,
    wish.WishClient,
    transaction.TransactionClient,
    geetest.GeetestClient,
):
    """A simple HTTP client for API endpoints."""
