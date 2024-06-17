def parse_user_agent(user_agent_string):
    os_name = "Unknown"
    os_architecture = "Unknown"
    os_type = "Unknown"
    browser_name = "Unknown"
    browser_version = "Unknown"

    if 'Windows' in user_agent_string:
        os_info = user_agent_string.split('(')[1].split(')')[0]
        os_info_parts = os_info.split('; ')
        if len(os_info_parts) >= 3:
            os_name = os_info_parts[0]
            os_architecture = os_info_parts[1]
            os_type = os_info_parts[2]
        elif len(os_info_parts) == 2:
            os_name = os_info_parts[0]
            os_architecture = os_info_parts[1]
        elif len(os_info_parts) == 1:
            os_name = os_info_parts[0]

    if 'Chrome' in user_agent_string and 'Edg' in user_agent_string:
        browser_name = 'Edge'
        browser_version = user_agent_string.split('Edg/')[1].split(' ')[0]
    elif 'Chrome' in user_agent_string:
        browser_name = 'Chrome'
        browser_version = user_agent_string.split('Chrome/')[1].split(' ')[0]

    return {
        "os_name": os_name,
        "os_architecture": os_architecture,
        "os_type": os_type,
        "browser_name": browser_name,
        "browser_version": browser_version
    }