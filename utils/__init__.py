from user_agents import parse

# if you use manuel
# def parse_user_agent(user_agent_string):
#     os_name = "Unknown"
#     os_architecture = "Unknown"
#     os_type = "Unknown"
#     browser_name = "Unknown"
#     browser_version = "Unknown"

#     # Check for Windows OS
#     if 'Windows' in user_agent_string:
#         os_info = user_agent_string.split('(')[1].split(')')[0]
#         os_info_parts = os_info.split('; ')
#         if len(os_info_parts) >= 3:
#             os_name = os_info_parts[0]
#             os_architecture = os_info_parts[1]
#             os_type = os_info_parts[2]
#         elif len(os_info_parts) == 2:
#             os_name = os_info_parts[0]
#             os_architecture = os_info_parts[1]
#         elif len(os_info_parts) == 1:
#             os_name = os_info_parts[0]

#     # Check for Android OS
#     elif 'Android' in user_agent_string:
#         os_name = 'Android'
#         os_info = user_agent_string.split('(')[1].split(')')[0]
#         os_info_parts = os_info.split('; ')
#         if len(os_info_parts) >= 3:
#             os_architecture = os_info_parts[1]
#             os_type = os_info_parts[2]
#             if len(os_info_parts) >= 4 and 'Build' in os_info_parts[3]:
#                 device_model = os_info_parts[3].split('Build/')[1]
#         elif len(os_info_parts) == 2:
#             os_architecture = os_info_parts[1]
#             os_type = os_info_parts[1]
#         elif len(os_info_parts) == 1:
#             os_architecture = os_info_parts[0]

#     # Check for iOS
#     elif 'iPhone' in user_agent_string or 'iPad' in user_agent_string:
#         os_name = 'iOS'
#         if 'iPhone' in user_agent_string:
#             os_type = 'iPhone'
#         elif 'iPad' in user_agent_string:
#             os_type = 'iPad'

#     # Check for macOS
#     elif 'Macintosh' in user_agent_string or 'Mac OS X' in user_agent_string:
#         os_name = 'macOS'

#     # Check for Linux
#     elif 'Linux' in user_agent_string:
#         os_name = 'Linux'

#     # Check for Chrome browser
#     if 'Chrome' in user_agent_string:
#         browser_name = 'Chrome'
#         browser_version = user_agent_string.split('Chrome/')[1].split(' ')[0]

#     # Check for Edge browser (Chromium based)
#     elif 'Edg' in user_agent_string:
#         browser_name = 'Edge'
#         browser_version = user_agent_string.split('Edg/')[1].split(' ')[0]

#     return {
#         "os_name": os_name,
#         "os_architecture": os_architecture,
#         "os_type": os_type,
#         "browser_name": browser_name,
#         "browser_version": browser_version,
#     }


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
