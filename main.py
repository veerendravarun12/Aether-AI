import argparse
import sys
from aether.core.agent import AetherAgent

def run_research(target: str):
    """Initializes Aether Agent for market research tasks."""
    print(f"--- Aether-AI: Starting Research on {target} ---")
    agent = AetherAgent(name="Aether-Research-Unit")
    
    # Simulating data ingestion
    agent.ingest_data(target, {"status": "Research-Active", "volume": "High"})
    
    # Sentiment Example
    sentiment = agent.analyze_sentiment(f"Market sentiment for {target} seems bullish due to increased adoption.")
    print(f"Agent Prediction: {sentiment['sentiment']} (Score: {sentiment['score']})")
    
    # Generate Intelligence
    print(agent.generate_report())

def main():
    parser = argparse.ArgumentParser(description="Aether-AI Command Line Interface")
    parser.add_argument("--mode", type=str, choices=["research", "predict"], default="research",
                        help="The mode to run the Aether Engine in.")
    parser.add_argument("--target", type=str, default="Polymarket",
                        help="The target market or asset to analyze.")
    
    args = parser.parse_args()
    
    if args.mode == "research":
        run_research(args.target)
    else:
        print(f"Error: Mode {args.mode} is under development.")

if __name__ == "__main__":
    main()