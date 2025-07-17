from typing import List, Optional
from pydantic import HttpUrl
from src.domain.models.account import Account

def extract_account_name_from_title(title: str) -> str:
    # Assumes account name is in format like "@accountname"
    import re
    match = re.search(r'@(\w+)', title)
    return match.group(1) if match else "unknown"

def extract_thumbnail(item: dict) -> Optional[HttpUrl]:
    # Try to get image from thumbnail or fallback
    pagemap = item.get("pagemap", {})
    thumbnail = pagemap.get("cse_thumbnail", [{}])
    image = thumbnail[0].get("src") if thumbnail else None

    # Optional: fallback to cse_image
    if not image:
        images = pagemap.get("cse_image", [{}])
        image = images[0].get("src") if images else None

def map_google_response_to_accounts(raw: dict, liked_accounts: set[str]) -> List[Account]:
    accounts = []
    for item in raw.get("items", []):
        title = item.get("title", "")
        name = extract_account_name_from_title(title)
        link = item.get("link", "")
        snippet = item.get("snippet", "")
        image = extract_thumbnail(item)
        like = name in liked_accounts

        accounts.append(Account(
            name=name,
            title=title,
            link=link,
            snippet=snippet,
            image=image,
            like=like
        ))

    return accounts