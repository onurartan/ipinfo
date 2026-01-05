from user_agents import parse

def parse_user_agent(user_agent_str: str):
    if not user_agent_str:
        return {
            "os_name": "Unknown",
            "os_architecture": "Unknown",
            "os_type": "Unknown",
            "browser_name": "Unknown",
            "browser_version": "Unknown",
        }
    user_agent = parse(user_agent_str)
    return {
        "browser_name": user_agent.browser.family,
        "browser_version": user_agent.browser.version_string,
        "os_name": user_agent.os.family,
        "os_version": user_agent.os.version_string,
        "os_architecture": "Unknown",
        "os_type": user_agent.device.family,
        "device": user_agent.device.family,
        "is_mobile": user_agent.is_mobile,
        "is_tablet": user_agent.is_tablet,
        "is_pc": user_agent.is_pc,
        "is_bot": user_agent.is_bot,
    }


# Test with example user agent strings
user_agent_string_1 = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 Edg/126.0.0.0"
user_agent_string_2 = "Mozilla/5.0 (Linux; Android 10; SM-G960F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.181 Mobile Safari/537.36"
user_agent_string_3 = "Mozilla/5.0 (iPhone; CPU iPhone OS 15_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.0 Mobile/15E148 Safari/604.1"

# parsed_1 = parse_user_agent(user_agent_string_1)
# parsed_2 = parse_user_agent(user_agent_string_2)
# parsed_3 = parse_user_agent(user_agent_string_3)

# print(parsed_1)
# print(parsed_2)
# print(parsed_3)
