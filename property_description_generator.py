# Real Estate AI - Property Description Generator
# Built with Claude AI | 10th Dimension

import anthropic

client = anthropic.Anthropic(api_key="YOUR_API_KEY_HERE")

def generate_property_description(property_details: dict) -> str:
    """
    Generate a professional property listing description using Claude AI.
    
    Args:
        property_details (dict): Dictionary containing property information
    
    Returns:
        str: AI-generated property description
    """
    prompt = f"""
You are a professional real estate copywriter. Generate an engaging and persuasive property listing description based on the following details:

Property Type: {property_details.get('type', 'Residential')}
Location: {property_details.get('location', '')}
Area: {property_details.get('area', '')} sq ft
Bedrooms: {property_details.get('bedrooms', '')}
Bathrooms: {property_details.get('bathrooms', '')}
Price: {property_details.get('price', '')}
Key Features: {', '.join(property_details.get('features', []))}
Nearby Amenities: {', '.join(property_details.get('amenities', []))}

Write a compelling 150-200 word description that highlights the best features and appeals to potential buyers.
"""

    message = client.messages.create(
        model="claude-opus-4-5",
        max_tokens=1024,
        messages=[
            {"role": "user", "content": prompt}
        ]
    )
    
    return message.content[0].text


def generate_followup_email(client_name: str, property_name: str, viewing_date: str) -> str:
    """
    Generate a follow-up email for a property viewing.
    
    Args:
        client_name (str): Name of the client
        property_name (str): Name/address of the property
        viewing_date (str): Date of the property viewing
    
    Returns:
        str: AI-generated follow-up email
    """
    prompt = f"""Write a professional and warm follow-up email to a potential property buyer.

Client Name: {client_name}
Property: {property_name}
Viewing Date: {viewing_date}

The email should:
- Thank them for visiting the property
- Highlight 2-3 key benefits of the property
- Invite them to ask questions
- Include a soft call-to-action
Keep it under 150 words and professional yet friendly."""

    message = client.messages.create(
        model="claude-opus-4-5",
        max_tokens=1024,
        messages=[
            {"role": "user", "content": prompt}
        ]
    )
    
    return message.content[0].text


# Example Usage
if __name__ == "__main__":
    # Sample property details
    property_info = {
        "type": "3BHK Apartment",
        "location": "Hinjewadi Phase 2, Pune",
        "area": "1450",
        "bedrooms": "3",
        "bathrooms": "2",
        "price": "₹85 Lakhs",
        "features": ["East Facing", "Modular Kitchen", "Covered Parking", "24x7 Security"],
        "amenities": ["IT Park - 0.5 km", "School - 1 km", "Hospital - 2 km", "Metro Station - 3 km"]
    }
    
    print("=== Property Description ===")
    description = generate_property_description(property_info)
    print(description)
    
    print("\n=== Follow-up Email ===")
    email = generate_followup_email("Rahul Sharma", "Hinjewadi Apartment", "29 March 2026")
    print(email)
