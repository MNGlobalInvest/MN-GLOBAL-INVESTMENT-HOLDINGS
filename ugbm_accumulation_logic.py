name: MN Global Autonomous Accumulator

on:
  schedule:
    # Runs every day at 00:00 UTC (The "Always-On" Business Heartbeat)
    - cron: '0 0 * * *'
  workflow_dispatch: # Allows you to trigger it manually for testing

jobs:
  accumulate:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout Repository
        uses: actions/checkout@v4

      - name: Set up Python
        uses: actions/setup-python@v4
        with:
          python-version: '3.10'

      - name: Install Dependencies
        run: |
          pip install pandas requests ta

      - name: Run Accumulation Logic
        run: python ugbm_accumulation_logic.py
        env:
          # If you eventually use a Private API or Node, add secrets here
          COINGECKO_API_KEY: ${{ secrets.COINGECKO_API_KEY }}
