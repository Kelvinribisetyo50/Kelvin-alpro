from user import Admin

hak_akses = [
    "can add post",
    "can delete post",
    "can ban user",
    "can edit user",
]
admin = Admin("Rina", "Kusuma", 35, "rina.kusuma@email.com", "Surakarta", hak_akses)
admin.privileges.show_privileges()