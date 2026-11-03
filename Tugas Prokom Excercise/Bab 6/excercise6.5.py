rivers = {
    "nile": "egypt",
    "amazon": "brazil",
    "yangtze": "china",
}
for river, country in rivers.items():
    print(f"The {river.title()} runs through {country.title()}.")
print("\nSungai dalam dictionary:")
for river in rivers.keys():
    print(river.title())
print("\nNegara dalam dictionary:")
for country in rivers.values():
    print(country.title())