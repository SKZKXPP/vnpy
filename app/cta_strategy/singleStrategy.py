from app.cta_strategy.strategies.atr_rsi_strategy import AtrRsiStrategy
from vnpy.app.cta_strategy.backtesting import BacktestingEngine
from vnpy.app.cta_strategy.strategies.boll_channel_strategy import (
    BollChannelStrategy,
)
from datetime import datetime
if __name__ == '__main__':

    engine = BacktestingEngine()
    engine.set_parameters(
        vt_symbol="IF88.CFFEX",
        interval="1m",
        start=datetime(2018, 1, 1),
        end=datetime(2019, 1, 1),
        rate=3.0/10000,
        slippage=0.2,
        size=300,
        pricetick=0.2,
        capital=1_000_000,
    )

    engine.add_strategy(AtrRsiStrategy, {})
    engine.load_data()
    engine.run_backtesting()
    df = engine.calculate_result()
    engine.calculate_statistics()
    engine.show_chart()