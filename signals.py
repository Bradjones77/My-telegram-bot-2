import random

def get_trade_signal(trade_type="general"):
    coins = ["BTC/USDT", "ETH/USDT", "ADA/USDT", "XRP/USDT"]
    actions = ["BUY", "SELL"]

    coin = random.choice(coins)
    action = random.choice(actions)
    stop_loss = round(random.uniform(0.5, 5.0), 2)  # %
    confidence = round(random.uniform(70, 95), 2)  # %

    return {
        "coin": coin,
        "action": action,
        "stop_loss": stop_loss,
        "confidence": confidence,
        "type": trade_type
    }
