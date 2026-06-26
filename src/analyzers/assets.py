"""
Asset Inventory
"""

def build_asset_inventory(events):

    assets = set()

    for event in events:

        if "Accepted password" in event:

            assets.add(event)

    return list(assets)
