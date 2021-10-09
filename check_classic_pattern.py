from decimal import Decimal
from classic_strategy import Order
from classic_strategy import fidelity_promo, bulk_item_promo, large_order_promo

promos = [
    promo
    for name, promo in globals().items()
    if name.endswith("_promo") and name != "best_promo"
]


def best_promo(order: Order) -> Decimal:
    """Compute the best discount available"""
    return max(promo(order) for promo in promos)
