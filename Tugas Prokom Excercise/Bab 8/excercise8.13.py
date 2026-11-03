def build_profile(first, last, **user_info):
    """Membuat dictionary yang berisi semua yang kita ketahui tentang pengguna."""
    user_info["first_name"] = first
    user_info["last_name"] = last
    return user_info

user_profile = build_profile(
    "Kelvin",
    "Ribisetyo",
    location="Pemalang",
    field="Industrial Engineering",
    hobby="futsal",
)
print(user_profile)