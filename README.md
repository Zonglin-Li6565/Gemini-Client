# Gemini client implimented in python

So far only has support for market data, and interface is TUI

## Run

```bash
python run.py
```
## Project Goals:

General goal: build up an automatic trading system of crypto curencies.

Components:

  - Platform system:

    - Automatic price data collection
    - Order sumbission system (should also block risky orders)
    - Maybe a simulated matching engine for model training

  - ML models:

    - Uses platform API
