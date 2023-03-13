from agent.agents.digital_twin import DigitalTwin
from agent.config import config
import os

if __name__ == "__main__":
    absolute_path = os.path.abspath("daodao-agent/agent_config.json")
    print(absolute_path)
    agent = DigitalTwin(
        config=config.Config(config_path=absolute_path), bot_type="discord"
    )
    agent.run()
