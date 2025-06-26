from user_agents import parse

def detect_source(request):
    ua_string = request.META.get('HTTP_USER_AGENT', '')
    user_agent = parse(ua_string)

    if 'WhatsApp' in ua_string:
        return 'whatsapp'
    elif 'Instagram' in ua_string:
        return 'instagram'
    elif 'FB' in ua_string or 'Facebook' in ua_string:
        return 'facebook'
    elif user_agent.is_mobile:
        return 'mobile'
    elif user_agent.is_tablet:
        return 'tablet'
    elif user_agent.is_pc:
        return 'desktop'
    return 'unknown'
