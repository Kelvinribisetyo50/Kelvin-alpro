def make_car(manufacturer, model, **car_info):
    """Membuat dictionary yang menyimpan informasi tentang sebuah mobil."""
    car = {"manufacturer": manufacturer, "model": model}
    car.update(car_info)
    return car

car = make_car("subaru", "outback", color="blue", tow_package=True)
print(car)