import anthropic
import os

client = anthropic.Anthropic(api_key=os.environ.get("ANTHROPIC_API_KEY"))

def generate_advisor_brief(profile: dict) -> str:
    prompt = f"""
    You are a financial advisor assistant. Given this client profile, 
    generate a concise pre-meeting brief with 3-4 talking points.
    
    Client Profile:
    - Name: {profile['name']}
    - Age: {profile['age']}
    - Risk Tolerance: {profile['risk_tolerance']}
    - Goals: {profile['goals']}
    - Portfolio Value: {profile['portfolio_value']}
    
    Format as a brief, professional summary followed by 3-4 bullet point talking points.
    """
    
    message = client.messages.create(
        model="claude-sonnet-4-6",
        max_tokens=1024,
        messages=[{"role": "user", "content": prompt}]
    )
    
    return message.content[0].text

def generate_followup_questions(profile: dict) -> str:
    prompt = f"""
    You are a financial advisor assistant. Given this client profile,
    generate 3 thoughtful follow-up questions the advisor should ask during the meeting.
    
    Client Profile:
    - Name: {profile['name']}
    - Age: {profile['age']}
    - Risk Tolerance: {profile['risk_tolerance']}
    - Goals: {profile['goals']}
    - Portfolio Value: {profile['portfolio_value']}
    
    Format as a numbered list of questions only.
    """
    
    message = client.messages.create(
        model="claude-sonnet-4-6",
        max_tokens=512,
        messages=[{"role": "user", "content": prompt}]
    )
    
    return message.content[0].text

if __name__ == "__main__":
    profile = {
        "name": "Sarah Chen",
        "age": 42,
        "risk_tolerance": "moderate",
        "goals": "retirement in 20 years, college fund for two kids",
        "portfolio_value": "$340,000"
    }

    print("=== ADVISOR PRE-MEETING BRIEF ===\n")
    print(generate_advisor_brief(profile))
    print("\n=== SUGGESTED FOLLOW-UP QUESTIONS ===\n")
    print(generate_followup_questions(profile))

